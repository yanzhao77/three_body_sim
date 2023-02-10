# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from common.consts import SECONDS_PER_WEEK
from common.system import System


def mayavi_run(bodies, dt=SECONDS_PER_WEEK,
               view_azimuth=0, view_distance='auto', view_focalpoint='auto',
               bgcolor=(1 / 255, 1 / 255, 30 / 255)):
    """
    用 mayavi 查看运行效果
    :param bodies: 天体
    :param dt: 单位：秒，按时间差进行演变，值越小越精确，但演变速度会慢。
    :param view_azimuth: 观测方位角，可选，float类型（以度为单位，0-360），用x轴投影到x-y平面上的球体上的位置矢量所对的角度。
    :param view_distance: 观测距离，可选，float类型 or 'auto',一个正浮点数，表示距放置相机的焦点的距离。
    :param view_focalpoint: 观测焦点，可选，类型为一个由3个浮点数组成的数组 or 'auto'，，代表观测相机的焦点
    :param bgcolor:
    :return:
    """
    from mayavi import mlab
    from simulators.mayavi_simulator import MayaviSimulator
    # 宇宙背景色
    mlab.figure(bgcolor=bgcolor, size=(1440, 810))
    body_sys = System(bodies)
    simulator = MayaviSimulator(body_sys)
    simulator.run(dt)
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
    mlab.view(azimuth=view_azimuth, distance=view_distance, focalpoint=view_focalpoint)
    # mlab.view(azimuth=-45, elevation=45, distance=100e8 * 2 * 2 * 4 * 4, focalpoint=[5e10, 5e10, 5e9])
    mlab.show()


def mpl_run(bodies, dt=SECONDS_PER_WEEK):
    """

    :param bodies: 天体
    :param dt: 单位：秒，按时间差进行演变，值越小越精确，但演变速度会慢。
    :return:
    """
    from simulators.mpl_simulator import MplSimulator
    body_sys = System(bodies)
    simulator = MplSimulator(body_sys)
    simulator.run(dt)


if __name__ == '__main__':
    from bodies import Sun, Earth

    """
    太阳、地球
    """
    bodies = [
        Sun(size_scale=1.2e2),  # 太阳放大 120 倍
        Earth(size_scale=4e3, distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    ]
    mpl_run(bodies, SECONDS_PER_WEEK)
