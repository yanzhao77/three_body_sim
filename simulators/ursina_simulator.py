# -*- coding:utf-8 -*-
# title           :ursina天体运行模拟器
# description     :ursina天体运行模拟器
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina
from ursina import Ursina, window, Entity, camera, color, mouse, Vec2, Vec3, load_texture, held_keys
from math import sin, cos, radians
from ursina.prefabs.first_person_controller import FirstPersonController
import sys
import random as rd
import os

from simulators.views.ursina_view import UrsinaView


class Player(FirstPersonController):
    def __init__(self, planets):
        # global planets

        super().__init__()
        pos = planets[0].position
        camera.fov = 100
        self.position = Vec3(pos[0], pos[1], pos[2])
        self.gravity = 0
        self.vspeed = 40
        self.speed = 100
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

# # -------------------------------------------------------------------------------
# app = Ursina()
# # window.fullscreen = True
# window.color = color.black
#
# planets = []
#
#
# class Planet(Entity):
#     def __init__(self, _type, pos, texture, scale=2):
#         self.angle = rd.uniform(0.0005, 0.01)
#         self.fastMode = 0
#         self.rotation = (rd.randint(0, 360) for i in range(3))
#         self.rotspeed = rd.uniform(0.25, 1.5)
#         self.rotMode = rd.choice(["x", "y", "z"])
#         self._type = _type
#         # texture = eval(f"{_type}_texture")
#         texture = load_texture(texture)
#         super().__init__(model="sphere",
#                          scale=scale,
#                          texture=texture,
#                          color=color.white,
#                          position=pos)
#
#     def turn(self, angle):
#         # if self._type != "sun":
#         #     if self.fastMode:
#         #         angle *= 200
#         # self.x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
#         # self.y = self.x * sin(radians(angle)) + self.y * cos(radians(angle))
#         exec(f"self.rotation_{self.rotMode}+=self.rotspeed")
#     #
#     def input(self, key):
#         if key == "enter":
#             self.fastMode = 1 - self.fastMode
#
#
#
#
#
# def update():
#     global planets, player
#     for planet in planets:
#         planet.turn(planet.angle)
#     player._update()
#
# # os.chdir("../")
#
#
# # sun_texture = load_texture(texture_root + "sun.png")
# # mercury_texture = load_texture(texture_root + "mercury.png")
# # venus_texture = load_texture(texture_root + "venus.png")
# # earth_texture = load_texture(texture_root + "earth.png")
# # mars_texture = load_texture(texture_root + "mars.png")
# # jupiter_texture = load_texture(texture_root + "jupiter.png")
# # saturn_texture = load_texture(texture_root + "saturn.png")
# # uranus_texture = load_texture(texture_root + "uranus.png")
# # neptune_texture = load_texture(texture_root + "neptune.png")
#
# texture_root = "../textures/"
# ps = ["sun", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
# cp = [200, 15, 35, 42, 20, 160, 145, 90, 80]  # 大小缩放
# x, y, z = 0, 0, 0
# for i, p in enumerate(ps):
#     # _type, pos, texture, scale=2
#     newPlanet = Planet(p, (x, y, z),texture_root+f"{p}.png", cp[i])
#     planets.append(newPlanet)
#     x += cp[i] * 10
#
# player = Player(planets)
#
# if __name__ == '__main__':
#     # os.chdir("../")
#     # sun_texture = os.path.join(texture_root, "sun.png")
#     # print(os.path.exists(sun_texture))
#     app.run()
#
# # ---------------------------------------------------------------------------


from simulators.simulator import Simulator
from common.system import System

ursina_views = []
player = None


class UrsinaSimulator(Simulator):
    def __init__(self, bodies_sys: System):
        self.app = Ursina()
        window.color = color.black

        super().__init__(bodies_sys, UrsinaView)

        # ps = ["sun", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
        # cp = [200, 15, 35, 42, 20, 160, 145, 90, 80]
        # x, y, z = 0, 0, 0
        for i, view in enumerate(self.body_views):
            # pos = tuple(body.position)
            # ursina_view = UrsinaView(body)
            view.update()
            ursina_views.append(view)
            # planets.append(newPlanet)
            # x += cp[i] * 10

    def run(self, dt, **kwargs):
        self.app.run()


if __name__ == '__main__':
    from bodies import Sun, Earth
    from common.consts import SECONDS_PER_WEEK

    """
    3个太阳、1个地球
    """
    # bodies = [
    #     Sun(name='太阳1', mass=1.5e30, init_position=[849597870.700, 0, 0], init_velocity=[0, 7.0, 0],
    #         size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
    #     Sun(name='太阳2', mass=2e30, init_position=[0, 0, 0], init_velocity=[0, -8.0, 0],
    #         size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
    #     Sun(name='太阳3', mass=2.5e30, init_position=[0, -849597870.700, 0], init_velocity=[18.0, 0, 0],
    #         size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
    #     Earth(name='地球', init_position=[0, -349597870.700, 0], init_velocity=[15.50, 0, 0],
    #           size_scale=4e3, texture="earth.png", distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    # ]
    bodies = [

        Sun(name='太阳2', mass=1.5e30, init_position=[0, 0, 0], init_velocity=[0, -8.0, 0],
            size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
        Sun(name='太阳2', mass=1.5e30, init_position=[849597870.700, 0, 0], init_velocity=[0, -8.0, 0],
            size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
        Sun(name='太阳2', mass=1.5e30, init_position=[0, -849597870.700, 0], init_velocity=[0, -8.0, 0],
            size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
        Earth(name='地球',mass=5.97237e24, init_position=[0, -349597870.700, 0], init_velocity=[15.50, 0, 0],
              size_scale=4e3, texture="earth.png", distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    ]
    body_sys = System(bodies)
    simulator = UrsinaSimulator(body_sys)

    player = Player(ursina_views)


    def update():
        # print('OK')
        global ursina_views, player
        for ursina_view in ursina_views:
            ursina_view.update()
            # ursina_view.entity.turn(ursina_view.entity.angle)
        player._update()


    simulator.run(SECONDS_PER_WEEK)
