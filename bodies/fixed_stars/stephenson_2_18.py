# -*- coding:utf-8 -*-
# title           :史蒂文森2-18
# description     :史蒂文森2-18
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Stephenson_2_18(FixedStar):
    """
    史蒂文森2-18 (Stephenson 2-18)
    质量：40.0 太阳质量
    分类: 红超巨星
    直径: 3005015000 km
    半径: 2158R☉ [1]
    https://baijiahao.baidu.com/s?id=1734063731226819203&wfr=spider&for=pc
    这颗恒星的体积就更加夸张了，根据科学家的估计，这颗恒星的体积，是太阳的100亿倍。换一句话说，史蒂文森2-18的体积是盾牌座UY的两倍。
    --------------- 维基百科 ---------------
    史蒂芬森2-18
    Stephenson 2-18 zoomed in, 2MASS survey, 2003.png
    2MASS拍摄的史蒂芬森2-18与其母星团史蒂芬森2（左上）。
    Credit: 斯特拉斯堡大学/CNRS (2003)
    观测资料
    历元 J2000
    星座	盾牌座
    星官
    赤经	18h 39m 02.3709s[1]
    赤纬	-06° 05′ 10.5357″[1]
    视星等（V）
    特性
    演化阶段	红超巨星
    光谱分类	~M6[2]
    视星等 (G)	15.2631±0.0092[1]
    视星等 (J)	7.150[3]
    视星等 (H)	4.698[3]
    视星等 (K)	2.9[3]
    天体测定
    自行 (μ)	赤经：−3.045±0.511[1] mas/yr
    赤纬：−5.950±0.480[1] mas/yr
    视差 (π)	−0.0081 ± 0.3120[1] mas
    距离	18,900[4] ly
    (5,800[4] pc)
    详细资料
    半径	2,150[5][a] R☉
    亮度	437,000[5] (90,000[6] – 630,000[4][b]) L☉
    温度	3,200[5] K
    其他命名
    史蒂芬2-18、史蒂芬森2DFK1、RSGC2-18、2MASS J18390238-0605106、IRAS 18363-0607
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="史蒂文森2-18", mass=40.0 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(198, 29, 3),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.2, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 5.666922409347618e-06,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass,
            "texture_bright": 3,
            "texture_contrast": 4
        }
        super().__init__(**params)
        self.glows = (12, 1.008, 0.1)


if __name__ == '__main__':
    fixed_star = Stephenson_2_18()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=2150)
