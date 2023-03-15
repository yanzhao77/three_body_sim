# -*- coding:utf-8 -*-
# title           :太阳系场景模拟2
# description     :太阳系场景模拟（展示的效果非太阳系真实的距离和大小）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Asteroids
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY, SECONDS_PER_MONTH, SECONDS_PER_YEAR
from scenes.func import mayavi_run, ursina_run

if __name__ == '__main__':
    # 八大行星：木星(♃)、土星(♄)、天王星(♅)、海王星(♆)、地球(⊕)、金星(♀)、火星(♂)、水星(☿)
    # 排列顺序
    # 1、体积：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 1330：745：65：60：1：0.86：0.15：0.056
    # 2、质量：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 318：95：14.53：17.15：1：0.8：0.11：0.0553
    # 3、离太阳从近到远的顺序：水星、金星、地球、火星、木星、土星、天王星、海王星
    #  =====================================================================
    #  以下展示的效果非太阳系真实的距离和大小
    #  1、由于宇宙空间尺度非常大，如果按照实际的天体大小，则无法看到天体，因此需要对天体的尺寸进行放大
    #  2、为了达到最佳的显示效果，对每个行星天体的距离进行了缩放

    # region 构建太阳系
    bodies = [
        Sun(size_scale=0.8e2),                              # 太阳放大 80 倍
        Mercury(size_scale=4e3, distance_scale=1.3),        # 水星放大 4000 倍，距离放大 1.3 倍
        Venus(size_scale=4e3, distance_scale=1.3),          # 金星放大 4000 倍，距离放大 1.3 倍
        Earth(size_scale=4e3, distance_scale=1.3),          # 地球放大 4000 倍，距离放大 1.3 倍
        Asteroids(size_scale=3e2),  # 小行星模拟
        Mars(size_scale=4e3, distance_scale=1.3),           # 火星放大 4000 倍，距离放大 1.3 倍
        Jupiter(size_scale=0.68e3, distance_scale=0.65),    # 木星放大 680 倍，距离缩小到真实距离的 0.65
        Saturn(size_scale=0.68e3, distance_scale=0.52),     # 土星放大 680 倍，距离缩小到真实距离的 0.52
        Uranus(size_scale=0.8e3, distance_scale=0.36),      # 天王星放大 800 倍，距离缩小到真实距离的 0.36
        Neptune(size_scale=1e3, distance_scale=0.27),       # 海王星放大 1000 倍，距离缩小到真实距离的 0.27
        Pluto(size_scale=10e3, distance_scale=0.23),        # 冥王星放大 10000 倍，距离缩小到真实距离的 0.23(从太阳系的行星中排除)
    ]
    # endregion

    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45, view_distance=3e9, view_focalpoint=[5e2, 5e2, 5e2])

    # 使用 ursina 查看的运行效果
    ursina_run(bodies, SECONDS_PER_WEEK, position=(0, 0, 0))