# -*- coding:utf-8 -*-
# title           :Mayavi天体运行模拟器
# description     :Mayavi天体运行模拟器
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from mayavi import mlab
from simulators.simulator import Simulator
from common.system import System
from simulators.views.mayavi_view import MayaviView


class MayaviSimulator(Simulator):
    """
    Mayavi天体运行模拟器
    """

    def __init__(self, bodies_sys: System):
        super().__init__(bodies_sys, MayaviView)

    @mlab.animate(delay=100, ui=True)
    def run(self, dt, **kwargs):
        f = mlab.gcf()
        while True:
            self.evolve(dt)
            f.scene.render()
            yield


if __name__ == '__main__':
    from scenes.func import mayavi_run
    from bodies import Sun, Earth
    from common.consts import SECONDS_PER_WEEK

    """
    3个太阳、1个地球
    """
    bodies = [
        Sun(name='太阳1', mass=1.5e30, init_position=[849597870.700, 0, 0], init_velocity=[0, 7.0, 0],
            size_scale=5e1, texture="sun1.jpg"),  # 太阳放大 100 倍
        Sun(name='太阳2', mass=2e30, init_position=[0, 0, 0], init_velocity=[0, -8.0, 0],
            size_scale=5e1, texture="sun2.jpg"),  # 太阳放大 100 倍
        Sun(name='太阳3', mass=2.5e30, init_position=[0, -849597870.700, 0], init_velocity=[18.0, 0, 0],
            size_scale=5e1, texture="sun2.jpg"),  # 太阳放大 100 倍
        Earth(name='地球', init_position=[0, -349597870.700, 0], init_velocity=[15.50, 0, 0],
              size_scale=4e3, distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    ]
    mayavi_run(bodies, SECONDS_PER_WEEK)
