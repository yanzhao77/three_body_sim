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


class Bellatrix(FixedStar):
    """
    参宿五 (Bellatrix)
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000
    星座	猎户座
    星官	参（参宿，白虎）
    赤经	05h 25m 07.86325s[1]
    赤纬	+06° 20′ 58.9318″[1]
    视星等（V）	1.64[2] (1.59 - 1.64[3])
    特性
    光谱分类	B2 III[4]
    U−B 色指数	–0.86[2]
    B−V 色指数	–0.21[2]
    变星类型	?[3]
    天体测定
    径向速度 (Rv)	+18.2[5] km/s
    自行 (μ)	赤经：–8.11[1] mas/yr
    赤纬：–12.88[1] mas/yr
    视差 (π)	12.92 ± 0.52[1] mas
    距离	250 ± 10 ly
    (77 ± 3 pc)
    绝对星等 (MV)	−2.78[6]
    详细资料
    质量	8.6[7] M☉
    半径	5.75[8] R☉
    表面重力 (log g)	3.60[9]
    亮度	9,211[8] L☉
    温度	22000[9] K
    金属量 [Fe/H]	–0.07[8] dex
    自转速度 (v sin i)	46±8[9] km/s
    年龄	25.2[7] Myr
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="参宿五", mass=8.6 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(122, 187, 255),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.5, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 63.69,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Bellatrix()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=5.75)
