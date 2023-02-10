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

    if isinstance(radius_offset, float):
        radius = radius + np.random.rand(len(angles)) * radius_offset

    if isinstance(force_offset, float):
        force = force + np.random.rand(len(angles)) * force_offset

    pxs = radius * np.cos(angles)
    pys = radius * np.sin(angles)

    fys = force * np.cos(angles)  # math.cos(math.radians(angle))
    fxs = force * np.sin(angles)  # math.sin(math.radians(angle))

    # return pxs, pys, fxs, fys
    return np.round(pxs, 2), np.round(pys, 2), -np.round(fxs, 2), np.round(fys, 2)


def calculate_distance(pos1, pos2=[0, 0, 0]):
    """
    计算两点间的距离
    :param pos1:
    :param pos2:
    :return:
    """
    d = pow(pow(np.array(pos1[0]) - np.array(pos2[0]), 2) +
            pow(np.array(pos1[1]) - np.array(pos2[1]), 2) +
            pow(np.array(pos1[2]) - np.array(pos2[2]), 2), 1 / 2)
    return d


if __name__ == '__main__':
    print(calculate_distance([6, 8, 0], [3, 4, 0]))
