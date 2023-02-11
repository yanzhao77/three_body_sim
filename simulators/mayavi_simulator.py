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
    def run(self, dt):
        f = mlab.gcf()
        while True:
            self.evolve(dt)
            # Updating scene...
            f.scene.render()
            yield


if __name__ == '__main__':
    from scenes.func import mayavi_run
    from bodies import Sun, Earth
    from common.consts import SECONDS_PER_WEEK

    """
    太阳、地球
    """
    bodies = [
        Sun(size_scale=1.2e2),  # 太阳放大 120 倍
        Earth(size_scale=4e3, distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    ]
    mayavi_run(bodies, SECONDS_PER_WEEK)
