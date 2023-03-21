# -*- coding:utf-8 -*-
# title           :大角星
# description     :大角星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar, Sun
from common.consts import MO


class Arcturus(FixedStar):
    """
    TODO： 大角星 (Arcturus)
    质量：20太阳质量
    密度：1.16×10⁻⁴ g/cm³
    颜色值：#FF9100
    直径：1,180倍太阳直径


    中文名大角星外文名Arcturus别    名牧夫座α，牧夫座16 [2]  、α Boötis、天栋分    类恒星（橙巨星）质    量约 1.08 M⊙ [4] 表面温度约 4286 K [4] 视星等-0.05 等 [3] 绝对星等-0.38 等赤    经14时15分39.7秒赤    纬+19°10′56″距地距离36.7 光年半    径25.4±0.2 R☉ [4] 光    度170 L☉ [5] 光谱类型K0III [2]

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="大角星", mass=20 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0xF0, 0xE4),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.408e3,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Arcturus()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)