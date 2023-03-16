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
import matplotlib.colors as mcolors
from simulators.simulator import Simulator
from common.system import System
from common.consts import AU
from simulators.views.mpl_view import MplView
from simulators.func import create_fig_ax, update_ax_styles
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

    def save_as_gif(self, dt, gif_max_frame=200, gif_file_name='bodies_run.gif', styles={}):
        """
        保存 GIF 文件
        :param dt: 单位：秒，按时间差进行演变，值越小越精确，但演变速度会慢。
        :param gif_max_frame: 导出的 gif 文件的画面帧数
        :param gif_file_name: 导出的 gif 文件名
        :return:
        """

        fig, ax = create_fig_ax()

        views_frames = []
        for i in range(gif_max_frame):
            self.evolve(dt)
            body_views = copy.deepcopy(self.body_views)
            views_frames.append(body_views)

        def update(num):
            body_views = views_frames[num]
            print("\rGIF 生成进度：%d/%d %.2f" % (num + 1, gif_max_frame, ((num + 1) / gif_max_frame) * 100) + "%", end='')
            return self.show_figure(ax, body_views, pause=0, update_ax=update_ax_styles, styles=styles)

        ani = animation.FuncAnimation(fig=fig, func=update, frames=np.arange(0, gif_max_frame), interval=1)
        ani.save(gif_file_name)

    def run(self, dt, **kwargs):
        """

        :param dt: 单位：秒，按时间差进行演变，值越小越精确，但演变速度会慢。
        :param kwargs:
            gif_file_name: 导出的 gif 文件名，如果为空，则显示动画
            gif_max_frame: 导出的 gif 文件的画面帧数
        :return:
        """
        gif_file_name = kwargs["gif_file_name"] if "gif_file_name" in kwargs else None
        gif_max_frame = kwargs["gif_max_frame"] if "gif_max_frame" in kwargs else None
        styles = kwargs["styles"] if "styles" in kwargs else {}

        if gif_file_name is not None:
            self.save_as_gif(dt, gif_max_frame=gif_max_frame, gif_file_name=gif_file_name, styles=styles)
            return

        fig, ax = create_fig_ax()

        # TODO: 注意：显示动态图，需先进行以下设置：
        # Pycharm：：File –> Settings –> Tools –> Python Scientific –> Show plots in tool window(取消打勾)

        while True:
            self.evolve(dt)
            body_views = copy.deepcopy(self.body_views)
            self.show_figure(ax, body_views, pause=0.1, update_ax=update_ax_styles, styles=styles)

    def show_figure(self, ax, bodies, pause=0.1, update_ax=None, styles={}):
        """

        :param ax:
        :param bodies:
        :param pause:
        :return:
        """
        if update_ax is not None:
            # 更新 ax
            update_ax(ax, styles)

        for idx, body in enumerate(bodies):
            if hasattr(body, "torus_stars"):
                # 暂不支持环状小行星群
                continue

            if body.is_fixed_star:
                color = 'red'
            else:
                color = 'blue'
            # size = 800 if str(body.name).lower().startswith("sun") else 500
            size = body.raduis * body.size_scale / 80000
            # size = pow(body.raduis / AU * body.size_scale,3)
            pos = body.position / AU

            # 天体
            ax.scatter(pos[0], pos[1], pos[2], color=color, s=size, alpha=0.8)
            # for _his_pos in body.his_position():
            #     ax.scatter3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.5)
            # ax.scatter(his_pos[0], his_pos[1], his_pos[2], color=colors[idx], s=10)
            his_pos = np.array(body.his_position) / AU
            tail_len = len(his_pos)
            if tail_len > 1:
                _his_pos = list(zip(*his_pos))
                # 历史轨迹线
                ax.plot3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.5)

            z_range = ax.get_zlim()[1] - ax.get_zlim()[0]
            ax.text(pos[0], pos[1], pos[2] + size * (z_range / 5000), s=body.name, color=color, fontsize=12)

        if pause > 0:
            plt.pause(pause)


if __name__ == '__main__':
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
    # 保存 GIF，参数为指定保存 GIF 文件以及文件的画面帧数
    gif_file_name, gif_max_frame = 'bodies_run.gif', 100

    # 只显示动画，不保存 GIF 文件。注释掉以下代码，则使用上面的参数
    # TODO: 注意：显示动态图，需先进行以下设置：
    # Pycharm：：File –> Settings –> Tools –> Python Scientific –> Show plots in tool window(取消打勾)
    gif_file_name, gif_max_frame = None, None

    mpl_run(bodies, SECONDS_PER_WEEK, gif_file_name, gif_max_frame)
