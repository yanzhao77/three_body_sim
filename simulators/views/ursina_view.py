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
from math import sin, cos, radians
import os
import matplotlib.pyplot as plt

SCALE_FACTOR = 1e-7


# 创建 TorusMesh
class TorusMesh(Mesh):
    def __init__(self, radius=1, thickness=.25, radial_segments=16, tubular_segments=32):
        super().__init__()
        self.radius = radius
        self.thickness = thickness
        self.radial_segments = radial_segments
        self.tubular_segments = tubular_segments
        self.vertices = []
        self.triangles = []

        for j in range(radial_segments):
            for i in range(tubular_segments):
                a = i / tubular_segments * math.pi * 2
                b = j / radial_segments * math.pi * 2
                x = (radius + thickness * math.cos(b)) * math.cos(a)
                y = (radius + thickness * math.cos(b)) * math.sin(a)
                z = thickness * math.sin(b)
                u = i / tubular_segments
                v = j / radial_segments
                self.vertices.append((x, y, z))
                self.uvs.append((u, v))

        for j in range(radial_segments):
            for i in range(tubular_segments):
                a = i
                b = j
                c = (i + 1) % tubular_segments
                d = (j + 1) % radial_segments
                self.triangles.append((a + b * tubular_segments, b + d * tubular_segments, c + b * tubular_segments))
                self.triangles.append((c + b * tubular_segments, b + d * tubular_segments, c + d * tubular_segments))


class UrsinaPlayer(FirstPersonController):
    def __init__(self, position, targets=None):
        # global planets
        super().__init__()
        # pos = planets[0].position
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
        self.position = Vec3(pos[0], pos[1], pos[2])
        # 将摄像机的观察角度绕 x 轴旋转 45 度，绕 y 轴旋转 0 度，绕 z 轴旋转 0 度
        camera.rotation = Vec3(45, 90, 0)

        self.gravity = 0
        self.vspeed = 400
        self.speed = 1000
        self.mouse_sensitivity = Vec2(160, 160)
        self.on_enable()
        self.rotation_speed = 80

    # def space_callback(self):
    #     best_camera_position = self.best_camera_position()
    #     if best_camera_position is None:
    #         return
    #     best_pos = np.array(best_camera_position[0]) * SCALE_FACTOR
    #     camera.position, camera.rotation = best_pos, best_camera_position[1]
    #
    # def best_camera_position(self):
    #     if self.planets is None:
    #         return None
    #
    #     min_x, max_x, min_y, max_y, min_z, max_z = None, None, None, None, None, None
    #     for planet in self.planets:
    #         if min_x is None or planet.x < min_x:
    #             min_x = planet.x
    #         if max_x is None or planet.x > max_x:
    #             max_x = planet.x
    #         if min_y is None or planet.y < min_y:
    #             min_y = planet.y
    #         if max_y is None or planet.y > max_y:
    #             max_y = planet.y
    #         if min_z is None or planet.z < min_z:
    #             min_z = planet.z
    #         if max_z is None or planet.z > max_z:
    #             max_z = planet.z
    #     x = (min_x + max_x) / 2
    #     y = (min_y + max_y) / 2
    #     z = (min_z + max_z) / 2
    #     distance = max(max_x - min_x, max_y - min_y, max_z - min_z) * 1.5
    #     return (x, y + distance, z - distance), (0, -90, 0)

    # def camera_adj(self, targets):
    #     # 创建一些物体
    #     # targets = []
    #     # for i in range(10):
    #     #     targets.append(Entity(model='cube', color=color.random_color(), position=(i * 2 - 10, i % 2 * 2 - 1, 0)))
    #
    #     # 计算所有物体的平均位置
    #     avg_pos = sum(np.array([target.position for target in targets]))/ len(targets)
    #
    #     # 创建一个OrthographicCamera，使其位于所有目标的中心位置，并面向下方
    #     # camera = OrthographicCamera()
    #     camera.position = avg_pos + (0, 0, 20)
    #     camera.rotation_x = -90



    def input(self, key):
        if key == "escape":
            if mouse.locked:
                self.on_disable()
            else:
                sys.exit()
        return super().input(key)
        # elif key == "space":
        #     self.space_callback()
        # Input.bind('space', space_callback)

    # def _update(self):
    #     # # {'left mouse': 0, 'left': 0, 'left shift': 0, 'space': 1, 'w': 0, 's': 0, 'd': 0, 'a': 0, 'shift': 0})
    #     # if held_keys["left mouse"]:
    #     #     self.on_enable()
    #     # if held_keys["left shift"]:
    #     #     self.y -= self.vspeed
    #     # if held_keys["space"]:
    #     #     self.y += self.vspeed
    #     # WASD keys
    #
    #     if held_keys['f']:
    #         camera.fov += 1
    #     if held_keys['r']:
    #         camera.fov -= 1
    #     # camera.position
    #     # self.rotation_y += held_keys['d'] * self.rotation_speed * time.dt
    #     # self.rotation_y -= held_keys['a'] * self.rotation_speed * time.dt
    #     # self.rotation_x += held_keys['w'] * self.rotation_speed * time.dt
    #     # self.rotation_x -= held_keys['s'] * self.rotation_speed * time.dt
    #
    #     forward = self.forward * (held_keys['w'] - held_keys['s'])
    #     right = self.right * (held_keys['d'] - held_keys['a'])
    #
    #     self.position += (forward + right) * self.speed * time.dt
    #     # if held_keys['w']:
    #     #     camera.position += camera.forward * time.dt
    #     # if held_keys['s']:
    #     #     camera.position -= camera.forward * time.dt
    #     # if held_keys['a']:
    #     #     camera.position -= camera.right * time.dt
    #     # if held_keys['d']:
    #     #     camera.position += camera.right * time.dt
    #     #
    #     # # Mouse control
    #     # camera.rotation_y += held_keys['right mouse'] * mouse.velocity[0] * 20
    #     # camera.rotation_x -= held_keys['right mouse'] * mouse.velocity[1] * 20
    #     # camera.rotation_x = clamp(camera.rotation_x, -90, 90)


class Planet(Entity):
    def __init__(self, body_view: BodyView):
        self.body_view = body_view
        # self.angle = 0  # random.uniform(0.0005, 0.01)
        # self.fastMode = 0
        # self.rotation = (random.randint(0, 360) for i in range(3))
        self.rotspeed = random.uniform(0.25, 1.5)
        self.rotMode = 'x'  # random.choice(["x", "y", "z"])
        self.name = body_view.name

        pos = body_view.position * body_view.body.distance_scale * SCALE_FACTOR
        scale = body_view.body.diameter * body_view.body.size_scale * SCALE_FACTOR

        # texture = eval(f"{_type}_texture")
        # e = os.path.exists(texture)
        # texture = self.__set_texture(body_view.texture)
        texture = load_texture(body_view.texture)

        # 将贴图旋转90度
        super().__init__(model="sphere",
                         scale=scale,
                         texture=texture,
                         color=color.white,
                         position=pos,
                         rotation=(0, 0, 0))

    # def __set_texture(self, image_file):
    #     """
    #     设置纹理图片到天体
    #     :param image_file:
    #     :return:
    #     """
    #     outfile = image_file.replace('.png', '_rotate.png').replace('.jpg', '_rotate.jpg')
    #     from PIL import Image
    #     # 打开原始图片
    #     image = Image.open(image_file)
    #     # 顺时针旋转90度
    #     rotated_image = image.rotate(90, expand=True)
    #
    #     # 保存旋转后的图片
    #     rotated_image.save(outfile)
    #
    #     return outfile

    def turn(self):
        # if self.name != "sun":
        #     if self.fastMode:
        #         angle *= 200
        # self.x = self.x * cos(radians(angle)) - self.y * sin(radians(angle))
        # self.y = self.x * sin(radians(angle)) + self.y * cos(radians(angle))
        pos = self.body_view.position * SCALE_FACTOR

        self.x = -pos[1]
        self.y = pos[2]
        self.z = pos[0]

        # self.rotation_y -= self.rotspeed

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
        # 将列表元素往后移动一位，最后一位变为第一位
        # a1 = a[1:] + [a[0]]
        # self.velocity = np.concatenate((body.velocity[1:], [body.velocity[0]]))

        # 将列表元素往前移动一位，第一位变为最后一位
        # a2 = [a[-1]] + a[:-1]
        # self.velocity = np.concatenate((np.array([body.velocity[-1]]), body.velocity[0:2]))

        self.planet = Planet(self)
        if body.has_rings:
            self.create_rings()

    def create_rings(self):
        ring = Entity(model='torus', texture='textures/saturnRings.jpg', scale=(4, 4), double_sided=True)

        # ring = Entity(model=TorusMesh(radius=self.body.diameter * 100, thickness=.5), texture='textures/saturnRings.jpg', scale=3)
        ring.world_parent = self.planet
        ring.position = self.planet.position

    def update(self):
        self.planet.turn()

    def appear(self):
        pass

    def disappear(self):
        self.planet.disable()
