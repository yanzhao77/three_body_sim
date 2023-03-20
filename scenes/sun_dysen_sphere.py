# -*- coding:utf-8 -*-
# title           :太阳、地球场景模拟
# description     :太阳、地球场景模拟
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, DysenSphere
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY, AU
from scenes.func import mayavi_run, ursina_run

if __name__ == '__main__':
    """
    太阳、戴森球
    """

    sun = Sun(size_scale=5e1, init_velocity=[0, 2, 0])  # 太阳放大 50 倍
    bodies = [
        sun,
        DysenSphere(size_scale=5e1, parent=sun),  # 戴森球放大 50 倍
    ]

    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)

    # 使用 ursina 查看的运行效果
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    # position = 左-右+、上+下-、前+后-
    ursina_run(bodies, SECONDS_PER_WEEK, position=(0, AU / 2, -3 * AU))
