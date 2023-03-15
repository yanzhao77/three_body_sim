# -*- coding:utf-8 -*-
# title           :太阳、地球场景模拟
# description     :太阳、地球场景模拟
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY
from scenes.func import mayavi_run, ursina_run

if __name__ == '__main__':
    """
    太阳、地球
    """
    bodies = [
        Sun(size_scale=5e1),                      # 太阳放大 50 倍
        Earth(size_scale=2e3, distance_scale=1),  # 地球放大 2000 倍，距离保持不变
    ]

    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)

    # 使用 ursina 查看的运行效果
    ursina_run(bodies, SECONDS_PER_WEEK, position=(0, 0, 0))
