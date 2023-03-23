# -*- coding:utf-8 -*-
# title           :猎户座一等星
# description     :猎户座一等星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Rigel(FixedStar):
    """
    参宿七 （Rigel）
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000.0
    星座	猎户座
    星官	参（参宿）
    赤经	05h 14m 32.30s
    赤纬	−08° 12' 06"
    视星等（V）	0.12/6.80
    特性
    光谱分类	B8Ia
    U−B 色指数	−0.66
    B−V 色指数	−0.03
    变星类型	Slightly irregular
    天体测定
    径向速度 (Rv)	20.7 km/s
    自行 (μ)	赤经：1.87 mas/yr
    赤纬：−0.56 mas/yr
    视差 (π)	3.90 ± 0.81 mas
    距离	大约800 ly
    (大约260 pc)
    绝对星等 (MV)	−6.98
    详细资料
    质量	18 M☉
    半径	74-78 R☉
    亮度	53,800(126,000)(bolometric) L☉
    温度	11,400 K
    其他命名
    β Orionis, 19 Ori, Algebar; Elgebar, HD 34085, HR 1713, HIP 24436, SAO 131907
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="参宿七", mass=18 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(200, 200, 255),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.33, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.053406159915035785,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)
        self.glows = 7


if __name__ == '__main__':
    fixed_star = Rigel()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=78)
