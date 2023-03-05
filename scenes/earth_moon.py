# -*- coding:utf-8 -*-
# title           :地月场景模拟
# description     :地月场景模拟
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth, Moon
from common.consts import SECONDS_PER_HOUR, SECONDS_PER_HALF_DAY, SECONDS_PER_DAY, SECONDS_PER_WEEK
from scenes.func import mayavi_run, ursina_run
from bodies.body import AU

if __name__ == '__main__':
    """
    地球、月球
    """
    # 地球的Y方向初始速度
    EARTH_INIT_VELOCITY = 0.2  # 200m/s
    bodies = [
        Earth(init_position=[0, 0, 0],
              init_velocity=[0, EARTH_INIT_VELOCITY, 0], size_scale=1e1),  # 地球放大 10 倍，距离保持不变
        Moon(init_position=[363104, 0, 0],
             init_velocity=[0, EARTH_INIT_VELOCITY + 1.023, 0], size_scale=1e1)  # 月球放大 10 倍，距离保持不变
    ]
    mayavi_run(bodies, SECONDS_PER_HALF_DAY / 2, view_azimuth=-45)

    # 使用 ursina 查看的运行效果
    # ursina_run(bodies, SECONDS_PER_DAY, position=(0, 0, 0))