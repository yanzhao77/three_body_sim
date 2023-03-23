# -*- coding:utf-8 -*-
# title           :太阳系场景模拟1
# description     :太阳系场景模拟（展示的效果为太阳系真实的距离）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Moon, Asteroids
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY, SECONDS_PER_YEAR, AU
from scenes.func import mayavi_run, ursina_run

if __name__ == '__main__':
    # 八大行星：木星(♃)、土星(♄)、天王星(♅)、海王星(♆)、地球(⊕)、金星(♀)、火星(♂)、水星(☿)
    # 排列顺序
    # 1、体积：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 1330：745：65：60：1：0.86：0.15：0.056
    # 2、质量：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 318：95：14.53：17.15：1：0.8：0.11：0.0553
    # 3、离太阳从近到远的顺序：水星、金星、地球、火星、木星、土星、天王星、海王星
    #  =====================================================================
    #  以下展示的效果为太阳系真实的距离
    #  由于宇宙空间尺度非常大，如果按照实际的天体大小，则无法看到天体，因此需要对天体的尺寸进行放大
    sun = Sun(name="太阳", size_scale=0.8e2)       # 太阳放大 80 倍，距离保持不变
    # sun.init_velocity = [0, 0, 2]                # 太阳带着其他行星一起跑
    bodies = [
        sun,
        Mercury(name="水星", size_scale=4e3),      # 水星放大 4000 倍，距离保持不变
        Venus(name="金星", size_scale=4e3),        # 金星放大 4000 倍，距离保持不变
        Earth(name="地球", size_scale=4e3),        # 地球放大 4000 倍，距离保持不变
        Mars(name="火星", size_scale=4e3),         # 火星放大 4000 倍，距离保持不变
        Asteroids(name="小行星群", size_scale=3.2e2,
                  parent=sun),                     # 小行星群模拟(仅 ursina 模拟器支持)
        Jupiter(name="木星", size_scale=0.8e3),    # 木星放大 800 倍，距离保持不变
        Saturn(name="土星", size_scale=0.8e3),     # 土星放大 800 倍，距离保持不变
        Uranus(name="天王星", size_scale=0.8e3),   # 天王星放大 800 倍，距离保持不变
        Neptune(name="海王星", size_scale=1e3),    # 海王星放大 1000 倍，距离保持不变
        Pluto(name="冥王星", size_scale=10e3),     # 冥王星放大 10000 倍，距离保持不变(从太阳系的行星中排除)
    ]

    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)

    # 使用 ursina 查看的运行效果
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    # position = 左-右+、上+下-、前+后-
    ursina_run(bodies, SECONDS_PER_YEAR, position=(0, 2 * AU, -11 * AU), bg_music="../sounds/universe_04.mp3")
