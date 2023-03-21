# -*- coding:utf-8 -*-
# title           :恒星演示
# description     :恒星演示
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Sirius, Stephenson_2_18
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY
from scenes.func import mayavi_run, mpl_run, ursina_run
from bodies.body import Body, AU

if __name__ == '__main__':
    """
    恒星演示
    """
    # 构建两个天体对象（太阳、地球）
    bodies = [
        Sun(size_scale=1, init_position=[0, 0, 0]),
        Sirius(size_scale=1, init_position=[0, 2 * AU, 0]),
        Stephenson_2_18(size_scale=1, init_position=[0, 3 * AU, 0])
    ]

    # 使用 ursina 查看的运行效果
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    # position = 左-右+、上+下-、前+后-
    ursina_run(bodies, SECONDS_PER_WEEK, position=(0, AU, -5 * AU), ignore_mass=True)
