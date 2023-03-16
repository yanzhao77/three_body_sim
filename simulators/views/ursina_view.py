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
    load_texture, held_keys, destroy

from ursina.prefabs.first_person_controller import FirstPersonController
import sys
from bodies import Body

from simulators.ursina.ursina_config import UrsinaConfig
from common.color_utils import adjust_brightness, conv_to_vec4_color
from simulators.views.body_view import BodyView
from simulators.views.ursina_mesh import create_sphere, create_torus
import numpy as np
import math


class UrsinaPlayer(FirstPersonController):
    """

    """
    body_rotation_speed_control = 1.0

    def __init__(self, position, targets=None):
        super().__init__()
        # camera.fov = 2000 # 100
        # camera.rotation_y = 90
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
        pos = np.array(position) * UrsinaConfig.SCALE_FACTOR
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

        pos = body_view.position * body_view.body.distance_scale * UrsinaConfig.SCALE_FACTOR
        scale = body_view.body.diameter * body_view.body.size_scale * UrsinaConfig.SCALE_FACTOR

        if hasattr(body_view, "texture"):
            texture = load_texture(body_view.texture)
        else:
            texture = None

        if hasattr(self.body_view.body, "torus_stars"):
            # 创建一个星环小天体群（主要模拟小行星群，非一个天体）
            model = create_torus(0.86, 1.02, 64, 4)
            rotation = (90, 0, 0)
        else:
            # 创建一个天体
            model = create_sphere(0.5, 32)
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

        if hasattr(self.body_view.body, "torus_stars"):
            # 星环小天体群（主要模拟小行星群，非一个天体）
            self.set_light_off()
        else:
            # 一个天体
            # 拖尾球体的初始化
            self.trail_init()

    def trail_init(self):
        """
        拖尾球体的初始化
        :return:
        """
        # 存放拖尾球体
        self.trails = {}
        # 拖尾球体的数量
        self.trail_len = 100

        # 根据天体的颜色获取拖尾的颜色
        trail_color = conv_to_vec4_color(self.body_view.body.color)
        trail_color = adjust_brightness(trail_color, 0.4)
        self.trail_color = color.rgba(trail_color[0], trail_color[1], trail_color[2], 0.6)
        # 拖尾球体的大小为该天体的 1/5
        self.trail_scale = self.scale_x / 5
        if self.trail_scale < 1:
            # 如果太小，则
            pass

    def distance_between_two_points(self, point_a: Vec3, point_b: Vec3) -> float:
        # 计算两点在 x、y、z 三个坐标轴上的差值
        diff_x = point_a.x - point_b.x
        diff_y = point_a.y - point_b.y
        diff_z = point_a.z - point_b.z

        # 计算两点之间的距离
        distance = math.sqrt(diff_x ** 2 + diff_y ** 2 + diff_z ** 2)

        return distance

    def create_trails(self):
        """
        创建拖尾
        :return:
        """
        # 当前天体的位置
        try:
            pos = self.position
        except Exception as e:
            self.destroy_me()
            return
        trails_keys = self.trails.keys()
        # 如果有拖尾
        if len(trails_keys) > 0:
            # 获取最后一个拖尾的位置
            last_key = list(trails_keys)[-1]
            last_pos = self.trails[last_key]
            # 获取拖尾与当前天体的位置
            distance = self.distance_between_two_points(pos, last_pos)
            # 如果位置比较近，就不创建拖尾了，保证拖尾间隔一定的距离
            if distance < self.trail_scale * 1.2:  # 间隔距离不小于1.2倍的拖尾球体
                return

        # 创建拖尾球体，并作为字典的key，存放拖尾球体的位置
        self.trails[self.create_trail(pos)] = pos

        # 计算拖尾球体超过的数量
        trail_overflow_count = len(self.trails) - self.trail_len

        if trail_overflow_count > 0:
            # 如果拖尾球体超过的数量，就删除之前的拖尾球体
            for entity, pos in self.trails.items():
                destroy(entity)
                trail_overflow_count -= 1
                if trail_overflow_count <= 0:
                    break

    def create_trail(self, pos):
        """
        在天体当前的位置创建一个拖尾球体
        :param pos:
        :return:
        """
        trail = Entity(model="sphere", color=self.trail_color, scale=self.trail_scale, position=pos)
        trail.set_light_off()
        return trail

    def turn(self):
        pos = self.body_view.position * UrsinaConfig.SCALE_FACTOR

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
            self.rotspeed = self.rotation_speed * (dt / 3600) / 2.4 * \
                            UrsinaConfig.ROTATION_SPEED_FACTOR * UrsinaConfig.body_spin_factor
            # rotation_speed 度/小时  dt 秒 = (dt / 3600)小时

        # if self.rotation_y < 0:
        #     self.rotation_y += 360
        try:
            # 天体旋转
            self.rotation_y -= self.rotspeed
        except Exception as e:
            self.destroy_me()
            return

        # 如果有行星环
        if hasattr(self, "ring"):
            # 如果有行星环，则不让行星环跟随行星转动
            self.ring.rotation = -Vec3(self.rotation_x - self.ring_rotation_x,
                                       self.rotation_y,
                                       self.rotation_z)

        # 有时候第一个位置不正确，所以判断一下有历史记录后在创建
        if len(self.body_view.body.his_position()) > 1:
            self.create_trails()

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
        self.ring = Entity(parent=self, model=torus, texture='../textures/saturnRings.jpg', scale=1,
                           rotation=(self.ring_rotation_x, 0, 0), double_sided=True)

        # 设置行星环不受灯光影响，否则看不清行星环
        self.ring.set_light_off()

    def destroy_me(self):
        for entity, pos in self.trails.items():
            destroy(entity)
        if hasattr(self, "ring"):
            destroy(self.ring)
        destroy(self)


class UrsinaView(BodyView):
    """
    ursina天体视图（天体效果展示用）
    """

    def __init__(self, body: Body):
        BodyView.__init__(self, body)
        self.velocity = body.velocity

        self.planet = Planet(self)
        if body.has_rings:
            # 创建行星环（目前只有土星环）
            self.planet.create_rings()

    def update(self):
        """

        :return:
        """
        self.planet.turn()


    def appear(self):
        pass

    def disappear(self):
        self.planet.destroy_me()
