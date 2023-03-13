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

SCALE_FACTOR = 5e-7
# 旋转因子为1，则为正常的转速
ROTATION_SPEED_FACTOR = 1.0
ROTATION_SPEED_FACTOR = 0.01


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


from math import pi, sin, cos


# def create_sphere(radius, subdivisions):
#     # 生成球体的顶点、UV坐标、法线和三角面
#     # radius = 1
#     # subdivisions = 16
#     theta = np.linspace(0, 2 * np.pi, subdivisions + 1)
#     phi = np.linspace(0, np.pi, subdivisions + 1)
#     u = np.linspace(0, 1, subdivisions + 1)
#     v = np.linspace(0, 1, subdivisions + 1)
#     verts = []
#     uvs = []
#     normals = []
#     for i in range(len(theta)):
#         for j in range(len(phi)):
#             x = radius * np.sin(phi[j]) * np.cos(theta[i])
#             y = radius * np.sin(phi[j]) * np.sin(theta[i])
#             z = radius * np.cos(phi[j])
#             verts.append((x, y, z))
#             uvs.append((u[i], v[j]))
#             normals.append((x / radius, y / radius, z / radius))
#
#     tris = []
#     for i in range(len(theta)):
#         for j in range(len(phi)):
#             a = i * (subdivisions + 1) + j
#             b = (i + 1) * (subdivisions + 1) + j
#             tris.append((a, b, a + 1))
#             tris.append((a + 1, b, b + 1))
#
#     # # 反转面法线
#     # for i in range(len(tris)):
#     #     a, b, c = tris[i]
#     #     tris[i] = (c, b, a)
#     #     normals[a], normals[b], normals[c] = -Vec3(*normals[a]), -Vec3(*normals[b]), -Vec3(*normals[c])
#     #     normals[a], normals[b], normals[c] = -Vec3(*normals[a]), -Vec3(*normals[b]), -Vec3(*normals[c])
#
#     # 创建球体 Mesh 对象并设置材质
#     sphere_mesh = Mesh(vertices=verts, uvs=uvs, normals=normals, triangles=tris, mode='triangle')
#     return sphere_mesh

def create_sphere(radius, subdivisions):
    verts = []
    tris = []
    normals = []
    uvs = []

    for y in range(subdivisions + 1):
        for x in range(subdivisions + 1):
            x_segment = x / subdivisions
            y_segment = y / subdivisions
            x_pos = cos(x_segment * 2 * pi) * sin(y_segment * pi)
            y_pos = cos(y_segment * pi)
            z_pos = sin(x_segment * 2 * pi) * sin(y_segment * pi)

            verts.append(Vec3(x_pos, y_pos, z_pos) * radius)
            uvs.append(Vec2(x_segment, y_segment))
            normals.append(Vec3(x_pos, y_pos, z_pos))

    for y in range(subdivisions):
        for x in range(subdivisions):
            first = (y * (subdivisions + 1)) + x
            second = first + subdivisions + 1
            tris.append((first, second + 1, second))
            tris.append((first, first + 1, second + 1))

    # 反转面法线
    for i in range(len(tris)):
        a, b, c = tris[i]
        tris[i] = (c, b, a)
        # normals[a], normals[b], normals[c] = -Vec3(*normals[a]), -Vec3(*normals[b]), -Vec3(*normals[c])

    return Mesh(vertices=verts, triangles=tris, normals=normals, uvs=uvs, mode='triangle')


class Planet(Entity):
    def __init__(self, body_view: BodyView):
        self.body_view = body_view
        self.rotation_speed = self.body_view.body.rotation_speed
        self.rotMode = 'x'  # random.choice(["x", "y", "z"])
        self.name = body_view.name

        pos = body_view.position * body_view.body.distance_scale * SCALE_FACTOR
        scale = body_view.body.diameter * body_view.body.size_scale * SCALE_FACTOR

        subdivisions = 32 # int(scale*20)

        if hasattr(body_view, "texture"):
            texture = load_texture(body_view.texture)
        else:
            texture = None

        super().__init__(
            # model="sphere",
            model=create_sphere(0.5, subdivisions),
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

    def create_rings(self):
        """
        创建行星环（使用土星贴图）
        :return:
        """
        # 行星环偏移角度
        self.ring_rotation_x = 75
        # 创建行星环
        self.ring = Entity(parent=self.planet, model="circle", texture='../textures/saturnRings.jpg', scale=2,
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
