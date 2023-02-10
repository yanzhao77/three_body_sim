# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth
from common.consts import SECONDS_PER_WEEK
from scenes.func import mayavi_run

if __name__ == '__main__':
    """
    太阳、地球
    """
    bodies = [
        Sun(size_scale=1.2e2),                    # 太阳放大 120 倍
        Earth(size_scale=2e3, distance_scale=1),  # 地球放大 2000 倍，距离保持不变
    ]
    mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)
