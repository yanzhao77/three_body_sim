# -*- coding:utf-8 -*-
# title           :北河三
# description     :北河三
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar, Sun
from common.consts import MO


class PolluxB(FixedStar):
    """
    TODO： 北河三b (Pollux b)
    质量：1.5太阳质量
    密度：1.8 g/cm³
    颜色值：#F5E8D5
    直径：1.84倍太阳直径

    中文名北河三b外文名Pollux b
β Gem b别    名HD 62509 b、Thestias分    类系外行星发现者亚提·瀚兹(等人)发现时间2006年质    量2.3 MJ(至少)距地距离33.78 光年 [2] 半长轴1.64 AU离心率0.02公转周期589.64 ± 0.81 天

一、北河三比太阳大多少，77.4个太阳
北河三，亮度为太阳的43倍，是目前发现的全天第17亮星（夜晚最亮的是大犬座的天狼星，典型的蓝矮星）。因为北河三非常亮，所以经常有人把它与太阳相比较，至于北河三比太阳大多少？据小编查询，北河三质量是太阳的1.86倍，半径是太阳的8.8倍，体积是太阳的77.4倍。

二、北河三有多大，红巨星中较小
太阳是恒星，北河三为红巨星，所以北河三比太阳大很多。不过在红巨星中，北河三又成了较小的存在，多数亮巨星超巨星都比他大。比如星心宿二是颗红超巨星，直径达到太阳的700倍；参宿七是颗蓝超巨星，直径约为太阳77倍。类似的恒星还很多，北河三并不算大。

    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="北河三b", mass=1.5 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xF5, 0xE8, 0xD5),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.5e3,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = PolluxB()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)