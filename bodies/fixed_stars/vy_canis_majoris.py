# -*- coding:utf-8 -*-
# title           :大犬座VY
# description     :大犬座VY
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class VYCanisMajoris(FixedStar):
    """
    T大犬座VY（VY Canis Majoris）
    --------------- 维基百科 ---------------
    VY Canis Majoris
    Sun and VY Canis Majoris.svg

    太阳与大犬座VY大小比较
    观测资料
    历元 J2000
    星座	大犬座
    星官
    赤经	07h 22m 58.33s[1]
    赤纬	−25° 46′ 03.17″[1]
    视星等（V）	6.5 to 9.6[2]
    7.9607[3]
    特性
    光谱分类	M3[1]-M5e Ia[4]
    B−V 色指数	2.24[1]
    变星类型	半规则变星[5]
    天体测定
    径向速度 (Rv)	49 ± 10[1] km/s
    自行 (μ)	赤经：9.84[1] mas/yr
    赤纬：0.75[1] mas/yr
    视差 (π)	0.83 ± 0.1[6] mas
    距离	大约3900 ly
    (大约1200 pc)
    详细资料
    质量	~30[7]-40[8] M☉
    半径	~1400左右[9] R☉
    亮度	~450,000[10][11] L☉
    温度	~3000[11] K
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="大犬座VY", mass=30 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(234, 90, 65),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.23, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.5393586005830937e-05,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass,
            "texture_bright": 1,
            "texture_contrast": 5
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = VYCanisMajoris()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=1400)
