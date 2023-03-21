# -*- coding:utf-8 -*-
# title           :三体场景模拟01
# description     :三体场景模拟（3个太阳、1个地球）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth, FixedStar
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY, AU, SECONDS_PER_MONTH, SECONDS_PER_YEAR
from scenes.func import mayavi_run, ursina_run

if __name__ == '__main__':
    """
    3个太阳、1个地球（效果1）
    可以修改影响效果的参数为： 
    1、三个方向的初始位置 init_position[x, y, z]
    2、三个方向的初始速度 init_velocity[x, y, z]
    3、天体质量 mass    
    """
    import math

    mass = 2e30
    r = 2 * AU
    # p = 12  # 三体转圆形花
    p = 14.88  # 三体转圈近似圆形
    # p = 16  # 三体转圆形花
    # p = 18  # 三体转圆形花
    # p = 19  # 三体转圆形花
    bodies = [
        Sun(name="红轨太阳A", mass=mass,
            init_position=[0, math.sqrt(3) * r, 0],
            init_velocity=[-p, 0, 0],
            color=(255, 0, 0),
            size_scale=5e1, texture="sun2.jpg"),  # 太阳放大 100 倍
        Sun(name="绿轨太阳B", mass=mass,
            init_position=[-r, 0, 0],
            init_velocity=[1 / 2 * p, -math.sqrt(3) / 2 * p, 0],
            color=(0, 255, 0),
            size_scale=5e1, texture="sun2.jpg"),  # 太阳放大 100 倍
        Sun(name="蓝轨太阳C", mass=mass,
            init_position=[r, 0, 0],
            init_velocity=[1 / 2 * p, math.sqrt(3) / 2 * p, 0],
            color=(0, 0, 255),
            size_scale=5e1, texture="sun2.jpg"),  # 太阳放大 100 倍
        # Earth(init_position=[0, -349597870.700, 0],
        #       init_velocity=[15.50, 0, 0],
        #       size_scale=4e3, distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    ]
    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=0)

    # 使用 ursina 查看的运行效果
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    # position = 左-右+、上+下-、前+后-
    ursina_run(bodies, SECONDS_PER_YEAR, position=(3 * AU, AU, -4 * AU))
