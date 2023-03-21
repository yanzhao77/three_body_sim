# -*- coding:utf-8 -*-
# title           :心大星
# description     :心大星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar, Sun
from common.consts import MO


class Antares(FixedStar):
    """
    TODO： 心宿二，英文名为Antares
    质    量A：12 ± 0.2 M⊙ B：7.2 M⊙
    半    径A:680–800 R☉；B:5.2 R☉
    A：红超巨星 B：蓝矮星
    质量：为18.6太阳质量
    大小：为883太阳半径
    颜色：为0xFF, 0x44, 0x00
    密度：为0.0037 g/cm³。


    中文名心宿二外文名Antares别    名Alpha Scorpii分    类A：红超巨星 B：蓝矮星质    量A：12 ± 0.2 M⊙ B：7.2 M⊙表面温度A：3570 K B：18500 K视星等A：0.6 ～ 1.6 B：5.5绝对星等-5.28 等 [9] 赤    经16时29分24.46秒赤    纬-26°25′55.21″距地距离550 ly（170 pc）U-B 色指数A：M1.5Iab-Ib B：B2.5VB-V 色指数+1.83光    度A:75,900 L☉ (44,700 – 128,900 L☉)；B:2754 L☉ [9] 变星类型Lc半    径A:680–800 R☉；B:5.2 R☉ [9] 拼    音xīn xiù èr

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="心宿二", mass=18.6 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0x44, 0x00),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.0037e3,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Antares()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)