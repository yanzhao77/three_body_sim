# -*- coding:utf-8 -*-
# title           :ursina天体视图
# description     :ursina天体视图（天体效果展示用，需要安装 ursina）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina
from ursina import Ursina, window, Entity, camera, color, mouse, Vec2, load_texture, held_keys
from bodies import Body
import random
from simulators.views.body_view import BodyView
import numpy as np
from math import sin, cos, radians
import os


class Planet(Entity):
    def __init__(self, name, texture, pos, scale=2):
        self.angle = random.uniform(0.0005, 0.01)
        self.fastMode = 0
        self.rotation = (random.randint(0, 360) for i in range(3))
        self.rotspeed = random.uniform(0.25, 1.5)
        self.rotMode = random.choice(["x", "y", "z"])
        self.name = name
        # texture = eval(f"{_type}_texture")
        # e = os.path.exists(texture)
        texture = load_texture(texture)
        super().__init__(model="sphere",
                         scale=scale,
                         texture=texture,
                         color=color.white,
                         position=pos)

    def turn(self, angle):
        if self.name != "sun":
            if self.fastMode:
                angle *= 200
            self.x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
            self.y = self.x * sin(radians(angle)) + self.y * cos(radians(angle))
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
        self.entity = Planet(body.name, self.texture, tuple(self.position/1e4), body.size_scale)

    def update(self):
        self.entity.turn(10)

    def appear(self):
        pass

    def disappear(self):
        pass
