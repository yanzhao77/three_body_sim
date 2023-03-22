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


class UYScuti(FixedStar):
    """
    盾牌座 UY (UY Scuti)
    质量：10个太阳质量
    密度：不详
    颜色值：#EFF6FF
    直径：为1708±192倍太阳直径

中文名盾牌座 UY外文名UY Scuti
别    名UY Sct、BD−12°5055、IRC−10422、RAFGL 2162、HV 3805
分    类红超巨星发现时间1860年
质    量7 至 10 M⊙(有争议)
直    径2.376✕109 km(±0.268)表面温度3365 K(±134)视星等+8.29 ~ +10.56绝对星等-6.2 等 [1] 赤    经18时27分36.53秒赤    纬-12°27′58.86″距地距离9500 光年(±1030, 有争议) [1] 光谱类别M2-M4Ia-IabU-B 色指数+3.29 [2] B-V 色指数+3.00 [3] 变星类型SRc（半规则） [4] 光    度约340000 L⊙（有争议）半    径1708±192 R☉（有争议）表面重力加速度0.008 m/s²表面重力-0.5 cgs [2] 赤道自转线速度约1.95 km/s径向速度18.33±0.82 km/s [5] 视    差0.6433±0.1059 mas（有争议） [5] 自    行赤经: 1.3 mas/yr; 赤纬: −1.6 mas/yr

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="盾牌座UY", mass=10 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(255,116,0),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 2.832e-06,
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

    fixed_star = UYScuti()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)
    r = 1708
    print("密度換算", fixed_star.mass / 1e9 / (4 / 3 * math.pi * pow(r * sun.raduis, 3)))

    # print( "%s" % (2.376e9 / (sun.raduis*2)))