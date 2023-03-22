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


class Bellatrix(FixedStar):
    """
    TODO： 参宿五 (Bellatrix)
    质量：8.6太阳质量
    密度：1.16×10⁻⁴ g/cm³
    颜色值：#FF9100
    直径：5.75倍太阳直径

    中文名参宿五
    外文名Bellatrix别    名猎户座γ
    分    类恒星
    质    量8.6 M⊙
    表面温度22000 K
    视星等1.64 等
    绝对星等-2.78 等
    赤    经5时25分07.9秒
    赤    纬+6°20′58.93″
    距地距离约 250 光年
    光谱类型B2 III
    径向速度18.2 km/s
    视    差12.92±0.52 mas
    半    径5.75 R☉
    表面重力3.6 cgs
    光    度9,211 L☉
    金属量–0.07 dex
    自转速度46±8 km/s
    U−B 色指数-0.86
    B−V 色指数-0.21
    年    龄25.2 Myr
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="参宿五", mass=8.6 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(122, 187, 255),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.5, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 63.69,
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

    fixed_star = Bellatrix()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)
