# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from mayavi import mlab
import numpy as np
from bodies import Body
from mayavi import mlab
import numpy as np
from tvtk.api import tvtk
from abc import ABCMeta, abstractmethod
import os
import matplotlib.pyplot as plt
from common.func import get_dominant_colors


class MayaviBody:
    def __init__(self, body: Body):
        self.body = body
        if self.body.texture is None or self.body.texture == '':
            self.color = tuple(np.array(body.color) / 255)
        else:
            self.texture = self.__find_texture(self.body.texture)  # 纹理
            if self.texture is None:
                self.color = tuple(np.array(body.color) / 255)
            else:
                self.color = self.__texture_to_color(self.texture)
        self.build_body()

    def update_source_data(self):
        """

        :return:
        """
        x_offset = self.body.position[0] - self.sphere.mlab_source.x
        y_offset = self.body.position[1] - self.sphere.mlab_source.y
        z_offset = self.body.position[2] - self.sphere.mlab_source.z

        self.sphere.mlab_source.set(x=self.position[0], y=self.position[1], z=self.position[2])
        # print(self.sphere.mlab_source.y, self.position[1])
        # self.sphere.actor.actor.position = self.position
        return x_offset[0], y_offset[0], z_offset[0]

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

    def build_body(self):
        """
        构建球体对象
        :return:
        """
        if not hasattr(self, "sphere"):
            scale_factor = self.body.size_scale * self.body.raduis
            sphere = mlab.points3d(self.body.position[0], self.body.position[1], self.body.position[2],
                                   scale_factor=scale_factor,
                                   color=self.color,
                                   resolution=50,
                                   opacity=1,
                                   name=self.body.name)
            # # 调整镜面反射参数
            sphere.actor.property.specular = 0.5  # 0.1
            sphere.actor.property.specular_power = 128
            # 设置背面剔除，以更好的显示透明效果
            sphere.actor.property.backface_culling = True
            # sphere.actor.property.lighting_ = 10
            sphere.actor.property.lighting = False
            sphere.scene.disable_render = False
            # sphere_earth.scene.disable_render = False

            sphere.scene.anti_aliasing_frames = 10
            # sphere_earth.scene.anti_aliasing_frames = 0
            self.sphere = sphere

        if self.texture is not None and self.texture != '':
            self.__set_texture(self.texture)
            pass
        return self.sphere

    def __set_texture(self, image_file):
        if not os.path.exists(image_file):
            return
        img = plt.imread(image_file)
        outfile = image_file.replace('.jpg', '_flipped.jpg')
        img = img[::-1, ...]
        plt.imsave(outfile, img)
        image_file = outfile
        img = tvtk.JPEGReader(file_name=image_file)
        texture = tvtk.Texture(input_connection=img.output_port, interpolate=0, repeat=0)
        self.sphere.actor.actor.texture = texture
        self.sphere.actor.tcoord_generator_mode = 'sphere'
        cylinder_mapper = self.sphere.actor.tcoord_generator
        cylinder_mapper.prevent_seam = 0
