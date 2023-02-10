# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from PIL import Image
from common.consts import AU
import numpy as np
import random


def get_dominant_colors(infile, resize=(20, 20)):
    """
    获取图片的主要颜色
    :param infile:
    :param resize:
    :return:
    """
    image = Image.open(infile)

    # 缩小图片，否则计算机压力太大
    small_image = image.resize(resize)
    result = small_image.convert(
        "P", palette=Image.ADAPTIVE, colors=10
    )

    # 10个主要颜色的图像

    # 找到主要的颜色
    palette = result.getpalette()
    color_counts = sorted(result.getcolors(), reverse=True)
    colors = list()

    for i in range(10):
        palette_index = color_counts[i][1]
        dominant_color = palette[palette_index * 3: palette_index * 3 + 3]
        colors.append(tuple(dominant_color))

    return colors


def circle_x_y(points, radius=1.6 * AU):
    """

    :param points:
    :param radius:
    :return:
    """
    x = radius * np.cos(points)
    y = radius * np.sin(points)
    return x, y


def get_position_force(angles, force=1, radius=1, radius_offset=None, force_offset=None):
    """

    :param angles:
    :param force:
    :param radius:
    :param radius_offset:
    :param force_offset:
    :return:
    """
    angles = np.array(angles * np.pi)

    if isinstance(radius_offset, int):
        radius = radius + np.random.rand(len(angles)) * radius_offset

    if isinstance(force_offset, int):
        force = force + np.random.rand(len(angles)) * force_offset

    pxs = radius * np.cos(angles)
    pys = radius * np.sin(angles)

    fys = force * np.cos(angles)  # math.cos(math.radians(angle))
    fxs = force * np.sin(angles)  # math.sin(math.radians(angle))

    # return pxs, pys, fxs, fys
    return np.round(pxs, 2), np.round(pys, 2), -np.round(fxs, 2), np.round(fys, 2)
#
#
# import math
#
# """
# 用python写一个函数，根据不同角度的参数列表，返回坐标 pos_x, pos_y，以及分解力fx fy
#
# def get_force(angle_list):
#     pos_x = 0
#     pos_y = 0
#     fx = 0
#     fy = 0
#     for angle in angle_list:
#         force_x, force_y = get_force_from_angle(angle)
#         pos_x += force_x
#         pos_y += force_y
#         fx += force_x
#         fy += force_y
#
#     return pos_x, pos_y, fx, fy
#
# def get_force_from_angle(angle):
#     force_x = math.cos(math.radians(angle))
#     force_y = math.sin(math.radians(angle))
#     return force_x, force_y
# """
#
# """
# ```python
# def get_positions_forces_from_angles(angles,radius, force):
#
# ```
# """
#
#
# def get_position_force(angle_list, radius=1, force=1):
#     fxs = []
#     fys = []
#     angle_list = np.array(angle_list * np.pi)
#     pxs = radius * np.cos(angle_list)
#     pys = radius * np.sin(angle_list)
#
#     for angle in angle_list:
#         fx, fy = get_force_from_angle(angle)
#         fxs.append(fx * force)
#         fys.append(fy * force)
#
#     return np.round(pxs, 2), np.round(pys, 2), np.round(fxs, 2), np.round(fys, 2)
#
#
# def get_force_from_angle(angle):
#     force_x = math.cos(angle)
#     force_y = math.sin(angle)
#     # force_x = math.cos(math.radians(angle))
#     # force_y = math.sin(math.radians(angle))
#     return force_x, force_y
#
#
# if __name__ == '__main__':
#     # a = [0, 45, 90, 135, 180, 225, 270, 315, 360]
#     # start:返回样本数据开始点
#     # stop:返回样本数据结束点
#     # num:生成的样本数据量，默认为50
#     points = np.linspace(0, 2 * np.pi, 10)
#     # points = np.array([0, 45, 90, 135, 180, 225, 270, 315, 360])
#     # points = np.array([0.        , 0.17453293, 0.34906585, 0.52359878, 0.6981317 ,
#     #    0.87266463, 1.04719755, 1.22173048, 1.3962634 , 1.57079633])
#     # x, y = circle_x_y(points, 1)
#     # print(x, y)
#     print(points)
#     pos_x, pos_y, fx, fy = circle_x_y_f(points, radius=1.6, force=25.37)
#     print(pos_x, pos_y, fx, fy)
#
# """
#     asteroids = [
#         Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
#                  init_position=[1.6 * AU, 0, 0],
#                  init_velocity=[0, 25.37, 0],
#                  distance_scale=1),
#         Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
#                  init_position=[-1.6 * AU, 0, 0],
#                  init_velocity=[0, -25.37, 0],
#                  distance_scale=1),
#         Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
#                  init_position=[0, 1.6 * AU, 0],
#                  init_velocity=[-25.37, 0, 0],
#                  distance_scale=1),
#         Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
#                  init_position=[0, -1.6 * AU, 0],
#                  init_velocity=[25.37, 0, 0],
#                  distance_scale=1),
#     ]
# """
