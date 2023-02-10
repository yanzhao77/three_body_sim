# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulators.simulator import Simulator
from common.system import System
from simulators.views.mpl_view import MplView
import numpy as np
import time

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换默认sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）

X_MIN, X_MAX = -4e+8, 4e+8  # the x range of the bounding box (m)
Y_MIN, Y_MAX = -4e+8, 4e+8  # the y range of the bounding box (m)
Z_MIN, Z_MAX = -4e+8, 4e+8  # the z range of the bounding box (m)


class MplSimulator(Simulator):
    """
    matplotlib天体运行模拟器
    """

    def __init__(self, bodies_sys: System):
        super().__init__(bodies_sys, MplView)

    def run(self, dt):
        """

        :param dt:
        :return:
        """

        MAX_FRAME = 20
        views_frames = []
        for i in range(MAX_FRAME):
            self.evolve(dt)
            body_views = self.body_views
            self.show_figure(body_views)
            time.sleep(0.5)
            views_frames.append(body_views.copy())

        # TODO: views_frames 用于 gif 动画
        # fig = plt.figure()
        #
        # def update(num):
        #     body_viewers = viewers_frames[num]
        #     print(body_viewers)
        #
        #     return self.show_figure(plt, body_viewers)
        #
        # ani = animation.FuncAnimation(fig=fig, func=update, frames=np.arange(0, MAX_FRAME), interval=1)
        # ani.save('bodies_run.gif')
        # plt.show()

    def show_figure(self, bodies):
        fig = plt.figure(figsize=(16, 12))
        ax = plt.axes(projection="3d")
        ax.set_xlim(X_MIN, X_MAX)
        ax.set_ylim(Y_MIN, Y_MAX)
        ax.set_zlim(Z_MIN, Z_MAX)
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        for idx, body in enumerate(bodies):
            if body.is_fixed_star:
                color = 'red'
            else:
                color = 'blue'
            # size = 800 if str(body.name).lower().startswith("sun") else 500
            size = body.raduis / 80000
            pos = body.position
            ax.text(pos[0], pos[1], pos[2] + 1e8, body.name, color=color, fontsize=20)
            ax.scatter(pos[0], pos[1], pos[2], color=color, s=size)
            # for _his_pos in body.his_position():
            #     ax.scatter3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.5)
            # ax.scatter(his_pos[0], his_pos[1], his_pos[2], color=colors[idx], s=10)
            his_pos = body.his_position
            if len(his_pos) > 1:
                _his_pos = list(zip(*his_pos))
                ax.plot3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.8)
        plt.title("天体运行")
        # display the  plot
        plt.show()
        # return ax


if __name__ == '__main__':
    from scenes.func import mpl_run
    from bodies import Sun, Earth
    from common.consts import SECONDS_PER_WEEK

    """
    太阳、地球
    """
    bodies = [
        Sun(size_scale=1.2e2),  # 太阳放大 120 倍
        Earth(size_scale=4e3, distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    ]
    mpl_run(bodies, SECONDS_PER_WEEK)
