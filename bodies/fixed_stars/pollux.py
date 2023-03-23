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


class Pollux(FixedStar):
    """
    北河三 (Pollux)
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000.0
    星座	双子座
    星官	北河 (井宿)
    赤经	07h 45m 18.94987s[1]
    赤纬	+28° 01′ 34.3160″[1]
    视星等（V）	1.14[2]
    特性
    演化阶段	巨星
    光谱分类	K0III[3]
    U−B 色指数	+0.86[2]
    B−V 色指数	+1.00[2]
    变星类型	Suspected[4]
    天体测定
    径向速度 (Rv)	+3.23[5] km/s
    自行 (μ)	赤经：–626.55[1] mas/yr
    赤纬：–45.80[1] mas/yr
    视差 (π)	96.54 ± 0.27[1] mas
    距离	33.78 ± 0.09 ly
    (10.36 ± 0.03 pc)
    绝对星等 (MV)	+1.08±0.02[6]
    详细资料
    质量	1.91±0.09[7] M☉
    半径	8.8±0.1[8] R☉
    表面重力 (log g)	2.685±0.09[8]
    亮度	43[9] L☉
    温度	4666±95[8] K
    金属量 [Fe/H]	–0.07 to +0.19[8] dex
    自转	558 days[10]
    自转速度 (v sin i)	2.8[11] km/s
    年龄	724[12] Myr
    其他命名
    Beta Geminorum, 78 Geminorum, BD+28°1463, GCTP 1826.00, Gliese 286, HD 62509, HIP 37826, HR 2990, LFT 548, LHS 1945, LTT 12065, SAO 79666.[13]





    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="北河三", mass=2 * MO,
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
            "density": 4.132231404958686,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Pollux()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=8.8)