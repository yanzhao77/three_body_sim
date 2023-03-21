# -*- coding:utf-8 -*-
# title           :恒星演示
# description     :恒星演示
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth, Sirius, Rigel, Alcyone, Antares, Arcturus, Betelgeuse, Stephenson_2_18
from common.consts import SECONDS_PER_WEEK, SECONDS_PER_MONTH, SECONDS_PER_YEAR, SECONDS_PER_DAY
from scenes.func import mayavi_run, mpl_run, ursina_run
from bodies.body import Body, AU

if __name__ == '__main__':
    """
    恒星演示
    """
    # 构建两个天体对象（太阳、地球）
    D = 5e5
    SIZE_SCALE = 0.02
    bodies = [
        Earth(size_scale=1, init_velocity=[0, 29.79, 0], distance_scale=0.0006),
        Sun(size_scale=SIZE_SCALE),
        Sirius(size_scale=SIZE_SCALE, ignore_mass=True),
        Alcyone(size_scale=SIZE_SCALE, ignore_mass=True),
        Arcturus(size_scale=SIZE_SCALE, ignore_mass=True),
        Rigel(size_scale=SIZE_SCALE, ignore_mass=True),
        Antares(size_scale=SIZE_SCALE, ignore_mass=True),
        # Betelgeuse(size_scale=SIZE_SCALE, ignore_mass=True),
        Stephenson_2_18(size_scale=SIZE_SCALE, ignore_mass=True)
    ]
    distance_sum = 0
    for idx, body in enumerate(bodies):
        body.rotation_speed /= 50
        if idx > 1:
            body.light_on = False  # 关闭灯光效果，只有太阳对地球有灯光效果
            d = pow((body.diameter + bodies[idx - 1].diameter) * SIZE_SCALE, 0.75) * 120
            # d = (body.diameter + bodies[idx - 1].diameter) * SIZE_SCALE * 1.1 + D
            body.init_position = [(distance_sum + d) / 2, (distance_sum + d), 0]
            distance_sum += d

    # 使用 ursina 查看的运行效果
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    # position = 左-右+、上+下-、前+后-
    ursina_run(bodies, SECONDS_PER_MONTH, position=(0, 10, -4 * AU / 200))
