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


class Betelgeuse(FixedStar):
    """
    参宿四 (Betelgeuse)
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000.0
    星座	猎户座
    星官	参宿
    赤经	05h 55m 10.3053s[1]
    赤纬	+07° 24′ 25.426″[1]
    视星等（V）	0.42[1]（0.3 to 1.2）
    特性
    光谱分类	M2Iab（红超巨星）[1]
    U−B 色指数	2.06[2]
    B−V 色指数	1.85（橙红）[2]
    变星类型	SR c （半规则）[1]
    天体测定
    径向速度 (Rv)	+21.91[1] km/s
    自行 (μ)	赤经：24.95 ± 0.08[3] mas/yr
    赤纬：9.56 ± 0.15[3] mas/yr
    视差 (π)	5.07 ± 1.10[3] mas
    距离	643 ± 146 [3] ly
    (197 ± 45 [3] pc)
    绝对星等 (MV)	−6.05[4]
    详细资料
    质量	~18–19[5] M☉
    半径	~1180[6] R☉
    表面重力 (log g)	-0.5[7]
    亮度	~140,000[8] L☉
    温度	3,500[7][9] K
    金属量	0.05 Fe/H[10]
    自转	5 km/s[9]
    年龄	~1.0×107 [5] 年
    其他命名
    参宿四，α Ori，58 Ori，HR 2061, BD +7° 1055, HD 39801, FK5 224, HIP 27989, SAO 113271, GC 7451, CCDM J05552+0724AP, AAVSO 0549+07
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="参宿四", mass=19 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(254, 162, 1),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.24, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.6282093105916417e-05,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Betelgeuse()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=1180)
