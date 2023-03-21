# -*- coding:utf-8 -*-
# title           :天狼星
# description     :天狼星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body
from common.consts import MO
from common.image_utils import gen_fixed_star_texture, find_texture_root_path
import os


class FixedStar(Body):
    """
    恒星基类
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="恒星", mass=1 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0xFF, 0xFF),
                 texture=None, size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False, density=1.408e3):
        if texture is None or texture == "fixed_star.png":
            self.color = color
            texture = self.gen_texture(texture)
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": density,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)

    def gen_texture(self, texture):
        texture_path = find_texture_root_path()
        if texture_path is None:
            err_msg = "未找到纹理图片目录"
            raise Exception(err_msg)
        save_file = os.path.join(texture_path, "%s.png" % str(self.__class__.__name__).lower())
        fixed_star_img = os.path.join(texture_path, texture)
        gen_fixed_star_texture(self.color, save_file=save_file, fixed_star_img=fixed_star_img)
        return save_file

    @property
    def is_fixed_star(self):
        """
        恒星
        :return:
        """
        return True


if __name__ == '__main__':
    print(FixedStar())
