# -*- coding:utf-8 -*-
# title           :天狼星
# description     :天狼星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Sirius(FixedStar):
    """
    天狼星A (Sirius A)
    质量：太阳质量的2.02倍 (3.994e+30 kg)
    半径：太阳半径的1.711倍 (9.529e+05 km)
    直径：太阳直径的1.423倍 (2.386e+06 km)
    密度： 1.590 kg/m³
    自转： 16.7 度/小时
    --------------- 维基百科 ---------------
    天狼星A/B
    （大犬座α）
    Sirius A / B
    Position Alpha Cma.png
    天狼星的位置
    观测资料
    历元 J2000.0 (ICRS)
    星座	大犬座
    星官	天狼 (井宿)
    赤经	06h 45m 08.9173s[1][2]
    赤纬	−16° 42′ 58.017″[1][2]
    视星等（V）	−1.47 (A)[1]/ 8.30 (B)[3]
    特性
    光谱分类	A1V (A)[1]/ DA2 (B)[3]
    U−B 色指数	−0.05 (A)[4]/ −1.04 (B)[3]
    B−V 色指数	0.01 (A)[1]/ −0.03 (B)[3]
    天体测定
    径向速度 (Rv)	−7.6[1] km/s
    自行 (μ)	赤经：−546.05[1][2] mas/yr
    赤纬：−1223.14[1][2] mas/yr
    视差 (π)	379.21 ± 1.58[1] mas
    距离	8.6 ± 0.04 ly
    (2.64 ± 0.01 pc)
    绝对星等 (MV)	1.42 (A)[5]/ 11.18 (B)[3]
    轨道[6]
    伴星	天狼星 B
    绕行周期 (P)	50.09 yr
    半长轴 (a)	7.56"
    偏心率 (e)	0.592
    倾斜角 (i)	136.5°
    升交点黄经 (Ω)	44.6°
    近心点 历元 (T)	1894.13
    近心点幅角 (ω)
    (secondary)	147.3°
    详细资料
    质量	2.02[7](A) /    0.978[7](B) M☉
    半径	1.711[7](A) /    0.0084 ± 3%[8](B) R☉
    表面重力 (log g)	4.33[9](A)/8.57[8](B)
    亮度	25.4[7](A) /
    0.026[10](B) L☉
    温度	9,940[9](A) /
    25,200[7](B) K
    金属量	[Fe/H] =0.50[11](A)
    自转	16 km/s[12](A)
    年龄	2-3 × 108[7] 年
    其他命名
    System: α Canis Majoris, α CMa, 9 Canis Majoris, 9 CMa, HD 48915, HR 2491, BD -16°1591, GCTP 1577.00 A/B, GJ 244 A/B, LHS 219, ADS 5423, LTT 2638, HIP 32349.
    B: EGGR 49, WD 0642-166.[1][13][14]
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="天狼星A", mass=2.02 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0xFF, 0xFF),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.55, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 568.8079963025574,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Sirius()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=1.71)
