# -*- coding:utf-8 -*-
# title           :地月场景模拟（观看月相变化的过程）
# description     :地月场景模拟（观看月相变化的过程）
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

    # 观看月相变化的过程：分别是 新月、蛾眉月、上弦月、盈凸、满月、亏凸、下弦月、残月
    # 参考：images/moon/月相变化过程.jpeg
    # TODO: 月球在摄像机的前方（从 “新月” 开始）
    moon_pos, moon_vel = [384400, 0, 0], [0, EARTH_INIT_VELOCITY + 1.023, 0]
    # TODO: 月球在摄像机的右方（从 “下弦月” 开始），将会出现
    # moon_pos, moon_vel = [0, -384400, 0], [1.023, EARTH_INIT_VELOCITY, 0]
    # TODO: 月月球在摄像机的左方（从 “上弦月” 开始）
    # moon_pos, moon_vel = [0, 384400, 0], [-1.023, EARTH_INIT_VELOCITY, 0]

    bodies = [
        sun,
        Earth(init_position=[0, 0, 0],
              init_velocity=[0, EARTH_INIT_VELOCITY, 0],
              size_scale=1e1),        # 地球放大 10 倍，距离保持不变
        Moon(init_position=moon_pos,  # 距地距离约: 363104 至 405696 km
             init_velocity=moon_vel,
             size_scale=2e1)          # 月球放大 20 倍，距离保持不变
    ]
    # 使用 ursina 查看的运行效果
    # position = 左-右+、上+下-、前+后-
    # position=(0, 0, 0) 的位置是站在地球视角，可以观看月相变化的过程
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    ursina_run(bodies, SECONDS_PER_DAY, position=(0, 0, 0), save_as_json="../data/sun_earth_moon.json")

    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_HALF_DAY / 2, view_azimuth=-45)
