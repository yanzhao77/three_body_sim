# -*- coding:utf-8 -*-
# title           :参宿七
# description     :参宿七
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class YCanumVenaticorum(FixedStar):
    """

中文名猎犬座Y外文名Y Canum Venaticorum
别    名La Superba
分    类红巨星，碳星，变星
质    量3M⊙
直    径 299280000 km
表面温度2800K反照率不是行星视星等4.99赤    经12时45分07.83秒赤    纬+45°26′24.92″距地距离1000Ly光    度5800L⊙光    谱N3U-B色指数6.62B-V色指数2.54变星类型SRb编    号HR4846,HD110914,HIP62223
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="猎犬座Y", mass=3 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(255,55,18),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.000425,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    from bodies import Sun
    import math

    fixed_star = YCanumVenaticorum()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)
    r = 215
    print("密度換算", fixed_star.mass / 1e9 / (4 / 3 * math.pi * pow(r * sun.raduis, 3)))
    print((299280000 / sun.diameter))