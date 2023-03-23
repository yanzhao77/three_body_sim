# -*- coding:utf-8 -*-
# title           :心宿二
# description     :心宿二
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class EtaCarinae(FixedStar):
    """
    海山二/船底座 （Eta Carinae）
    --------------- 维基百科 ---------------
    观测资料
    历元 J2000
    星座	船底座
    星官	海山 (近南极星区)
    赤经	10h 45m 03.6s[1]
    赤纬	-59° 41′ 04″
    视星等（V）	6.21 (-0.8–7.9)[1]
    特性
    光谱分类	B3-5Ia0/O7I(WC8)
    U−B 色指数	-0.45
    B−V 色指数	0.61
    变星类型	高光度蓝变星 双星 或复合星
    天体测定
    径向速度 (Rv)	−25.0[1] km/s
    自行 (μ)	赤经：−7.6[1] mas/yr
    赤纬：1.0[1] mas/yr
    详细资料
    质量	105-125/30[2] M☉
    半径	278/12 R☉
    亮度	5,150，000/292,000bolometric) L☉
    温度	16500/38800 K
    金属量	?
    自转	?
    年龄	~ <3 × 106 年
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="海山二", mass=125 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(111, 140, 255),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.28, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.008191779995598798,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = EtaCarinae()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=278)
