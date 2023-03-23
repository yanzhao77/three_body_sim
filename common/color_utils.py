# -*- coding:utf-8 -*-
# title           :颜色工具类
# description     :颜色工具类
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================


def conv_to_vec4_color(colour: tuple, alpha=1):
    """

    :param colour:
    :param alpha:
    :return:
    """
    from ursina import Vec4
    if len(colour) == 3:
        return Vec4(colour[0], colour[1], colour[2], alpha * 255) / 255
    elif len(colour) == 4:
        return Vec4(colour[0], colour[1], colour[2], colour[3]) / 255
    raise Exception("colour错误")


def adjust_brightness(color, target_brightness: float = 0.6):
    """
    调整颜色的亮度到目标 target_brightness（确保亮度不超过 1.0）
    :param color:
    :param target_brightness:（确保亮度不超过 1.0）
    :return:
    """
    from ursina import Vec4
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


def get_inverse_color(color):
    """计算 RGB 颜色的反色"""
    r, g, b = color
    if r + g + b <= 3:
        inverse_r = 1.0 - r
        inverse_g = 1.0 - g
        inverse_b = 1.0 - b
    else:
        inverse_r = 255 - r
        inverse_g = 255 - g
        inverse_b = 255 - b
    return inverse_r, inverse_g, inverse_b
