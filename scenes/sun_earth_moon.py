# -*- coding:utf-8 -*-
# title           :地月场景模拟
# description     :地月场景模拟
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth, Moon
from common.consts import SECONDS_PER_HOUR, SECONDS_PER_HALF_DAY, SECONDS_PER_DAY, SECONDS_PER_WEEK, SECONDS_PER_MONTH
from scenes.func import mayavi_run, ursina_run
from bodies.body import AU

if __name__ == '__main__':
    """
    地球、月球
    """
    # 地球的Y方向初始速度
    EARTH_INIT_VELOCITY = 0  # 0km/s
    sun = Sun(init_position=[AU, 0, 0], size_scale=2e1)  # 太阳放大 20 倍
    # 忽略质量的引力
    sun.ignore_mass = True
    bodies = [
        sun,
        Earth(init_position=[0, 0, 0],
              init_velocity=[0, EARTH_INIT_VELOCITY, 0],
              size_scale=1e1),  # 地球放大 10 倍，距离保持不变
        Moon(init_position=[0, 384400, 0],  # 距地距离约: 363104 至 405696 km
             init_velocity=[-1.023, EARTH_INIT_VELOCITY, 0],
             size_scale=2e1)  # 月球放大 20 倍，距离保持不变
    ]
    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_HALF_DAY / 2, view_azimuth=-45)

    # 使用 ursina 查看的运行效果
    ursina_run(bodies, SECONDS_PER_DAY, position=(0, 0, 0))
