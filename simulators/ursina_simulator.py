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

from simulators.views.ursina_view import UrsinaView, UrsinaPlayer

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
import time
import datetime
from ursina import EditorCamera

player = None


class UrsinaSimulator(Simulator):
    def __init__(self, bodies_sys: System):
        self.app = Ursina()
        self.ursina_views = []
        window.color = color.black

        super().__init__(bodies_sys, UrsinaView)

        # ps = ["sun", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
        # cp = [200, 15, 35, 42, 20, 160, 145, 90, 80]
        # x, y, z = 0, 0, 0
        for i, view in enumerate(self.body_views):
            # pos = tuple(body.position)
            # ursina_view = UrsinaView(body)
            view.update()
            self.ursina_views.append(view)
            # planets.append(newPlanet)
            # x += cp[i] * 10

    def check_elapsed_time(self):
        """检查时间间隔是否已过"""
        now = datetime.datetime.now()
        elapsed_time = now - self.last_time
        return elapsed_time >= self.interval

    def check_and_evolve(self):
        if self.check_elapsed_time():
            super().evolve(self.evolve_dt)

    def run(self, dt, **kwargs):
        self.evolve_dt = dt
        # 设定时间间隔为1秒
        self.interval = datetime.timedelta(seconds=1)
        self.last_time = datetime.datetime.now()
        # EditorCamera()
        self.app.run()


if __name__ == '__main__':
    from bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon
    from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY

    """
    3个太阳、1个地球
    """
    bodies = [
        Sun(name='太阳1', mass=1.5e30, init_position=[849597870.700, 0, 0], init_velocity=[0, 7.0, 0],
            size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
        Sun(name='太阳2', mass=2e30, init_position=[0, 0, 0], init_velocity=[0, -8.0, 0],
            size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
        Sun(name='太阳3', mass=2.5e30, init_position=[0, -849597870.700, 0], init_velocity=[18.0, 0, 0],
            size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
        Earth(name='地球', init_position=[0, -349597870.700, 0], init_velocity=[15.50, 0, 0],
              size_scale=4e3, texture="earth.png", distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    ]
    # bodies = [
    #
    #     Sun(name='太阳2', mass=1.5e30, init_position=[0, 0, 0], init_velocity=[0, -8.0, 0],
    #         size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
    #     Sun(name='太阳2', mass=1.5e30, init_position=[849597870.700, 0, 0], init_velocity=[0, -8.0, 0],
    #         size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
    #     Sun(name='太阳2', mass=1.5e30, init_position=[0, -849597870.700, 0], init_velocity=[0, -8.0, 0],
    #         size_scale=5e1, texture="sun.png"),  # 太阳放大 100 倍
    #     Earth(name='地球', mass=5.97237e24, init_position=[0, -349597870.700, 0], init_velocity=[15.50, 0, 0],
    #           size_scale=4e3, texture="earth.png", distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    # ]
    bodies = [
        # Sun(size_scale=0.8e2),                            # 太阳放大 80 倍
        # Mercury(size_scale=4e3, distance_scale=1.3),      # 水星放大 4000 倍，距离放大 1.3 倍
        # Venus(size_scale=4e3, distance_scale=1.3),        # 金星放大 4000 倍，距离放大 1.3 倍
        # Earth(size_scale=4e3, distance_scale=1.3),        # 地球放大 4000 倍，距离放大 1.3 倍
        # Mars(size_scale=4e3, distance_scale=1.3),         # 火星放大 4000 倍，距离放大 1.3 倍
        # Jupiter(size_scale=0.68e3, distance_scale=0.65),  # 木星放大 680 倍，距离缩小到真实距离的 0.65
        Saturn(size_scale=0.68e3, init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],distance_scale=0.52),   # 土星放大 680 倍，距离缩小到真实距离的 0.52
        # Uranus(size_scale=0.8e3, distance_scale=0.36),    # 天王星放大 800 倍，距离缩小到真实距离的 0.36
        # Neptune(size_scale=1e3, distance_scale=0.27),     # 海王星放大 1000 倍，距离缩小到真实距离的 0.27
        # Pluto(size_scale=10e3, distance_scale=0.23),      # 冥王星放大 10000 倍，距离缩小到真实距离的 0.23(从太阳系的行星中排除)
    ]
    body_sys = System(bodies)
    simulator = UrsinaSimulator(body_sys)

    player = UrsinaPlayer((8495000, 8495000, 84950000),simulator.ursina_views)
    # player = UrsinaPlayer((0, 0, 0), simulator.ursina_views)

    def update():
        # print('OK')
        for ursina_view in simulator.ursina_views:
            simulator.check_and_evolve()
            ursina_view.update()
            # ursina_view.entity.turn(ursina_view.entity.angle)
        player._update()


    simulator.run(SECONDS_PER_DAY)
