# -*- coding:utf-8 -*-
# title           :心宿二
# description     :心宿二
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar, Sun
from common.consts import MO


class EtaCarinae(FixedStar):
    """
    TODO： 海山二/船底座（Eta Carinae）
    质量：100 太阳质量
    大小：500 太阳半径
    颜色：0xFF, 0xD7, 0x00
    密度：0.002 g/cm³

    中文名海山二/船底座 η 星外文名Eta Carinae别    名Eta Car / η Carinae / η Car分    类A：高光度蓝变星 B：主序星发现者爱德蒙·哈雷发现时间1677年质    量100 M⊙(B：50-80M)直    径386809200 km(B:33 393 600Km)表面温度A：9400 ~ 35200 K B：37200 K视星等约 4.3 等(-0.8至7.9)绝对星等-8.6 等赤    经10时45分03.59秒赤    纬-59°41′04.26″距地距离7500 ly（2300 pc）半长轴15.4 AU离心率0.9公转周期2,022.7 ± 1.3 days（5.54 yr）轨道倾角130 ~ 145°光谱型A：LBV B：OU-B 色指数-0.45B-V 色指数+0.61光    度A：5 × 10^6 L☉ B：10^6 L☉

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="海山二", mass=100 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0xD7, 0x00),
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
    fixed_star = EtaCarinae()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)