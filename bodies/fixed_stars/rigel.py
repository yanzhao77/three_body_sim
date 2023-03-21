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
    参宿七（Rigel）
    质量：为21太阳质量
    大小：为78.9太阳半径
    颜色：为0xFF, 0xEE, 0xC8
    密度：为0.18 g/cm³  # TODO: 0.060199??
    直径：1.07184✕108 km

    中文名参宿七外文名Rigel
    别名： 猎户座β(β Orionis)、猎户座19(19 Orionis) [8]
    分类： 恒星
    质量： 约 21 M⊙(±3) [7]
    直径： 1.07184✕108 km表
    面温度约： 12100 K(±150) [7]
    视星等约 0.13 等(0.05 - 0.18) [9]
    绝对星等-7.92 等(± 0.28) [9]
    赤经： 5时14分32.30秒
    赤纬： -8°12′06″距地距离860 光年(± 80) [9]
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="参宿七", mass=21 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(141,213,227),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.060199,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)
        self.glow_num = 7


if __name__ == '__main__':
    from bodies import Sun
    fixed_star = Rigel()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)
