# -*- coding:utf-8 -*-
# title           :matplotlib天体运行模拟器
# description     :matplotlib天体运行模拟器
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from simulators.simulator import Simulator
from common.system import System
from simulators.views.mpl_view import MplView
import numpy as np
import copy

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换默认sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）


class MplSimulator(Simulator):
    """
    matplotlib天体运行模拟器
    """

    def __init__(self, bodies_sys: System):
        super().__init__(bodies_sys, MplView)

    def save_as_gif(self, dt, gif_max_frame=200, gif_file_name='bodies_run.gif'):
        """
        保存 GIF 文件
        :param dt: 单位：秒，按时间差进行演变，值越小越精确，但演变速度会慢。
        :param gif_max_frame: 导出的 gif 的最多帧数
        :param gif_file_name: 导出的 gif 文件名
        :return:
        """
        fig = plt.figure('天体模拟运行效果', figsize=(16, 12))
        ax = fig.gca(projection="3d")
        views_frames = []
        for i in range(gif_max_frame):
            self.evolve(dt)
            body_views = copy.deepcopy(self.body_views)
            views_frames.append(body_views)

        def update(num):
            body_views = views_frames[num]
            print("GIF 生成进度：%d/%d %.2f" % (num + 1, gif_max_frame, ((num + 1) / gif_max_frame) * 100) + "%")
            return self.show_figure(ax, body_views, pause=0)

        ani = animation.FuncAnimation(fig=fig, func=update, frames=np.arange(0, gif_max_frame), interval=1)
        ani.save(gif_file_name)

    def run(self, dt, gif_file_name=None):
        """

        :param dt: 单位：秒，按时间差进行演变，值越小越精确，但演变速度会慢。
        :param gif_file_name: 导出的 gif 文件名，如果为空，则显示动画
        :return:
        """
        if gif_file_name is not None:
            self.save_as_gif(dt, gif_max_frame=200, gif_file_name=gif_file_name)
            return

        fig = plt.figure('天体模拟运行效果', figsize=(16, 12))
        ax = fig.gca(projection="3d")
        # TODO: 注意：显示动态图，需先进行以下设置：
        # Pycharm：：File –> Settings –> Tools –> Python Scientific –> Show plots in tool window(取消打勾)

        while True:
            self.evolve(dt)
            body_views = copy.deepcopy(self.body_views)
            self.show_figure(ax, body_views, pause=0.1)

    def show_figure(self, ax, bodies, pause=0.1):
        """

        :param ax:
        :param bodies:
        :param pause:
        :return:
        """
        plt.cla()

        ax.set_title('天体模拟运行效果')
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
            # 天体名称
            ax.text(pos[0], pos[1], pos[2] + 0.006, s=body.name, color=color, fontsize=12)
            # 天体
            ax.scatter(pos[0], pos[1], pos[2], color=color, s=size, alpha=0.8)
            # for _his_pos in body.his_position():
            #     ax.scatter3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.5)
            # ax.scatter(his_pos[0], his_pos[1], his_pos[2], color=colors[idx], s=10)
            his_pos = body.his_position
            tail_len = len(his_pos)
            if tail_len > 1:
                _his_pos = list(zip(*his_pos))
                # 历史轨迹线
                ax.plot3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.5)

        if pause > 0:
            plt.pause(pause)


if __name__ == '__main__':
    # TODO: 注意：显示动态图，需先进行以下设置：
    # Pycharm：：File –> Settings –> Tools –> Python Scientific –> Show plots in tool window(取消打勾)
    from scenes.func import mpl_run
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
    gif_file_name = None  # 显示动画
    # gif_file_name = 'bodies_run.gif'  # 保存 GIF 文件
    mpl_run(bodies, SECONDS_PER_WEEK, gif_file_name)
