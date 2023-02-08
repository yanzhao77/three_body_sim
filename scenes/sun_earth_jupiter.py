# -*- coding:utf-8 -*-
# title           :太阳系场景
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from mayavi import mlab
from bodies import Body, Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
from common.consts import SECONDS_PER_DAY, SECONDS_PER_HOUR, SECONDS_PER_MONTH, SECONDS_PER_WEEK

from simulators.mayavi_simulator import MayaviSimulator

if __name__ == '__main__':
    # 背景色
    bgcolor = (1 / 255, 1 / 255, 30 / 255)  # 宇宙背景色
    mlab.figure(bgcolor=bgcolor, size=(1440, 810))
    # 八大行星：木星(♃)、土星(♄)、天王星(♅)、海王星(♆)、地球(⊕)、金星(♀)、火星(♂)、水星(☿)
    # 排列顺序
    # 1、体积：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 1330：745：65：60：1：0.86：0.15：0.056
    # 2、质量：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 318：95：14.53：17.15：1：0.8：0.11：0.0553
    # 3、离太阳从近到远的顺序：水星、金星、地球、火星、木星、土星、天王星、海王星
    bodies = [
        Sun(size_scale=1),  # 太阳
        Earth(size_scale=2e1, distance_scale=1e1),  # 地球
        Jupiter(size_scale=0.5e1, distance_scale=1e1),  # 木星
    ]
    from simulators.system import System

    body_sys = System(bodies)
    simulator = MayaviSimulator(body_sys)
    simulator.run_anim(SECONDS_PER_WEEK)
    # azimuth:
    #    观测方位角，可选，float类型（以度为单位，0-360），用x轴投影到x-y平面上的球体上的位置矢量所对的角度。
    # elevation:
    #    观测天顶角，可选，float类型（以度为单位，0-180）, 位置向量和z轴所对的角度。
    # distance:
    #    观测距离，可选，float类型 or 'auto',一个正浮点数，表示距放置相机的焦点的距离。
    #    Mayavi 3.4.0中的新功能：'auto' 使得距离为观察所有对象的最佳位置。
    # focalpoint:
    #    观测焦点，可选，类型为一个由3个浮点数组成的数组 or 'auto'，，代表观测相机的焦点
    #    Mayavi 3.4.0中的新功能：'auto'，则焦点位于场景中所有对象的中心。
    # roll:
    #    控制滚动，可选，float类型，即摄影机围绕其轴的旋转
    # reset_roll:
    #    布尔值，可选。如果为True，且未指定“滚动”，则重置相机的滚动方向。
    # figure:
    #    要操作的Mayavi图形。如果为 None，则使用当前图形。
    mlab.view(azimuth=-45, distance=9e9)
    mlab.show()
