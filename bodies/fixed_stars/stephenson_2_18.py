# -*- coding:utf-8 -*-
# title           :史蒂文森2-18
# description     :史蒂文森2-18
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar, Sun
from common.consts import MO


class Stephenson_2_18(FixedStar):
    """
    史蒂文森2-18 (Stephenson 2-18)
    质量：40.0 太阳质量 ? TODO: 14.28e5 * MO ??
    大小：2150 太阳半径
    颜色：0xFF, 0xFF, 0xFF
    密度：0.0002 g/cm³ >> TODO:???
    半径：2158R☉
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="史蒂文森2-18", mass=14.28e5 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=((0xFF, 60, 0)),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.0002e3,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Stephenson_2_18()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)