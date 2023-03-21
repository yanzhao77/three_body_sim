# -*- coding:utf-8 -*-
# title           :天狼星
# description     :天狼星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Sirius(FixedStar):
    """
    天狼星A (Sirius)
    质量：2.06太阳质量
    密度：2.6 g/cm³ TODO: 0.58 kg/m³ ???
    颜色值：#FFF0E4
    直径：1.71倍太阳直径 TODO:

    中文名: 天狼星
    外文名: Sirius
    别名： α Canis Majoris A/ α CMa A
    分类： A：主序星 B：白矮星
    质量： A：2.063 ± 0.023 M⊙ B：1.018 ± 0.011 M⊙
    密度： B：10^8 ～ 10^10 kg/m³
    直径： A：1.711 D⊙  B：0.0084 ± 0.03 D⊙
    表面温度： A：9940 K B：25000 ± 200 K
    逃逸速度：671 km/s
    视星等： A：-1.47 B：+8.44 System：-1.46
    绝对星等：  A：+1.42 B：+11.18自转周期44.5天
    赤经： System：06h 45m 08.91728s
    赤纬： System：-16° 42′ 58.0171″
    距地距离： System：8.60 ± 0.04 ly（2.64 ± 0.01 pc）
    半长轴： 7.4957 ± 0.0025″
    离心率： 0.59142 ± 0.00037
    公转周期： 50.1284 ± 0.0043 yr
    平近点角： 149.161 ± 0.075°
    轨道倾角： 136.336 ± 0.040°升
    交点经度： 45.40 ± 0.071°
    光谱型： A：A0mA1Va B：DA2U-B
    色指数： A：-0.05 B：-1.04B-V
    色指数： A：+0.00 B：-1.03
    光度： A：25.4 L☉ B：0.056 L☉
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="天狼星A", mass=2.06 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0xFF, 0xFF),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.58e3,
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
    fixed_star = Sirius()
    sun = Sun()
    print(fixed_star)
    print(sun)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)
