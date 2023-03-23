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


class Aldebaran(FixedStar):
    """
    毕宿五 (Aldebaran)
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000.0
    星座	金牛座
    星官	毕（毕宿）
    赤经	04h 35m 55.23907s[1]
    赤纬	+16° 30′ 33.4885″[1]
    视星等（V）	0.75–0.95[2]
    特性
    演化阶段	红巨星分支[3]
    光谱分类	K5+ III[4]
    视星等 (J)	−2.095[5]
    U−B 色指数	+1.92[6]
    B−V 色指数	+1.44[6]
    变星类型	LB[2]
    天体测定
    径向速度 (Rv)	+54.26±0.03[7] km/s
    自行 (μ)	赤经：63.45±0.84[1] mas/yr
    赤纬：−188.94±0.65[1] mas/yr
    视差 (π)	49.97 ± 0.75[8] mas
    距离	65.3 ± 1 ly
    (20 ± 0.3 pc)
    绝对星等 (MV)	−0.641±0.034[8]
    详细资料
    质量	1.16±0.07[9] M☉
    半径	44.13±0.84[10] R☉
    表面重力 (log g)	1.45±0.3[11]
    亮度	439±17[12] L☉
    温度	3,900±50[11] K
    金属量 [Fe/H]	−0.33±0.1[11] dex
    自转	520 days[13]
    自转速度 (v sin i)	3.5±1.5[11] km/s
    年龄	6.4Gyr[9] Gyr

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="毕宿五", mass=1.16 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(250, 195, 47),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.35, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.019004605622458228,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Aldebaran()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=44.13)
