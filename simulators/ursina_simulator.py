# -*- coding:utf-8 -*-
# title           :ursina天体运行模拟器
# description     :ursina天体运行模拟器
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina
from ursina import Ursina, window, Entity, Grid, Mesh, camera, Text, application, color, mouse, Vec2, Vec3, \
    load_texture, held_keys
from ursina.prefabs.first_person_controller import FirstPersonController

from simulators.views.ursina_view import UrsinaView, UrsinaPlayer

from simulators.simulator import Simulator
from common.system import System
import time
import datetime
import math
from ursina import EditorCamera, PointLight, SpotLight, AmbientLight
from scenes.func import ursina_run


class WorldGrid(Entity):  # Entity # 定义构造方法
    def __init__(self):
        super().__init__()
        s = 100
        grid = Entity(model=Grid(s, s), scale=s * 20, color=color.rgba(255, 255, 255, 20), rotation_x=90,
                      position=(0, -80, 0))
        # 坐标轴
        # vertsx = ((0, 0, 0), (10, 0, 0))
        # Entity(model=Mesh(vertices=vertsx, mode='line', thickness=3), color=color.cyan).set_light_off()
        # vertsyz = [(0, 0, 0), (0, 10, 0), (0, 0, 0), (0, 0, 10)]
        # Entity(model=Mesh(vertices=vertsyz, mode='line', thickness=3), color=color.yellow).set_light_off()
        grid.set_light_off()


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
        value = elapsed_time >= self.interval
        if value:
            self.last_time = now
        return value

    def check_and_evolve(self):
        if self.check_elapsed_time():
            super().evolve(self.evolve_dt)

    def cosmic_background(self, texture='../textures/cosmic2.jpg'):
        """
        加入宇宙背景
        :param texture:
        :return:
        """
        # Add skybox
        from ursina import Sky
        Sky(texture=texture).scale = 10000

        # texture = load_texture(texture)
        # sky_dome = Entity(model='sky_dome', texture=texture, scale=10000,
        #                   color=color.white,
        #                   position=(0, 0, 0),
        #                   rotation=(0, 0, 0))

    def __add_glow(self, entity, intensity=2, light_color=color.white, attenuation=3):
        """
        未用，保留代码
        :param entity:
        :param intensity:
        :param light_color:
        :param attenuation:
        :return:
        """
        lights = []
        import math
        for i in range(5):
            glow_entity = Entity(parent=entity, model='sphere', color=color.rgba(1.0, 0.6, 0.2, 1),
                                 scale=math.pow(1.03, i), alpha=0.2)
            lights.append(glow_entity)
        # 创建一个新的 Entity 对象，作为光晕的容器
        # glow_entity = Entity(parent=entity, model='sphere', scale=entity.scale * 1.2)
        # 创建 PointLight 对象，并设置它的属性
        light = PointLight(parent=lights[0], intensity=intensity, color=light_color, attenuation=attenuation)
        lights.append(light)

        # 把 Entity 对象放到星星的后面，使得光晕看起来像是从星星发出来的
        glow_entity.world_position = entity.world_position
        glow_entity.world_parent = entity.parent
        glow_entity.y += entity.scale_y * 0.1
        glow_entity.depth_test = False
        return lights

    def create_fixed_star_lights(self, entity):
        """
        创建恒星的发光的效果、并作为灯光源
        :param entity:
        :return:
        """

        # 如果是恒星（如：太阳），自身会发光，则需要关闭灯光
        entity.set_light_off()

        # if hasattr(self, "sun"):
        #     return
        # self.sun = "sun"
        lights = []
        # 创建多个新的 Entity 对象，作为光晕的容器
        for i in range(10):
            # glow_entity = Entity(parent=entity, model='sphere', color=color.rgba(1.0, 0.6, 0.2, 1),
            #                      scale=math.pow(1.03, i), alpha=0.2)
            glow_entity = Entity(parent=entity, model='sphere', color=color.rgba(1.0, 0.6, 0.2, 1),
                                 scale=math.pow(1.03, i), alpha=0.1)

            lights.append(glow_entity)
        # 创建 PointLight 对象，作为恒星的灯光源
        light = PointLight(parent=entity, intensity=10, range=10, color=color.white)
        lights.append(light)
        return lights

    def run(self, dt, **kwargs):
        from ursina import EditorCamera, PointLight, SpotLight, AmbientLight, DirectionalLight
        # 设定时间间隔为0.01秒
        interval = 0.01
        self.evolve_dt = dt * interval
        self.interval = datetime.timedelta(seconds=interval)

        self.last_time = datetime.datetime.now() - datetime.timedelta(seconds=2)
        if "light" in kwargs:
            if kwargs["light"]:
                for v in self.ursina_views:
                    if v.body.is_fixed_star:
                        self.lights = self.create_fixed_star_lights(v.planet)

        if "show_grid" in kwargs:
            if kwargs["show_grid"]:
                WorldGrid()

        if "cosmic_bg" in kwargs:
            cosmic_bg = kwargs["cosmic_bg"]
            if cosmic_bg is None:
                # cosmic_bg = '../textures/cosmic1.png'
                # cosmic_bg = '../textures/cosmic2.jpg'
                cosmic_bg = '../textures/cosmic3.jpg'
            import os
            if cosmic_bg is not None and os.path.exists(cosmic_bg):
                self.cosmic_background(cosmic_bg)

        EditorCamera()

        pause_handler = Entity(ignore_paused=True)
        # 加载中文字体文件
        Text.default_font = 'simsun.ttc'
        # text_time_scale = "1"
        text_time_scale_info = None

        def show_text_time_scale_info():
            nonlocal text_time_scale_info
            if text_time_scale_info is not None:
                text_time_scale_info.disable()
            text_time_scale = "控制倍率:" + str(application.time_scale).ljust(4, " ")
            text_time_scale_info = Text(text=text_time_scale, position=(-0.8, 0.5), origin=(-1, 1), background=True)

        # 按空格键则暂停
        def pause_handler_input(key):
            nonlocal text_time_scale_info
            time_scales = [0.05, 0.1, 0.2, 0.5, 1, 5, 10, 20, 30]
            print(key)
            if key == 'space':
                application.paused = not application.paused  # Pause/unpause the game.
            elif key == 'tab':
                # application.time_scale 属性控制游戏时间流逝的速度。
                # 具体来说，它是一个浮点数，用于调整游戏时间流逝速度的比例，其默认值为 1.0，表示正常速度。
                # 当你将它设置为小于 1.0 的值时，游戏时间会变慢，而设置为大于 1.0 的值时，游戏时间则会变快。
                for idx, time_scale in enumerate(time_scales):
                    if float(application.time_scale) == time_scale:
                        if idx < len(time_scales) - 1:
                            application.time_scale = time_scales[idx + 1]
                            break
                        else:
                            application.time_scale = time_scales[0]
            elif key == '+' or key == "= up":
                if application.time_scale in time_scales:
                    idx = time_scales.index(application.time_scale)
                    if idx < len(time_scales) - 1:
                        application.time_scale = time_scales[idx + 1]
            elif key == '-' or key == "- up":
                if application.time_scale in time_scales:
                    idx = time_scales.index(application.time_scale)
                    if idx > 0:
                        application.time_scale = time_scales[idx - 1]

            show_text_time_scale_info()

        pause_handler.input = pause_handler_input
        show_text_time_scale_info()
        key_info_str = "退出[按2次ESC] 方位控制[鼠标QWEASD] 开始暂停[空格] 控制倍率[Tab - +]"
        key_info = Text(text=key_info_str, position=(-0.8, 0.5), origin=(-1, 1), background=True)
        self.app.run()


if __name__ == '__main__':
    from bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon
    from bodies.body import AU
    from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY, SECONDS_PER_HALF_DAY

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
        Sun(size_scale=0.8e2),  # 太阳放大 80 倍
        Mercury(size_scale=4e3, distance_scale=1.3),  # 水星放大 4000 倍，距离放大 1.3 倍
        Venus(size_scale=4e3, distance_scale=1.3),  # 金星放大 4000 倍，距离放大 1.3 倍
        Earth(init_position=[1.12 * AU, 0, 0],
              init_velocity=[0, 29.79, 0], size_scale=4e3, distance_scale=1.3),  # 地球放大 4000 倍，距离放大 1.3 倍
        Moon(init_position=[363104 + 1.12 * AU, 0, 0],
             init_velocity=[-9, 29.79 + 1.023, 0], size_scale=4e3, distance_scale=1.3),
        Mars(size_scale=4e3, distance_scale=1.3),  # 火星放大 4000 倍，距离放大 1.3 倍
        Jupiter(size_scale=0.68e3, distance_scale=0.65),  # 木星放大 680 倍，距离缩小到真实距离的 0.65
        Saturn(size_scale=0.68e3, distance_scale=0.52),  # 土星放大 680 倍，距离缩小到真实距离的 0.52
        Uranus(size_scale=0.8e3, distance_scale=0.36),  # 天王星放大 800 倍，距离缩小到真实距离的 0.36
        Neptune(size_scale=1e3, distance_scale=0.27),  # 海王星放大 1000 倍，距离缩小到真实距离的 0.27
        Pluto(size_scale=10e3, distance_scale=0.23),  # 冥王星放大 10000 倍，距离缩小到真实距离的 0.23(从太阳系的行星中排除)
    ]

    ursina_run(bodies, SECONDS_PER_DAY, position=(AU * 2, AU * 2, AU * 3), show_grid=True)
