# -*- coding:utf-8 -*-
# title           :恒星演示
# description     :恒星演示
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Earth, Sirius, Rigel, Bellatrix, Alcyone, Antares, Arcturus, Aldebaran, Betelgeuse
from bodies import VYCanisMajoris, UYScuti, Stephenson_2_18
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
        Sun(size_scale=SIZE_SCALE),  # 太阳
        Sirius(size_scale=SIZE_SCALE, ignore_mass=True),  # 天狼星A    质量倍数 2.06   半径倍数 1.71
        Bellatrix(size_scale=SIZE_SCALE, ignore_mass=True),  # 参宿五  质量倍数 8.6    半径倍数 5.75
        Alcyone(size_scale=SIZE_SCALE, ignore_mass=True),  # 昴宿六    质量倍数 7      半径倍数 10
        Arcturus(size_scale=SIZE_SCALE, ignore_mass=True),  # 大角星   质量倍数 1.08   半径倍数 25.42
        Aldebaran(size_scale=SIZE_SCALE, ignore_mass=True),  # 毕宿五  质量倍数 1.16   半径倍数 44.13
        Rigel(size_scale=SIZE_SCALE, ignore_mass=True),  # 参宿七      质量倍数 21     半径倍数 78.9
        Antares(size_scale=SIZE_SCALE, ignore_mass=True),  # 心宿二    质量倍数 12     半径倍数 770
        Betelgeuse(size_scale=SIZE_SCALE, ignore_mass=True),  # 参宿四 质量倍数 11.6   半径倍数 887
        VYCanisMajoris(size_scale=SIZE_SCALE, ignore_mass=True),  # 大犬座VY 质量倍数 25   半径倍数 1419.75
        UYScuti(size_scale=SIZE_SCALE, ignore_mass=True),  # 盾牌座 UY     质量倍数 10.0   半径倍数 1706.7
        Stephenson_2_18(size_scale=SIZE_SCALE, ignore_mass=True)  # 史蒂文森2-18    质量倍数 40.0  半径倍数 2158.5
    ]
    distance_sum = 0
    for idx, body in enumerate(bodies):
        body.rotation_speed /= 10
        if idx > 1:
            body.light_on = False  # 关闭灯光效果，只有太阳对地球有灯光效果
            d = pow((body.diameter + bodies[idx - 1].diameter) * SIZE_SCALE, 0.75) * 120
            # d = (body.diameter + bodies[idx - 1].diameter) * SIZE_SCALE * 1.1 + D
            body.init_position = [(distance_sum + d) / 2, (distance_sum + d), 0]
            distance_sum += d

    # 使用 ursina 查看的运行效果
    # 常用快捷键： P：运行和暂停  O：重新开始  I：显示天体轨迹
    # position = 左-右+、上+下-、前+后-
    ursina_run(bodies, SECONDS_PER_MONTH, position=(0, 200000, -AU / 200), show_trail=True)
