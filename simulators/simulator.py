# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from abc import ABCMeta, abstractmethod
from common.system import System


class Simulator(metaclass=ABCMeta):
    """

    """

    def __init__(self, bodies_sys: System, viewer_type: type):
        """

        :param bodies_sys: 天体系统
        :param viewer_type: BodyViewer类型
        """
        self.body_viewers = []
        self.bodies_sys = bodies_sys
        self.init_viewers(viewer_type)

    def init_viewers(self, viewer_type: type):
        """

        :param viewer_type: BodyViewer类型
        :return:
        """
        for body in self.bodies_sys.bodies:
            viewer = viewer_type(body)
            self.body_viewers.append(viewer)

    def evolve(self, dt: int):
        """
        按时间差进行演变，值越小越精确，但演变速度会慢。
        :param dt: 时间差（秒）
        :return:
        """
        self.bodies_sys.evolve(dt)
        for idx, viewer in enumerate(self.body_viewers):
            viewer.position = self.bodies_sys.bodies[idx].position * self.bodies_sys.bodies[idx].distance_scale
            viewer.update()

    @abstractmethod
    def run(self, dt: int):
        """
        按时间差运行，值越小越精确，但演变速度会慢。
        :param dt: 时间差（秒）
        :return:
        """
        pass
