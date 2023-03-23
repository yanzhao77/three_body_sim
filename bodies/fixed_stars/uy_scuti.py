# -*- coding:utf-8 -*-
# title           :参宿七
# description     :参宿七
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class UYScuti(FixedStar):
    """
    盾牌座 UY (UY Scuti)
    --------------- 维基百科 ---------------
    盾牌座UY
    盾牌座UY（影像中最亮恒星）周围有大量恒星。
    由美国哥伦比亚大学拉瑟弗德天文台摄于2011年。
    观测资料
    历元 J2000.0
    星座	盾牌座
    星官
    赤经	18h 27m 36.5334s[1]
    赤纬	-12° 27′ 58.866″[1]
    视星等（V）	9.0[1]
    特性
    光谱分类	M4Ia [1]
    B−V 色指数	2.6[1]
    变星类型	Semiregular[1]
    天体测定
    自行 (μ)	赤经：1.3[1] mas/yr
    赤纬：-1.6[1] mas/yr
    详细资料
    质量	7-10 M☉
    半径	~755 R☉
    亮度	86300 ~ 87100 [2] L☉
    其他命名
    V* UY Sct、BD-12 5055、IRC -10422、RAFGL 2162[1]
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="盾牌座UY", mass=10 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(255, 116, 0),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.22, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 3.271612056053086e-05,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = UYScuti()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=755)
