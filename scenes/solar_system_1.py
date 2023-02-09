# -*- coding:utf-8 -*-
# title           :太阳系场景
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon
from common.consts import SECONDS_PER_WEEK
from scenes.func import mayavi_run

if __name__ == '__main__':
    # 八大行星：木星(♃)、土星(♄)、天王星(♅)、海王星(♆)、地球(⊕)、金星(♀)、火星(♂)、水星(☿)
    # 排列顺序
    # 1、体积：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 1330：745：65：60：1：0.86：0.15：0.056
    # 2、质量：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 318：95：14.53：17.15：1：0.8：0.11：0.0553
    # 3、离太阳从近到远的顺序：水星、金星、地球、火星、木星、土星、天王星、海王星
    #  =====================================================================
    #  以下展示的效果为太阳系真实的距离
    #  但是由于宇宙空间尺度非常大，按照实际的大小无法看到行星天体，因此需要对天体的尺寸进行放大
    bodies = [
        Sun(size_scale=1.2e2),      # 太阳放大 120 倍，距离保持不变
        Mercury(size_scale=4e3),    # 水星放大 4000 倍，距离保持不变
        Venus(size_scale=4e3),      # 金星放大 4000 倍，距离保持不变
        Earth(size_scale=4e3),      # 地球放大 4000 倍，距离保持不变
        Mars(size_scale=4e3),       # 火星放大 4000 倍，距离保持不变
        Jupiter(size_scale=1e3),    # 木星放大 1000 倍，距离保持不变
        Saturn(size_scale=1e3),     # 土星放大 1000 倍，距离保持不变
        Uranus(size_scale=1e3),     # 天王星放大 1000 倍，距离保持不变
        Neptune(size_scale=1e3),    # 海王星放大 1000 倍，距离保持不变
        Pluto(size_scale=10e3),     # 冥王星放大 10000 倍，距离保持不变(从太阳系的行星中排除)
    ]
    mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)
