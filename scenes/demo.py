# -*- coding:utf-8 -*-
# title           :太阳、地球模拟运行
# description     :太阳、地球模拟运行（演示案例）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY
from scenes.func import mayavi_run, mpl_run, ursina_run
from bodies.body import Body, AU

if __name__ == '__main__':
    """
    太阳、地球模拟运行
    """
    # 构建两个天体对象（太阳、地球）
    bodies = [
        # 太阳的质量为 1.9891×10³⁰ kg
        # 初始位置 x=0, y=0, z=0
        # 初始速度 x=0, y=0, z=0
        # 纹理图片路径为 texture/douyin.jpg
        # 放大倍数为 120 倍
        # 距离保持不变
        Sun(name="太阳", mass=1.9891e30,
            init_position=[0, 0, 0],
            init_velocity=[0, 0, 0],
            texture="douyin.jpg", size_scale=1.2e2, distance_scale=1.0),

        # 地球的质量为 5.97237✕10²⁴ kg
        # 初始位置 x=1.12天文单位, y=0, z=0
        # 初始速度 x=0, y=29.7929.79 km/s, z=0
        # 纹理图片路径为 texture/pythoncr.jpg
        # 放大倍数为 5000 倍
        # 距离保持不变
        Earth(name="地球", mass=5.97237e24,
              init_position=[1.12 * AU, 0, 0],
              init_velocity=[0, 29.79, 0],
              texture="pythoncr.jpg", size_scale=5e3, distance_scale=1.0),
    ]
    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_DAY, view_azimuth=135)

    # 使用 matplotlib 查看运行效果
    # mpl_run(bodies, SECONDS_PER_WEEK)

    # 使用 ursina 查看的运行效果
    ursina_run(bodies, SECONDS_PER_WEEK, position=(0, 0, 0))
