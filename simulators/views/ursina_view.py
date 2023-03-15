# -*- coding:utf-8 -*-
# title           :ursina天体视图
# description     :ursina天体视图（天体效果展示用，需要安装 ursina）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina
from ursina import Ursina, window, Entity, Mesh, SmoothFollow, Texture, clamp, time, \
    camera, color, mouse, Vec2, Vec3, Vec4, \
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
from simulators.views.ursina_mesh import create_sphere, create_torus, create_body_torus
import numpy as np
import math

SCALE_FACTOR = 5e-7
# 旋转因子为1，则为正常的转速
ROTATION_SPEED_FACTOR = 1.0
ROTATION_SPEED_FACTOR = 0.01


class UrsinaPlayer(FirstPersonController):
    """

    """
    body_rotation_speed_control = 1.0

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
        # self.position = Vec3(pos[0], pos[1], pos[2])
        # 将摄像机位置设置为 x=0、y=1、z=0 的位置
        camera.position = Vec3(pos[0], pos[1], pos[2])
        # self.position = Vec3(pos[0], pos[1], pos[2])
        # 将摄像机的观察角度绕 x 轴旋转 45 度，绕 y 轴旋转 0 度，绕 z 轴旋转 0 度
        # camera.rotation = Vec3(45, 90, 0)
        camera.rotation = Vec3(0, 0, 0)

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
        self.rotation_speed = self.body_view.body.rotation_speed
        self.rotMode = 'x'  # random.choice(["x", "y", "z"])
        self.name = body_view.name

        self.tails = {}
        b_color = self.body_view.body.color
        self.tail_color = Vec4(b_color[0], b_color[1], b_color[2], 0.1)

        pos = body_view.position * body_view.body.distance_scale * SCALE_FACTOR
        scale = body_view.body.diameter * body_view.body.size_scale * SCALE_FACTOR

        subdivisions = 32  # int(scale*20)

        if hasattr(body_view, "texture"):
            texture = load_texture(body_view.texture)
        else:
            texture = None

        if hasattr(self.body_view.body, "torus_starts"):
            model = create_torus(0.86, 1.02, 64)
            rotation = (90, 0, 0)
        else:
            model = create_sphere(0.5, subdivisions)
            rotation = (0, 0, 0)

        super().__init__(
            # model="sphere",
            model=model,
            scale=scale,
            texture=texture,
            color=color.white,
            position=pos,
            rotation=rotation,
            double_sided=True)

        if hasattr(self.body_view.body, "torus_starts"):
            self.set_light_off()

    def create_tails(self):
        tail_keys = []
        his_pos = self.body_view.body.his_position()
        for pos in his_pos:
            tail_key = str(pos)
            tail_keys.append(tail_key)

        tail_more = len(self.tails) - len(his_pos)

        # 先删除超过的 tail entity
        if tail_more > 0:
            for key, entity in self.tails.items():
                entity.visible = False
                entity.disable()
                del entity
                tail_more -= 1
                if tail_more <= 0:
                    break

        # 再增加
        for pos in his_pos:
            tail_key = str(pos)
            if tail_key not in self.tails.keys():
                # pass
                self.tails[tail_key] = self.create_tail(pos)

    def create_tail(self, pos):
        pos = pos * SCALE_FACTOR
        # sphere = create_sphere(0.5, 10)
        scale = self.body_view.planet.scale_x / 5
        tail = Entity(model="diamond", color=self.tail_color, scale=scale)  # ,
        tail.x = -pos[1]
        tail.y = pos[2]
        tail.z = pos[0]
        tail.set_light_off()
        return tail

    def turn(self):
        pos = self.body_view.position * SCALE_FACTOR

        self.x = -pos[1]
        self.y = pos[2]
        self.z = pos[0]

        dt = 0
        if hasattr(self.body_view.body, "dt"):
            dt = self.body_view.body.dt
        if self.rotation_speed is None or dt == 0:
            self.rotspeed = 0
            # 旋转速度和大小成反比（未使用真实数据）
            # self.rotspeed = 30000 / self.body_view.raduis  # random.uniform(1.0, 2.0)
        else:
            # 是通过月球保持一面面对地球，调整得到
            self.rotspeed = self.rotation_speed * (dt / 3600) / 2.4 * ROTATION_SPEED_FACTOR  # / 60 / 24
            # rotation_speed 度/小时  dt 秒 = (dt / 3600)小时

        self.rotation_y -= self.rotspeed

        # self.create_tails()

    # def input(self, key):
    #     if key == "enter":
    #         self.fastMode = 1 - self.fastMode


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

    #     self.create_glow()
    #
    # def create_glow(self):
    #     # self.body.color
    #     # for i in range(1):
    #     b_color = self.body.color
    #     color = Vec4(b_color[0], b_color[1], b_color[2], 0.2)
    #         # glow_entity = Entity(parent=self.planet, model='sphere', color=color,
    #         #                      scale=math.pow(1.2, i), alpha=0.2)
    #
    #     glow_entity = Entity(parent=self.planet, model='sphere', color=color,
    #                          scale=1.01, alpha=0.1)
    #     glow_entity.set_light_off()

    def create_rings(self):
        """
        创建行星环（使用土星贴图）
        :return:
        """
        # 行星环偏移角度
        # self.ring_rotation_x = 80
        # 创建行星环
        # self.ring = Entity(parent=self.planet, model='circle', texture='../textures/saturnRings.jpg', scale=3.5,
        #                    rotation=(self.ring_rotation_x, 0, 0), double_sided=True)

        # 行星环偏移角度
        self.ring_rotation_x = 80
        # 创建行星环
        torus = create_torus(0.7, 1.2, 64)
        self.ring = Entity(parent=self.planet, model=torus, texture='../textures/saturnRings.jpg', scale=1,
                           rotation=(self.ring_rotation_x, 0, 0), double_sided=True)

        # 设置行星环不受灯光影响，否则看不清行星环
        self.ring.set_light_off()

    def update(self):
        """

        :return:
        """
        self.planet.turn()
        # 如果有行星环
        if hasattr(self, "ring"):
            # 如果有行星环，则不让行星环跟随行星转动
            self.ring.rotation = -Vec3(self.planet.rotation_x - self.ring_rotation_x,
                                       self.planet.rotation_y,
                                       self.planet.rotation_z)

    def appear(self):
        pass

    def disappear(self):
        self.planet.disable()
