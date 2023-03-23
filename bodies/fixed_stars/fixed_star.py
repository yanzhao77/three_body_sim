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
                 rotation_speed=0.1, ignore_mass=False, density=1.408e3, trail_color=None,
                 texture_bright=None, texture_contrast=None):
        if texture is None or texture == "fixed_star.png":
            self.color = color
            # bright=1.1, contrast=3.2
            texture = self.gen_texture(texture, texture_bright, texture_contrast)
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
            "ignore_mass": ignore_mass,
            "trail_color": trail_color
        }
        super().__init__(**params)
        self.light_on = True
        self.glows = (12, 1.009, 0.08)

    def gen_texture(self, texture, texture_bright, texture_contrast):
        if texture is None:
            return None
        texture_path = find_texture_root_path()
        if texture_path is None:
            err_msg = "未找到纹理图片目录"
            raise Exception(err_msg)
        save_file = os.path.join(texture_path, "fixed_star_%s.png" % str(self.__class__.__name__).lower())
        if os.path.exists(save_file):
            return save_file
        fixed_star_img = os.path.join(texture_path, texture)
        gen_fixed_star_texture(self.color,
                               bright=texture_bright,
                               contrast=texture_contrast,
                               save_file=save_file,
                               fixed_star_img=fixed_star_img)
        return save_file

    @property
    def is_fixed_star(self):
        """
        恒星
        :return:
        """
        return True

    def compare_with_sun(self):
        from bodies import Sun
        sun = Sun()
        print("---------------------------------")
        print("质量: %.2f M☉ (%.4g kg)" % (self.mass / sun.mass, self.mass))
        print("半径: %.2f R☉ (%.4g km)" % (self.raduis / sun.raduis, self.raduis))
        print("直径: %.2f D☉ (%.4g km)" % (self.diameter / sun.diameter, self.diameter))
        num_sun_volume = self.volume / sun.volume  # 相当于多少个太阳体积
        if num_sun_volume <= 10000:
            print("体积: %.2f V☉ (%.4g km³)" % (num_sun_volume, self.volume))
        elif num_sun_volume <= 100000000:
            print("体积: %.2f万 V☉ (%.4g km³)" % (num_sun_volume / 10000, self.volume))
        else:
            print("体积: %.2f亿 V☉ (%.4g km³)" % (num_sun_volume / 100000000, self.volume))

    def density_by_radius(self, raduis=None, num_sun_raduis=None):
        """
        密度換算
        @param raduis: 半径的长度（km）
        @param num_sun_raduis: 多少个太阳半径
        @return:
        """
        from bodies import Sun
        import math

        sun = Sun()
        if num_sun_raduis is not None:
            raduis = num_sun_raduis * sun.raduis
        print("---------------------------------\n密度換算: ", self.mass / 1e9 / (4 / 3 * math.pi * pow(raduis, 3)))


if __name__ == '__main__':
    print(FixedStar())
