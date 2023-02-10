# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from mayavi import mlab
from simulators.simulator import Simulator
from common.system import System
from simulators.viewers.mayavi_view import MayaviView


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
