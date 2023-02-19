# -*- coding:utf-8 -*-
# title           :三体场景模拟02
# description     :三体场景模拟（3个太阳、1个地球）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from mayavi import mlab
from bodies import Sun, Earth
from common.consts import SECONDS_PER_WEEK
from scenes.func import mayavi_run, mpl_run

if __name__ == '__main__':
    """
    注释： 3个太阳（ChatGPT生成的效果）
    可以修改影响效果的参数为： 
    1、三个方向的初始位置 init_position[x, y, z]
    2、三个方向的初始速度 init_velocity[x, y, z]
    3、天体质量 mass    
    """
    # 代码案例如下：
    SIZE_SCALE = 5e1  # 生成的太阳放大 50 倍
    RUN_DIAMETER = 1.392e6  # 真实太阳的直径
    bodies = [
        Sun(name="太阳1", mass=2.5e30, init_position=[100 * RUN_DIAMETER, 200 * RUN_DIAMETER, 300 * RUN_DIAMETER],
            init_velocity=[-12.5, -12.0, 11.5],
            size_scale=SIZE_SCALE, texture="sun1.jpg"),
        Sun(name="太阳2", mass=2e30, init_position=[-150 * RUN_DIAMETER, 250 * RUN_DIAMETER, 350 * RUN_DIAMETER],
            init_velocity=[11.5, 12.0, 12.5],
            size_scale=SIZE_SCALE, texture="sun2.jpg"),
        Sun(name="太阳3", mass=2.8e30, init_position=[200 * RUN_DIAMETER, -300 * RUN_DIAMETER, 400 * RUN_DIAMETER],
            init_velocity=[-11.5, -12.5, -12.0],
            size_scale=SIZE_SCALE, texture="sun2.jpg"),
    ]

    # 按照以上代码案例格式生成代码，要求 init_position 、init_velocity、mass 生成后，要保证在万有引力的作用下，能正常运行，不会碰撞
    """
太阳1：

    初始位置：(100000, 200000, 300000) km
    初始速度：(-1.0, -2.0, 3.0) km/s
    质量：2.5 x 10^30 kg

太阳2：

    初始位置：(-150000, 250000, 350000) km
    初始速度：(2.0, -3.0, -1.0) km/s
    质量：2.0 x 10^30 kg

太阳3：

    初始位置：(200000, -300000, 400000) km
    初始速度：(-3.0, 1.0, -2.0) km/s
    质量：2.8 x 10^30 kg
    """
    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=0)
    mpl_run(bodies, SECONDS_PER_WEEK)
