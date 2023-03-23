# -*- coding:utf-8 -*-
# title           :大角星
# description     :大角星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Arcturus(FixedStar):
    """
    大角星 (Arcturus)
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000
    星座	牧夫座
    星官	苍龙亢宿大角
    赤经	14h 15 m 39.7s
    赤纬	+19° 10' 56"
    视星等（V）	−0.04
    特性
    光谱分类	K1.5 IIIpe
    U−B 色指数	1.22
    B−V 色指数	1.24
    变星类型	Suspected
    天体测定
    径向速度 (Rv)	−5.2 km/s
    自行 (μ)	赤经：−1093.45 mas/yr
    赤纬：−1999.40 mas/yr
    视差 (π)	88.78 ± 0.68 mas
    距离	36.7 ± 0.3 ly
    (11.26 ± 0.09 pc)
    绝对星等 (MV)	−0.38
    详细资料
    质量	1.10 ± 0.06[1] M☉
    半径	25.7 ± 0.3[2] R☉
    亮度	180-210[3] L☉
    温度	4,300[4] K
    金属量	20–50% Sun
    年龄	> 4.6 × 109 年
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="大角星", mass=1.1 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(254, 218, 185),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.4, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.09124224657404181,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Arcturus()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=25.7)
