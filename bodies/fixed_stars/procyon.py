# -*- coding:utf-8 -*-
# title           :北河三
# description     :北河三
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Procyon(FixedStar):
    """
    南河三 (Procyon）
    --------------- 维基百科 ---------------
    南河三A/B
    观测资料
    历元 J2000
    星座	小犬座
    星官	南河（井宿，朱雀）
    赤经	07h 39m 18.11950s[1]
    赤纬	+05° 13′ 29.9552″[1]
    视星等（V）	0.34[2] (A) / 10.7[3] (B)
    特性
    光谱分类	F5 IV–V[2] + DQZ[4]
    U−B 色指数	+0.00[5]
    B−V 色指数	+0.42[5]
    变星类型	？[6] (A)
    天体测定
    径向速度 (Rv)	−3.2[7] km/s
    自行 (μ)	赤经：−714.590[1] mas/yr
    赤纬：−1036.80[1] mas/yr
    视差 (π)	284.56 ± 1.26[1] mas
    距离	11.46 ± 0.05 ly
    (3.51 ± 0.02 pc)
    绝对星等 (MV)	2.66/13.0[3]
    详细资料
    南河三A
    质量	1.499±0.031[8] M☉
    半径	2.048±0.025[2] R☉
    表面重力 (log g)	3.96[2]
    亮度	6.93[2] L☉
    温度	6,530±50[2] K
    金属量 [Fe/H]	−0.05±0.03[2] dex
    自转	23天[9]
    自转速度 (v sin i)	3.16±0.50[2] km/s
    年龄	1.87±0.13[8] Gyr
    南河三B
    质量	0.602±0.015[4] M☉
    半径	0.01234±0.00032[4] R☉
    表面重力 (log g)	8.0[4]
    亮度	0.00049[10] L☉
    温度	7,740±50[4] K
    年龄	1.37[10] Gyr
    轨道[11]
    伴星	南河三B
    绕行周期 (P)	40.82 yr
    半长轴 (a)	4.3"
    偏心率 (e)	0.407
    倾斜角 (i)	31.1°
    升交点黄经 (Ω)	97.3°
    近心点 历元 (T)	1967.97
    近心点幅角 (ω)
    (secondary)	92.2°
    其他命名
    Elgomaisa, Algomeysa, Antecanis, α Canis Minoris, 10 Canis Minoris,GCTP 1805.00, HR 2943, BD+05°1739, HD 61421, LHS 233, GJ 280, HIP 37279, SAO 115756.[12]






    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="南河三", mass=1.5 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xF5, 0xE8, 0xD5),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 245.15024448281426,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Procyon()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=2.05)