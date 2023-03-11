# -*- coding:utf-8 -*-
# title           :ursina天体视图
# description     :ursina天体视图（天体效果展示用，需要安装 ursina）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina
from ursina import Ursina, window, Entity, Mesh, SmoothFollow, Texture, clamp, time, camera, color, mouse, Vec2, Vec3, \
    load_texture, held_keys

# from ursina.camera import OrthographicCamera
from math import sin, cos, radians
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
import random as rd
import os
from bodies import Body
import random
from simulators.views.body_view import BodyView
import numpy as np
import math

SCALE_FACTOR = 1e-6


class UrsinaPlayer(FirstPersonController):
    """

    """

    def __init__(self, position, targets=None):
        super().__init__()
        camera.fov = 100
        camera.rotation_y = 90
        self.planets = None
        if targets is not None:
            self.planets = []
            # targets = [view.planet.parent for view in targets]
            # targets_parent = Entity()
            for view in targets:
                # view.planet.parent = targets_parent
                self.planets.append(view.planet)
            # self.camera_adj(planets)
            #     # planets.append(view.planet)
            #
            # camera.add_script(SmoothFollow(targets_parent, offset=(0, 8, -20)))
        pos = np.array(position) * SCALE_FACTOR
        self.position = Vec3(pos[0], pos[1], pos[2])
        # 将摄像机位置设置为 x=0、y=1、z=0 的位置
        # camera.position = Vec3(pos[0], pos[1], pos[2])
        # self.position = Vec3(pos[0], pos[1], pos[2])
        # 将摄像机的观察角度绕 x 轴旋转 45 度，绕 y 轴旋转 0 度，绕 z 轴旋转 0 度
        camera.rotation = Vec3(45, 90, 0)

        # self.gravity = 0
        # self.vspeed = 400
        # self.speed = 1000
        # self.mouse_sensitivity = Vec2(160, 160)
        self.on_enable()
        # self.rotation_speed = 80

    def input(self, key):
        if key == "escape":
            if mouse.locked:
                self.on_disable()
            else:
                sys.exit()
        return super().input(key)


class Planet(Entity):
    def __init__(self, body_view: BodyView):
        self.body_view = body_view
        # 旋转速度和大小成反比（未使用真实数据）
        self.rotspeed = 30000 / self.body_view.raduis  # random.uniform(1.0, 2.0)
        self.rotMode = 'x'  # random.choice(["x", "y", "z"])
        self.name = body_view.name

        pos = body_view.position * body_view.body.distance_scale * SCALE_FACTOR
        scale = body_view.body.diameter * body_view.body.size_scale * SCALE_FACTOR

        if hasattr(body_view, "texture"):
            texture = load_texture(body_view.texture)
        else:
            texture = None

        super().__init__(
            model="sphere",
            scale=scale,
            texture=texture,
            color=color.white,
            position=pos,
            rotation=(0, 0, 0))

    def turn(self):
        pos = self.body_view.position * SCALE_FACTOR

        self.x = -pos[1]
        self.y = pos[2]
        self.z = pos[0]

        self.rotation_y -= self.rotspeed

    def input(self, key):
        if key == "enter":
            self.fastMode = 1 - self.fastMode


class UrsinaView(BodyView):
    """
    ursina天体视图（天体效果展示用）
    """

    def __init__(self, body: Body):
        BodyView.__init__(self, body)
        self.velocity = body.velocity

        self.planet = Planet(self)
        if body.has_rings:
            self.create_rings()

        if self.body.is_fixed_star:
            # 如果是恒星（如：太阳），自身会发光，则需要关闭灯光
            self.planet.set_light_off()

    def create_rings(self):
        """
        创建星环（使用土星贴图）
        :return:
        """
        scale = 3 * self.body.diameter * self.body.size_scale * SCALE_FACTOR
        pos = self.planet.position
        self.ring = Entity(model="circle", texture='../textures/saturnRings.jpg', scale=scale, position=pos,
                           rotation=(70, 0, 0), double_sided=True)
        # 假设星环自身会发光
        self.ring.set_light_off()

    def update(self):
        self.planet.turn()
        if hasattr(self, "light"):
            self.light.position = Vec3(self.planet.x, self.planet.y, self.planet.z)
        if hasattr(self, "lights"):
            for light in self.lights:
                light.position = Vec3(self.planet.x, self.planet.y, self.planet.z)

        if hasattr(self, "ring"):
            self.ring.position = Vec3(self.planet.x, self.planet.y, self.planet.z)

    def appear(self):
        pass

    def disappear(self):
        self.planet.disable()
