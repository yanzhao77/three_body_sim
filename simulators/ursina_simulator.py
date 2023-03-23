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
    load_texture, held_keys, distance, Audio
from ursina.prefabs.first_person_controller import FirstPersonController
import itertools
from simulators.ursina.ursina_event import UrsinaEvent
# from simulators.ursina.ursina_ui import UrsinaUI
from simulators.ursina.ui.control_ui import ControlUI
from simulators.ursina.ui.control_handler import ControlHandler

from simulators.views.ursina_view import UrsinaView, UrsinaPlayer
from simulators.ursina.ursina_config import UrsinaConfig
from simulators.simulator import Simulator
from common.system import System
import time
import datetime
import math
import os
from ursina import EditorCamera, PointLight, SpotLight, AmbientLight, DirectionalLight
from scenes.func import ursina_run


class WorldGrid(Entity):
    """
    创建一个宇宙网格对象
    """

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
    """
    Ursina官网： https://www.ursinaengine.org/
    """

    def __init__(self, bodies_sys: System):
        self.app = Ursina()
        # import os
        # os.environ['CUDA_VISIBLE_DEVICES'] = '1'  # 选择第二个GPU
        # self.app = Ursina(window_title='GPU模拟',
        #              window_kwargs={'vsync': True, 'fullscreen': False, 'borderless': False, 'show_ursina_splash': True,
        #                             'high_resolution': True})
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
        self.adjust_system_motion_params()
        UrsinaEvent.on_searching_bodies_subscription(type(self).__name__, self.on_searching_bodies)

    # def get_bodies_max_distance(self, body_views):
    #     max_distance = 0
    #     for b1 in body_views:
    #         if b1.body.ignore_mass:
    #             continue
    #         for b2 in body_views:
    #             if (b1 is b2) or b2.body.ignore_mass:
    #                 continue
    #         d = distance(b1.planet, b2.planet)
    #         if d > max_distance:
    #             max_distance = d
    #     return max_distance

    def get_bodies_max_distance(self, body_views):
        """
        算法优化
        :param body_views:
        :return:
        """
        max_distance = 0
        for b1, b2 in itertools.combinations(body_views, 2):
            if b1.body.ignore_mass or b2.body.ignore_mass:
                continue
            d = distance(b1.planet, b2.planet)
            if d > max_distance:
                max_distance = d
        if max_distance == 0:
            if len(body_views) > 0:
                # 如果最大距离等于0，说明只有一个有效的天体，则以第一个天体的半径为基准
                max_distance = pow(body_views[0].planet.scale_x, 3)
        return max_distance

    def adjust_system_motion_params(self):
        """
        调整天体系统运行的参数
        :return:
        """
        max_distance = self.get_bodies_max_distance(self.body_views)
        # 根据天体之间的距离，调整 application.time_scale（控制摄像头运动的速度）
        time_scale = round(pow(max_distance, 1 / 4), 2)
        if time_scale < 0.01:
            time_scale = 0.01

        application.time_scale = time_scale
        # UrsinaConfig.auto_scale_factor = 1.0e-9

    def on_searching_bodies(self, **kwargs):
        views = []
        for view in self.body_views:
            # if view.appeared:
            views.append(view)
        return views

    def check_interval_expired(self):
        """
        检查时间间隔是否已过期
        :return:
        """
        now = datetime.datetime.now()
        elapsed_time = now - self.last_time
        is_expired = elapsed_time >= self.interval
        if is_expired:
            self.last_time = now
        return is_expired

    def check_and_evolve(self):
        if self.check_interval_expired():
            # 获取配置中的运行速度的因子
            run_speed_factor = float(UrsinaConfig.run_speed_factor)
            if UrsinaConfig.seconds_per <= 0:
                # 配置中，如果为0秒，表示默认开始运行设置的秒数（evolve_dt）
                evolve_dt = self.evolve_dt * run_speed_factor
            else:
                # 配置中，每年、月、天等等有多少秒
                evolve_dt = UrsinaConfig.seconds_per * run_speed_factor
            # interval_fator 能让更新天体运行状态（位置、速度）更精确
            evolve_dt = evolve_dt * self.interval_fator
            super().evolve(evolve_dt)

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

    # def __add_glow(self, entity, intensity=2, light_color=color.white, attenuation=3):
    #     """
    #     未用，保留代码
    #     :param entity:
    #     :param intensity:
    #     :param light_color:
    #     :param attenuation:
    #     :return:
    #     """
    #     lights = []
    #     import math
    #     for i in range(5):
    #         glow_entity = Entity(parent=entity, model='sphere', color=color.rgba(1.0, 0.6, 0.2, 1),
    #                              scale=math.pow(1.03, i), alpha=0.2)
    #         lights.append(glow_entity)
    #     # 创建一个新的 Entity 对象，作为光晕的容器
    #     # glow_entity = Entity(parent=entity, model='sphere', scale=entity.scale * 1.2)
    #     # 创建 PointLight 对象，并设置它的属性
    #     for i in range(2):
    #         light = PointLight(parent=lights[0], intensity=intensity, color=light_color, attenuation=attenuation)
    #         lights.append(light)
    #
    #     # 把 Entity 对象放到星星的后面，使得光晕看起来像是从星星发出来的
    #     glow_entity.world_position = entity.world_position
    #     glow_entity.world_parent = entity.parent
    #     glow_entity.y += entity.scale_y * 0.1
    #     glow_entity.depth_test = False
    #     return lights

    # def create_fixed_star_lights(self, entity):
    #     """
    #     创建恒星的发光的效果、并作为灯光源
    #     :param entity:
    #     :return:
    #     """
    #
    #     # 如果是恒星（如：太阳），自身会发光，则需要关闭灯光
    #     entity.set_light_off()
    #
    #     lights = []
    #     # 创建多个新的 Entity 对象，作为光晕的容器
    #     for i in range(10):
    #         glow_entity = Entity(parent=entity, model='sphere', color=color.rgba(1.0, 0.6, 0.2, 1),
    #                              scale=math.pow(1.03, i), alpha=0.1)
    #
    #         lights.append(glow_entity)
    #     for i in range(2):
    #         # 创建 PointLight 对象，作为恒星的灯光源
    #         light = PointLight(parent=entity, intensity=10, range=10, color=color.white)
    #         lights.append(light)
    #
    #     # light = DirectionalLight(shadows=True, direction=Vec3(0, 0, 1), color=color.white)
    #     # light.look_at(Vec3(0, 0, -1))
    #     # light = SpotLight(parent=entity,shadows=True, direction=Vec3(1,1,1), color=color.white)
    #
    #     return lights

    def run(self, dt, **kwargs):

        window.title = '宇宙模拟器'

        # 设置 camera 的裁剪面和位置
        # camera.clip_plane_near = 0.01
        # camera.fov = 120
        # camera.clip_plane_far = 1000
        # camera.position = (0, 10, -20)
        # camera.rotation_x = -30

        # interval_fator 能让更新天体运行状态（位置、速度）更精确
        # 设定时间间隔为0.01秒
        self.interval_fator = 0.01
        self.evolve_dt = dt

        # interval 和 last_time 用于检查时间间隔是否已过期
        self.interval = datetime.timedelta(seconds=self.interval_fator)
        self.last_time = datetime.datetime.now() - datetime.timedelta(seconds=2)

        if "light" in kwargs:
            if kwargs["light"]:
                for v in self.ursina_views:
                    if v.body.is_fixed_star:
                        # self.lights = self.create_fixed_star_lights(v.planet)
                        pass

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

        # ui = UrsinaUI()
        ctl = ControlUI(ControlHandler(), position=(0.6, 0.5))

        EditorCamera(ignore_paused=True)
        # 防止打开中文输入法
        # self.switch_to_english_input_method()
        #     file: 指定音乐文件的路径
        #     loop: 是否循环播放，默认为 True
        #     autoplay: 是否自动播放，默认为 True
        #     volume: 音量大小，取值范围为 0.0 到 1.0，默认为 1.0
        #     pitch: 音调，取值范围为 0.5 到 2.0，默认为 1.0
        #     time: 指定音乐从何处开始播放，单位为秒，默认为 0.0
        #     stop_when_done: 音乐播放完毕后是否停止播放，默认为 True
        if "bg_music" in kwargs:
            bg_music = kwargs["bg_music"]
        elif "background_music" in kwargs:
            bg_music = kwargs["background_music"]
        else:
            bg_music = None

        if bg_music is None:
            bg_music = "../sounds/universe_04.mp3"

        if os.path.exists(bg_music):
            audio = Audio(bg_music, pitch=1, loop=True, autoplay=True)
            audio.volume = 0.3

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
