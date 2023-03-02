# -*- coding:utf-8 -*-
# title           :ursina天体视图
# description     :ursina天体视图（天体效果展示用，需要安装 ursina）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina
from ursina import Ursina, window, Entity, SmoothFollow, camera, color, mouse, Vec2, Vec3, load_texture, held_keys
from math import sin, cos, radians
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
import random as rd
import os
from bodies import Body
import random
from simulators.views.body_view import BodyView
import numpy as np
from math import sin, cos, radians
import os

SCALE_FACTOR = 1e-7


class UrsinaPlayer(FirstPersonController):
    def __init__(self, position, targets=None):
        # global planets
        super().__init__()
        # pos = planets[0].position
        camera.fov = 100
        if targets is not None:
            # planets = []
            # targets = [view.planet.parent for view in targets]
            targets_parent = Entity()
            for view in targets:
                view.planet.parent = targets_parent
                # planets.append(view.planet)

            camera.add_script(SmoothFollow(targets_parent, offset=(0, 8, -20)))
        pos = np.array(position) * SCALE_FACTOR
        self.position = Vec3(pos[0], pos[1], pos[2])
        # 将摄像机位置设置为 x=0、y=1、z=0 的位置
        # camera.position = Vec3(pos[0], pos[1], pos[2])
        self.position = Vec3(pos[0], pos[1], pos[2])
        # 将摄像机的观察角度绕 x 轴旋转 45 度，绕 y 轴旋转 0 度，绕 z 轴旋转 0 度
        camera.rotation = Vec3(45, 90, 0)

        self.gravity = 0
        self.vspeed = 4000
        self.speed = 10000
        self.mouse_sensitivity = Vec2(160, 160)
        self.on_enable()

    def input(self, key):
        if key == "escape":
            if mouse.locked:
                self.on_disable()
            else:
                sys.exit()

    def _update(self):
        # {'left mouse': 0, 'left': 0, 'left shift': 0, 'space': 1, 'w': 0, 's': 0, 'd': 0, 'a': 0, 'shift': 0})
        if held_keys["left mouse"]:
            self.on_enable()
        if held_keys["left shift"]:
            self.y -= self.vspeed
        if held_keys["space"]:
            self.y += self.vspeed


class Planet(Entity):
    def __init__(self, body_view: BodyView):
        self.body_view = body_view
        self.angle = random.uniform(0.0005, 0.01)
        self.fastMode = 0
        self.rotation = (random.randint(0, 360) for i in range(3))
        self.rotspeed = random.uniform(0.25, 1.5)
        self.rotMode = 'x'  # random.choice(["x", "y", "z"])
        self.name = body_view.name

        pos = body_view.position * SCALE_FACTOR
        scale = body_view.body.diameter * body_view.body.size_scale * SCALE_FACTOR

        # texture = eval(f"{_type}_texture")
        # e = os.path.exists(texture)
        texture = load_texture(body_view.texture)
        super().__init__(model="sphere",
                         scale=scale,
                         texture=texture,
                         color=color.white,
                         position=pos)

    def turn(self, angle):
        # if self.name != "sun":
        #     if self.fastMode:
        #         angle *= 200
        # self.x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
        # self.y = self.x * sin(radians(angle)) + self.y * cos(radians(angle))
        pos = self.body_view.position * SCALE_FACTOR
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]
        exec(f"self.rotation_{self.rotMode}+=self.rotspeed")

    #
    def input(self, key):
        if key == "enter":
            self.fastMode = 1 - self.fastMode


class UrsinaView(BodyView):
    """
    ursina天体视图（天体效果展示用）
    """

    def __init__(self, body: Body):
        BodyView.__init__(self, body)
        self.planet = Planet(self)

    def update(self):
        self.planet.turn(self.planet.angle)

    def appear(self):
        pass

    def disappear(self):
        self.planet.disable()
