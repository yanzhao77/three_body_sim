# -*- coding:utf-8 -*-
# title           :太阳、地球、木星场景模拟
# description     :太阳、地球、木星场景模拟
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth, Jupiter
from common.consts import SECONDS_PER_WEEK
from scenes.func import mayavi_run

if __name__ == '__main__':
    """
    太阳、地球、木星
    """
    bodies = [
        Sun(size_scale=1.2e2),                        # 太阳放大 120 倍
        Earth(size_scale=4e3, distance_scale=1),      # 地球放大 4000 倍，距离保持不变
        Jupiter(size_scale=1e3, distance_scale=0.5),  # 木星放大 1000 倍，距离缩小到真实距离的 0.5
    ]
    mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)
