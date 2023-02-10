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
    天体运行模拟器
    """

    def __init__(self, bodies_sys: System, viewer_type: type):
        """

        :param bodies_sys: 天体系统
        :param viewer_type: BodyViewer类型
        """
        self.body_views = []
        self.bodies_sys = bodies_sys
        self.init_views(viewer_type)

    def init_views(self, viewer_type: type):
        """

        :param viewer_type: BodyViewer类型
        :return:
        """
        for body in self.bodies_sys.bodies:
            view = viewer_type(body)
            self.body_views.append(view)

    def evolve(self, dt: int):
        """
        单位：秒，按时间差进行演变，值越小越精确，但演变速度会慢。
        :param dt: 时间差（秒）
        :return:
        """
        self.bodies_sys.evolve(dt)
        for idx, view in enumerate(self.body_views):
            body = self.bodies_sys.bodies[idx]
            view.appeared = body.appeared
            if not view.appeared:
                view.disappear()
                continue
            view.position = body.position * body.distance_scale
            view.name = body.name
            view.mass = body.mass
            view.acceleration = body.acceleration
            view.velocity = body.velocity
            # viewer.volume = body.volume
            view.raduis = body.raduis * body.size_scale
            view.his_position = body.his_position()
            view.is_fixed_star = body.is_fixed_star
            view.has_rings = body.has_rings
            view.size_scale = body.size_scale
            view.distance_scale = body.distance_scale

            view.update()

        self.bodies_sys.bodies = list(filter(lambda b:b.appeared, self.bodies_sys.bodies))
        self.body_views = list(filter(lambda b:b.appeared, self.body_views))

    @abstractmethod
    def run(self, dt: int):
        """
        按时间差运行，值越小越精确，但演变速度会慢。
        :param dt: 时间差（秒）
        :return:
        """
        pass
