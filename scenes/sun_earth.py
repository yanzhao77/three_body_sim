# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
# from mayavi import mlab

from bodies import Sun, Earth

bodies = [
    Sun(size_scale=1.5e-2),
    Earth(size_scale=9e3)  # 地球
]
print(bodies)
# 运行天体的动画
# run_anim(bodies)

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
# mlab.view(azimuth=-45, elevation=45, distance=50e8 * 2 * 2 * 4 * 4, focalpoint=[5e10, 0, 0])
# mlab.show()
