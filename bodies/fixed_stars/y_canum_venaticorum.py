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


class YCanumVenaticorum(FixedStar):
    """
    猎犬座Y (Y Canum Venaticorum)
    分  类: 红巨星，碳星，变星
    --------------- 维基百科 ---------------
    La Superba
    Y Canum Venaticorum.jpg
    天文程式 Celestia 中的猎犬座Y（右）与太阳（左）的体积比较。
    观测资料
    历元 J2000.0
    星座	猎犬座
    星官
    赤经	12h 45m 07.83s
    赤纬	+45° 26' 24.92"
    视星等（V）	+4.8 to +6.3
    天体测定
    自行 (μ)	赤经：-2.20 mas/yr
    赤纬：13.05 mas/yr
    视差 (π)	4.590 mas
    距离	711 ± 113 ly
    (218 ± 35 pc)
    特性
    光谱分类	C54J, C-N5, C-J4.5
    变星类型	半规则变星
    详细资料
    质量	3 M☉
    半径	215 R☉
    亮度	4,400
    (bolometric) L☉
    温度	2,800 K
    其他命名
    Y Canum Venaticorum, HR 4846, HD 110914, BD+46°1817, FK5 1327, HIP 62223, SAO 44317, GC 17342
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="猎犬座Y", mass=3 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(255, 55, 18),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.3, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.000425,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = YCanumVenaticorum()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=215)
