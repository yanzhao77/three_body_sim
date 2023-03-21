# -*- coding:utf-8 -*-
# title           :大犬座VY
# description     :大犬座VY
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar, Sun
from common.consts import MO


class CanisMajorisVY(FixedStar):
    """
    TODO： 大犬座VY（VY Canis Majoris）
    质量：30.0 太阳质量
    大小：1420 太阳半径
    颜色：0xFF, 0x8D, 0x29
    密度：0.0004 g/cm³

    平均密度5.33✕10-3 至 8.38✕10-3 g/m³  0.00533
     恒星质量17±8 M☉ [1]
     半    径2,069 R☉ [1]  [12-13]

    中文名大犬座VY外文名VY Canis Majoris别    名VY CMa分
    类红特超巨星发现者杰罗姆·拉朗德发现时间1801年3月7日平均密度5.33✕10-3 至 8.38✕10-3 g/m³
    表面温度3490 K(±90)视星等6.5 至 9.6 等赤    经07时22分58.33秒赤    纬-25°46′03.24″
    距地距离3820 光年(+260 −230)光谱型M3-M4.5（M2.5-M5e Ia） [1-3]
    视星等（U）12.01 [4] 视星等（B）10.19 [4] 视星等（V）7.95 [4] 视星等（J）1.98 [4]
    视星等（H）0.44 [4] 视星等（K）8.1 [5] U-B色指数+2.32 [6] B-V色指数+2.057 [7] V-R色指数+2.20 [6]
    变星类型SRc或Lc [8-9]  径向速度41 km/s [10] 自
    行赤经：9.84 mas/yr 赤纬：0.75 mas/yr [7] 视    差0.83±0.08 mas [11]
    距    离1,170（+80或-70）pc，3,820（+260或-230）ly [1] 绝对热星等-9.4


    热光度270,000±40,000，178,000（+40,900或-29,900）L☉ [12-14]
     表面重力-0.6±0.4 cgs [1] 有效温度3,940±90 K [1] 金属丰度[Fe/H]-0.3 dex [15] 自转速度300 km/s [11]
     年    龄8.2 Myr [11]
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="大犬座VY", mass=30 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0x5B, 0x5B),
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
    fixed_star = CanisMajorisVY()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)