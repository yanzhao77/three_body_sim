# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from PIL import Image


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
