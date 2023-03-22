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


class Alcyone(FixedStar):
    """
    昴宿六 (Alcyone)
    质量：7个太阳质量
    密度：不详
    颜色值：#EFF6FF
    直径：6.12倍太阳直径

    中文名: 昴宿六
    外文名: Alcyone
    表面温度: 13000K；
    总光度: 太阳的2,400倍
    半径: 太阳的10倍
    质量: 太阳的7倍
    视星等: 2.87
    自转周期: 3天
    光谱型: B7III
    绝对星等: -2.76

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="昴宿六", mass=7 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xBB, 0xAA, 0xFF),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 9.856,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Alcyone()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=10)
