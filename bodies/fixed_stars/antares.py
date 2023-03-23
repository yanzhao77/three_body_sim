# -*- coding:utf-8 -*-
# title           :心大星
# description     :心大星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Antares(FixedStar):
    """
    心宿二 (Antares)
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000
    星座	天蝎座
    星官	心 (心宿)
    赤经	16h 29m 24s[1]
    赤纬	−26° 25′ 55″[1]
    视星等（V）	+0.96[2]
    特性
    光谱分类	M1.5Iab-b + B2.5V[3]
    U−B 色指数	+1.34[2]
    B−V 色指数	+1.83[2]
    变星类型	LC[4]
    天体测定
    径向速度 (Rv)	−3.4[5] km/s
    自行 (μ)	赤经：−12.11[1] mas/yr
    赤纬：−23.30[1] mas/yr
    视差 (π)	5.89 ± 1.00[1] mas
    距离	大约550 ly
    (大约170 pc)
    绝对星等 (MV)	−5.28
    详细资料
    A
    质量	15.5[6] M☉
    半径	680[6] R☉
    表面重力 (log g)	0.1[6]
    亮度	62,300[7] L☉
    温度	3400 ± 200[7] K
    自转速度 (v sin i)	20[8] km/s
    B
    质量	6-8 M☉
    半径	4 R☉
    温度	18,500[7] K


    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="心宿二A", mass=15.5 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(249,198,83),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.25, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 6.940769387339728e-05,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)
        self.glows = 6


if __name__ == '__main__':
    fixed_star = Antares()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=680)