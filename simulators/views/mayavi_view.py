# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from mayavi import mlab
from tvtk.api import tvtk
import os
import matplotlib.pyplot as plt
from common.func import get_dominant_colors

from simulators.views.body_view import BodyView
import numpy as np


class MayaviView(BodyView):
    """
    Mayavi天体视图（天体效果展示用）
    """

    def update(self):
        """
        更新天体信息和数据，比如：更新天体的位置
        :return:
        """
        if hasattr(self.sphere, "mlab_source"):
            x_offset = self.body.position[0] - self.sphere.mlab_source.x
            y_offset = self.body.position[1] - self.sphere.mlab_source.y
            z_offset = self.body.position[2] - self.sphere.mlab_source.z
            self.sphere.mlab_source.set(x=self.position[0], y=self.position[1], z=self.position[2])
        else:
            x_offset, y_offset, z_offset = 0, 0, 0

        if hasattr(self, "rings"):
            if hasattr(self.rings, "mlab_source"):
                if hasattr(self, "rings") and self.body.has_rings:
                    x = self.rings.mlab_source.x
                    y = self.rings.mlab_source.y
                    z = self.rings.mlab_source.z
                    self.rings.mlab_source.set(x=x + x_offset, y=y + y_offset, z=z + z_offset)

        # return x_offset[0], y_offset[0], z_offset[0]

    def build_rings(self):
        if not hasattr(self, "rings") or self.rings is None:

            R = 2
            r = 0.3
            rings_scale = 0.5e5
            resolution = 50
            theta = np.linspace(0, 2 * np.pi, resolution)
            phi = np.linspace(0, 2 * np.pi, resolution)
            torus = np.zeros((3, resolution, resolution))

            for i in range(0, resolution):
                for j in range(0, resolution):  # size_scale=8.0e2
                    torus[0][i][j] = (R + r * np.cos(phi[j])) * np.cos(theta[i]) * \
                                     self.body.size_scale * rings_scale + self.body.position[0]
                    torus[1][i][j] = (R + r * np.cos(phi[j])) * np.sin(theta[i]) * \
                                     self.body.size_scale * rings_scale + self.body.position[1]
                    torus[2][i][j] = 1 * np.sin(phi[j]) + self.body.position[2]
            rings_color = (173 / 255, 121 / 255, 92 / 255)
            if hasattr(self.body, "rings_color"):
                rings_color = tuple(np.array(self.body.rings_color) / 255)
            self.rings = mlab.mesh(torus[0], torus[1], torus[2], color=rings_color,
                                   representation='surface')
        return self.rings

    def appear(self):
        """
        天体显示的操作，比如：构建天体视图对象
        :return:
        """
        if not hasattr(self, "sphere") or self.sphere is None:
            scale_factor = self.body.size_scale * self.body.diameter
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

        if self.body.has_rings:
            self.build_rings()
            return self.sphere, self.rings

        return self.sphere,

    def __set_texture(self, image_file):
        """
        设置纹理图片到天体
        :param image_file:
        :return:
        """
        outfile = image_file.replace('.jpg', '_flipped.jpg')
        if os.path.exists(outfile):
            image_file = outfile
        else:
            if not os.path.exists(image_file):
                return
            img = plt.imread(image_file)
            img = img[::-1, ...]
            plt.imsave(outfile, img)
            image_file = outfile

        img = tvtk.JPEGReader(file_name=image_file)
        texture = tvtk.Texture(input_connection=img.output_port, interpolate=0, repeat=0)
        self.sphere.actor.actor.texture = texture
        self.sphere.actor.tcoord_generator_mode = 'sphere'
        cylinder_mapper = self.sphere.actor.tcoord_generator
        cylinder_mapper.prevent_seam = 0
