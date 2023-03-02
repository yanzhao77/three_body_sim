# -*- coding:utf-8 -*-
# title           :manim天体运行模拟器
# description     :manim天体运行模拟器
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# manim version   :Manim Community v0.17.2
# ==============================================================================
# 环境安装教程参考：
# https://blog.csdn.net/FRIGIDWINTER/article/details/121526956

import os
from manim import *
from manim import *
from manim.mobject.three_d import Sphere
from manim.three_d.light import *
from manim.mobject.opengl import *
from PIL import Image


class TexturedSphere(ThreeDVMobject):
    def __init__(self, radius=1, u_min=0, u_max=1, v_min=0, v_max=1, **kwargs):
        self.radius = radius
        self.u_min = u_min
        self.u_max = u_max
        self.v_min = v_min
        self.v_max = v_max
        super().__init__(**kwargs)

    def init_points(self):
        sphere = Sphere(radius=self.radius).mesh
        for i in range(len(sphere[0])):
            u, v = sphere[0][i], sphere[1][i]
            self.add_point(self.radius * np.array([
                np.cos(u) * np.sin(v),
                np.sin(u) * np.sin(v),
                np.cos(v)
            ]))
            self.add_tex_coords([
                interpolate(self.u_min, self.u_max, u / (2 * np.pi)),
                interpolate(self.v_min, self.v_max, v / np.pi)
            ])
        self.set_color_by_tex()

    def set_color_by_tex(self, texture_file='saturn.jpg'):
        texture_path = f'textures/{texture_file}'
        texture = Image.open(texture_path).transpose(Image.FLIP_TOP_BOTTOM).convert('RGBA')
        self.set_texture(texture)


class TexturedSaturn(Scene):
    def construct(self):
        sphere = TexturedSphere(radius=2.5, texture_file='saturn.jpg')
        rings = TexturedSphere(radius=3.5, texture_file='saturnRings.jpg', u_min=0.2, u_max=0.8, v_min=0.2, v_max=0.8)
        rings.set_rotation(right=PI / 2)
        rings.set_shade_in_3d(True)
        rings.set_opacity(0.8)

        light = ThreeDPointLight(
            location=5 * OUT + 5 * RIGHT + 5 * UP,
            color=WHITE,
        )
        ambient = ThreeDAmbientLight(color="#444444")
        self.add(light, ambient, sphere, rings)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(20)
        self.stop_ambient_camera_rotation()


if __name__ == '__main__':
    os.system("manim -pqh manim_simulator.py TexturedSaturn")
