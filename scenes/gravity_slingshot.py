# -*- coding:utf-8 -*-
# title           :引力弹弓模拟演示
# description     :引力弹弓模拟演示
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
    太阳、地球
    """
    bodies = [
        Sun(size_scale=2e1),    # 太阳放大 20 倍
        Earth(size_scale=1e3,   # 地球放大 1000 倍
              init_position=[0, -3 * AU, 0],  # 地球距离太阳 3 个天文单位
              # TODO: 尝试调整朝向太阳的速度，取值 33、38、50 或者其他
              # init_velocity=[0, 33, -1],
              init_velocity=[0, 38, -1],  # 朝向太阳的速度为 38km/s，-1 km/s 是为了防止地球正面对着太阳冲去
              # init_velocity=[0, 50, -1],
              ),
    ]

    # 使用 mayavi 查看的运行效果
    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)

    # 使用 ursina 查看的运行效果
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    # position = 左-右+、上+下-、前+后-
    ursina_run(bodies, SECONDS_PER_MONTH, position=(0, AU, -3 * AU), show_trail=True)
