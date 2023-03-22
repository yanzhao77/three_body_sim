# -*- coding:utf-8 -*-
# title           :史蒂文森2-18
# description     :史蒂文森2-18
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Stephenson_2_18(FixedStar):
    """
    史蒂文森2-18 (Stephenson 2-18)
    质量：40.0 太阳质量 ?
    大小：2150 太阳半径
    颜色：0xFF, 0xFF, 0xFF
    密度：0.0002 g/cm³
    半径：2158R☉


    中文名: 史蒂文森2-18
    外文名: Stephenson 2-18
    别名: Stephenson 2 DFK 1、RSGC2-18、St2-18、2MASS J18390238-0605106 [2]  、IRAS 18363-0607 [2]
    分类: 红超巨星
    发现者: 查尔斯·布鲁斯·史蒂文森发现时间1990年
    直径: 3005015000 km
    表面温度: 约 3200 K [3]
    赤经: 18时39分02.37秒
    赤纬: -6°05′10.54″
    距地距离: 约 20000 光年
    光谱型~M6 [4]
    视星等（V）不可见 [5]
    视星等（G）15.2631 ± 0.0092 [6]
    视星等（J）7.150 [7]
    视星等（H）4.698 [7]
    视星等（K）2.9 [7]
    半径: 2158R☉ [1]
    光度: 437000（90000~630000）L☉ [3]
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="史蒂文森2-18", mass=40.0 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(198, 29, 3),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.2, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 5.60e-06,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass,
            "texture_bright": 3,
            "texture_contrast": 4
        }
        super().__init__(**params)
        self.glows = (12, 1.008, 0.1)


if __name__ == '__main__':
    from bodies import Sun
    import math
    fixed_star = Stephenson_2_18()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)
    r = 2158
    print("密度換算", fixed_star.mass / 1e9 / (4 / 3 * math.pi * pow(r * sun.raduis, 3)))
