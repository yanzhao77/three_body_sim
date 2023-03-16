# -*- coding:utf-8 -*-
# title           :颜色工具类
# description     :颜色工具类
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from ursina import Vec4


def to_vec4_color(colour: tuple, alpha=1) -> Vec4:
    if len(colour) == 3:
        return Vec4(colour[0], colour[1], colour[2], alpha * 255) / 255
    elif len(colour) == 4:
        return Vec4(colour[0], colour[1], colour[2], colour[3]) / 255
    raise Exception("colour错误")


def adjust_brightness(color: Vec4, target_brightness: float = 0.6) -> Vec4:
    """
    调整颜色的亮度到目标 target_brightness（确保亮度不超过 1.0）
    :param color:
    :param target_brightness:（确保亮度不超过 1.0）
    :return:
    """
    # 获取颜色的亮度值
    brightness = color.x * 0.299 + color.y * 0.587 + color.z * 0.114

    # 如果亮度值不够，增加亮度
    if brightness < target_brightness:
        # 调整 RGB 值，确保亮度不超过 1.0
        r = min(color.x + (target_brightness - brightness), 1.0)
        g = min(color.y + (target_brightness - brightness), 1.0)
        b = min(color.z + (target_brightness - brightness), 1.0)
        return Vec4(r, g, b, color.w)
    else:
        return color
