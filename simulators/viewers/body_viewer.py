# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from abc import ABCMeta, abstractmethod
from bodies import Body
from common.func import get_dominant_colors
import numpy as np
import os


class BodyViewer(metaclass=ABCMeta):
    def __init__(self, body: Body):
        self.body = body
        self.sphere = None
        if self.body.texture is None or self.body.texture == '':
            self.color = tuple(np.array(body.color) / 255)
        else:
            self.texture = self.__find_texture(self.body.texture)  # 纹理
            if self.texture is None:
                self.color = tuple(np.array(body.color) / 255)
            else:
                self.color = self.__texture_to_color(self.texture)
        self.sphere = self.build()
        self.position = None

    def __find_texture(self, texture):
        """
        在多路径下寻找纹理图片
        :param texture: 纹理图片
        :return: 纹理图片的路径
        """
        paths = ['./textures', '../textures']
        for path in paths:
            p = path + "/" + texture
            if os.path.exists(p):
                return p

        return None

    def __texture_to_color(self, texture):
        """
        根据纹理图片获取颜色
        :param texture:
        :return:
        """
        colors = get_dominant_colors(texture)
        first_color = colors[0]
        # print(self.name, first_color)
        return tuple(np.array(first_color) / 255)

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def build(self):
        pass
