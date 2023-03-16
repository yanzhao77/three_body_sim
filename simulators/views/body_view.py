# -*- coding:utf-8 -*-
# title           :天体视图
# description     :天体视图（天体效果展示用）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from abc import ABCMeta, abstractmethod
from bodies import Body
from common.func import get_dominant_colors
import numpy as np
import os


class BodyView(metaclass=ABCMeta):
    """
    天体视图（天体效果展示用）
    """

    def __init__(self, body: Body, bodies_system):
        self.body = body
        self.bodies_system = bodies_system
        self.sphere = None
        if self.body.texture is None or self.body.texture == '':
            self.color = tuple(np.array(body.color) / 255)
        else:
            self.texture = self.__find_texture(self.body.texture)  # 纹理
            if self.texture is None:
                self.color = tuple(np.array(body.color) / 255)
            else:
                self.color = self.__get_texture_main_color(self.texture)
        self.appear()
        self.position = body.position
        self.name = body.name
        self.mass = body.mass
        self.raduis = body.raduis
        self.velocity = body.velocity

        self.appeared = True

    def __repr__(self):
        return '<%s> m=%.3e(kg), r=%.3e(km), p=[%.3e,%.3e,%.3e](km), v=%s(km/s)' % \
               (self.name, self.mass, self.raduis,
                self.position[0], self.position[1], self.position[2], self.velocity)

    def __find_texture(self, texture):
        """
        尝试在多个路径下寻找纹理图片
        :param texture: 纹理图片
        :return: 纹理图片的路径
        """
        paths = ['./textures', '../textures']
        for path in paths:
            p = path + "/" + texture
            if os.path.exists(p):
                return p

        return None

    def __get_texture_main_color(self, texture):
        """
        获取纹理图片的主要颜色
        :param texture:
        :return:
        """
        colors = get_dominant_colors(texture)
        first_color = colors[0]
        # print(self.name, first_color)
        return tuple(np.array(first_color) / 255)

    @abstractmethod
    def update(self):
        """
        更新天体信息和数据，比如：更新天体的位置
        :return:
        """
        pass

    def disappear(self):
        """
        天体消失的操作，比如：销毁天体视图对象
        :return:
        """
        pass

    @abstractmethod
    def appear(self):
        """
        天体显示的操作，比如：构建天体视图对象
        :return:
        """
        pass
