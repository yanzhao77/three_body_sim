# -*- coding:utf-8 -*-
# title           :公共库函数
# description     :公共库函数
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
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


def get_positions_velocitys(angles, velocity=1, radius=1, radius_offset=None, velocity_offset=None):
    """
    以位置 （0, 0, 0）为中心，随机获取空间上的位置和公转方向的速度集合
    （比如：获取大批小行星的位置）
    :param angles: 参考中心位置（0, 0, 0）的角度集合
    :param velocity: 速度
    :param radius: 半径（距离中心位置（0, 0, 0）的距离）
    :param radius_offset:在半径的基础上，随机偏移的值
    :param velocity_offset:在速度的基础上，随机偏移的值
    :return:
    """
    angles = np.array(angles * np.pi)

    if isinstance(radius_offset, float):
        radius = radius + np.random.rand(len(angles)) * radius_offset

    if isinstance(velocity_offset, float):
        velocity = velocity + np.random.rand(len(angles)) * velocity_offset

    pxs = radius * np.cos(angles)
    pys = radius * np.sin(angles)

    vys = velocity * np.cos(angles)
    vxs = velocity * np.sin(angles)

    # return pxs, pys, fxs, fys
    return np.round(pxs, 2), np.round(pys, 2), -np.round(vxs, 2), np.round(vys, 2)


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
