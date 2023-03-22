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
    质量：太阳质量
    颜色值：#FF9100
    直径：44.13倍太阳直径

中文名毕宿五
外文名Aldebaran
别    名金牛座α
分    类红巨星
质    量约 1.16 M⊙
表面温度约 3900 K
视星等0.85 等
绝对星等约 -0.641 等
自转周期~520 d
赤    经4时35分55.24秒
赤    纬+16°30′33.49″
距地距离约 65.3 光年
半    径44.13±0.84 R☉
光谱类型K5+III变星类型慢不规则变星径向速度54.26±0.03 km/s视    差49.97±0.75 mas表面重力1.45±0.3光    度439±17 L☉金属量-0.33±0.1 dex自转速度3.5±1.5 km/sU−B 色指数1.92B−V 色指数1.44年    龄6.4 Gyr

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
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.019,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    from bodies import Sun
    import math
    fixed_star = Aldebaran()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)
    r = 44.13
    print("密度換算", fixed_star.mass / 1e9 / (4 / 3 * math.pi * pow(r * sun.raduis, 3)))
