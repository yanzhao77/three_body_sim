# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from mayavi import mlab
from bodies import Body, Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
from common.consts import SECONDS_PER_DAY, SECONDS_PER_HOUR, SECONDS_PER_MONTH, SECONDS_PER_WEEK

from simulators.mayavi_body import MayaviBody


class MayaviSimulator:
    """

    """

    def __init__(self, sys):
        self.sys = sys
        self.mayavi_bodies = []
        for body in self.sys.bodies:
            mbody = MayaviBody(body)
            self.mayavi_bodies.append(mbody)

    def run(self, dt):
        self.sys.evolve(dt)
        for idx, body in enumerate(self.mayavi_bodies):
            # acceleration 加速度
            # body.velocity = self.sys.bodies[idx].velocity
            # body.position += 0.5 * body.acceleration * (dt ** 2)
            body.position = self.sys.bodies[idx].position * self.sys.bodies[idx].distance_scale
            body.update_source_data()
            print(self.sys.bodies[idx])

    @mlab.animate(delay=100, ui=True)
    def run_anim(self):
        f = mlab.gcf()
        while True:
            self.run(SECONDS_PER_WEEK)
            # Updating scene...
            f.scene.render()
            yield


if __name__ == '__main__':
    # 背景色
    bgcolor = (1 / 255, 1 / 255, 100 / 255)  # 宇宙背景色
    mlab.figure(bgcolor=bgcolor, size=(1440, 810))
    # 八大行星：木星(♃)、土星(♄)、天王星(♅)、海王星(♆)、地球(⊕)、金星(♀)、火星(♂)、水星(☿)
    # 排列顺序
    # 1、体积：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 1330：745：65：60：1：0.86：0.15：0.056
    # 2、质量：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 318：95：14.53：17.15：1：0.8：0.11：0.0553
    # 3、离太阳从近到远的顺序：水星、金星、地球、火星、木星、土星、天王星、海王星
    bodies = [
        Sun(size_scale=1),  # 太阳
        Mercury(size_scale=3e1, distance_scale=1e1),  # 水星
        Venus(size_scale=2e1, distance_scale=1e1),  # 金星
        Earth(size_scale=2e1, distance_scale=1e1),  # 地球
        Mars(size_scale=2e1, distance_scale=1e1),  # 火星
        Jupiter(size_scale=0.5e1, distance_scale=0.4e1),  # 木星
        Saturn(size_scale=0.5e1, distance_scale=0.3e1),  # 土星
        Uranus(size_scale=0.5e1, distance_scale=0.2e1),  # 天王星
        Neptune(size_scale=0.5e1, distance_scale=0.15e1),  # 海王星
        Pluto(size_scale=5e1, distance_scale=0.12e1),  # 冥王星(从太阳系的行星中排除)
    ]
    from simulators.system import System

    body_sys = System(bodies)
    simulator = MayaviSimulator(body_sys)
    simulator.run_anim()
    mlab.view(azimuth=-45, distance=9e9)
    mlab.show()
