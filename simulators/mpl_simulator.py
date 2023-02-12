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

plt.rcParams['font.sans-serif'] = ['SimHei']  # 步骤一（替换默认sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False  # 步骤二（解决坐标轴负数的负号显示问题）


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
        fig = plt.figure('天体模拟运行效果', figsize=(16, 12))
        ax = fig.gca(projection="3d")

        MAX_FRAME = 2000
        views_frames = []
        for i in range(MAX_FRAME):
            self.evolve(dt)
            body_views = self.body_views
            self.show_figure(ax, body_views)
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

    def show_figure(self, ax, bodies):
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
        plt.pause(0.1)


if __name__ == '__main__':
    # TODO: 注意：绘制动态图，需先进行以下设置：
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
    mpl_run(bodies, SECONDS_PER_WEEK)
