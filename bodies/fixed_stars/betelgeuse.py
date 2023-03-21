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


class Betelgeuse(FixedStar):
    """
    TODO： 参宿四 (Betelgeuse)
    质量：20太阳质量
    密度：1.16×10⁻⁴ g/cm³
    颜色值：#FF9100
    直径：1,180倍太阳直径

    中文名参宿四外文名Betelgeuse别    名α Orionis分    类红超巨星质    量11.6，11.6 + 5.0 或 11.6 - 3.9 M⊙直    径887 ± 203 或955 ± 217 D⊙表面温度3590 K视星等+0.50（0.0 ~ +1.3）绝对星等-5.85赤    经5时55分10.30秒赤    纬+7°24′25.43″距地距离640 光年光谱型M1-M2Ia-abU-B 色指数+2.06B-V 色指数+1.85光    度90000 ~ 1.5 × 10^5 L⊙变星类型SRc

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="参宿四", mass=20 * MO,
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
    fixed_star = Betelgeuse()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)