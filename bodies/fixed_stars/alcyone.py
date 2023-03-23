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


class Alcyone(FixedStar):
    """
    昴宿六 (Alcyone)
    --------------- 维基百科 ---------------
    昴宿六
    观测资料
    观测资料
    历元 J2000
    星座	金牛座
    星官	昴宿 昴
    赤经	03h 47m 29.077s
    赤纬	24° 06′ 18.49″
    视星等（V）	2.87
    特性
    光谱分类	B7IIIe
    U−B 色指数	−0.34
    B−V 色指数	−0.09
    天体测定
    径向速度 (Rv)	5.40 km/s
    自行 (μ)	赤经：19.34 ± 0.39 mas/yr
    赤纬：-43.67 ± 0.33 mas/yr
    视差 (π)	8.09 ± 0.42 mas
    距离	440 ly
    绝对星等 (MV)	-2.8
    详细资料
    质量	6 M☉
    半径	9 R☉
    亮度	2,100 L☉
    温度	13,000 K
    自转速度 (v sin i)	149 km/s

    昴宿六（η Tau/金牛座η）西方星名为Alcyone，是一个在金牛座的聚星系统。
    距离太阳大约440光年，为昴宿星团中最明亮的一颗恒星，该星团很年轻，年龄大约1亿年。
    还有数颗暗淡的恒星很靠近昴宿六，很可能都是星团的成员。

    神话
    西方星名Alcyone是由希腊神话来的，即阿尔克俄涅，她是阿特拉斯和普勒俄涅的七个女儿之一。

    恒星系统
    双星和聚星星表列出了它的3个伴星：
    B是金牛座24，视星等6.28的A0主序星，距离117"；
    C是金牛座V647，是盾牌座δ型变星；
    D是视星等9.15的F3主序星。
    金牛座V647的变光幅度在+8.25到+8.30，周期1.13小时。

    华盛顿双星目录列出了4个更暗的伴星，全都在11等以下，另外也表示伴星D本身也是个联星，2个几乎一样的成员分离0.30"。

    主星，昴宿六A，包含了3个成员，最亮的是蓝白色的B型巨星，和其他昴星团的亮星相似。
    视星等+2.87（绝对星等-2.8），将近9太阳半径。
    大约13,000K的表面温度使他有2100倍太阳光度。
    光谱类型B7IIIe代表在光谱里有发射线。像众多的Be星,昴宿六A自转速度是很高的149km/s，造成了环绕恒星赤道气体盘。

    最近的伴星质量非常低，并且距离小于1毫角秒，轨道周期可能略大于4天。
    另外一个恒星大约有蓝巨星质量的一半，分离0.031角秒，大约是太阳到木星的距离，轨道周期大约830天。
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="昴宿六", mass=6 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xBB, 0xAA, 0xFF),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.45, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 9.85333138941539,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Alcyone()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=9.5)
