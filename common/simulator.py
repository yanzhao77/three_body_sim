# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from common.system import System
from bodies import Body, Sun, Earth

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

X_MIN, X_MAX = -2e+14, 2e+14  # the x range of the bounding box (m)
Y_MIN, Y_MAX = -2e+14, 2e+14  # the y range of the bounding box (m)
Z_MIN, Z_MAX = -2e+14, 2e+14  # the z range of the bounding box (m)

X_MIN, X_MAX = -2e+12, 2e+12  # the x range of the bounding box (m)
Y_MIN, Y_MAX = -2e+12, 2e+12  # the y range of the bounding box (m)
Z_MIN, Z_MAX = -2e+12, 2e+12  # the z range of the bounding box (m)

X_MIN, X_MAX = -1e+9, 1e+9  # the x range of the bounding box (m)
Y_MIN, Y_MAX = -1e+9, 1e+9  # the y range of the bounding box (m)
Z_MIN, Z_MAX = -1e+9, 1e+9  # the z range of the bounding box (m)

# X_MIN, X_MAX = -8e+8, 8e+8  # the x range of the bounding box (m)
# Y_MIN, Y_MAX = -8e+8, 8e+8  # the y range of the bounding box (m)
# Z_MIN, Z_MAX = -8e+8, 8e+8  # the z range of the bounding box (m)


def show(bodies, idx=0):
    # from scipy.interpolate import make_interp_spline

    # Creating figures for the plot
    fig = plt.figure(figsize=(16, 12))
    ax = plt.axes(projection="3d")
    ax.set_xlim(X_MIN, X_MAX)
    ax.set_ylim(Y_MIN, Y_MAX)
    ax.set_zlim(Z_MIN, Z_MAX)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    # Creating a plot using the random datasets
    colors = ['red', 'blue', 'red', 'red']
    sizes = [800, 500, 800, 800]
    for idx, body in enumerate(bodies):
        color = 'red' if str(body.name).startswith("sun") else 'blue'
        size = 800 if str(body.name).startswith("sun") else 500
        pos = body.position
        ax.text(pos[0], pos[1], pos[2] + 1e8, body.name, color=color, fontsize=20)
        ax.scatter(pos[0], pos[1], pos[2], color=color, s=size)
        # for _his_pos in body.his_position():
        #     ax.scatter3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.5)
        # ax.scatter(his_pos[0], his_pos[1], his_pos[2], color=colors[idx], s=10)
        his_pos = body.his_position()
        if len(his_pos) > 1:
            _his_pos = list(zip(*his_pos))
            ax.plot3D(_his_pos[0], _his_pos[1], _his_pos[2], color=color, alpha=0.8)
    plt.title("3D scatter plot %s" % idx)
    # display the  plot
    plt.show()


import time


class Simulator:
    def __init__(self, system, dt):
        self.system = system
        self.dt = dt

    def evolve(self, dt):
        show(self.system.bodies)
        self.system.update_acceleration()

        # next_p = p + dt * v + 0.5 * a * (dt ** 2)
        # next_v = v + dt * a
        #     for body1 in bodies:
        #         for body2 in bodies:
        #             if body1 == body2:  # 相等说明是同一个天体，跳过计算
        #                 continue
        #             r = body2.position - body1.position
        #             # F = G x (m1 x m2) / r²  万有引力定律
        #             F = Configs.G * body1.mass * body2.mass * r / np.linalg.norm(r) / r.dot(r)
        #             body1.momentum = body1.momentum + F * dt  # 动量定理
        #         body1.position = body1.position + (body1.momentum / body1.mass) * dt
        #         body1.update_source_data()

        for body in self.system.bodies:
            # body.vx = body.vx + ax * dt
            # body.x = body.x + body.vx * dt
            # acceleration 加速度
            body.velocity += body.acceleration * dt
            # body.position += body.velocity * dt  # - 0.5 * body.acceleration * (dt ** 2)
            body.position += body.velocity * dt
            print(body)
            # print(body.name, body.position)

    def run(self, t):
        n = int(t / self.dt)
        for i in range(n):
            self.evolve(self.dt)
            time.sleep(1)

    def run_always(self):
        dt = 1  # 时间变化1秒
        while True:
            # time.sleep(1)
            self.evolve(dt)


if __name__ == '__main__':
    t = 60 * 60 * 24 * 100

    # _sys = System([Sun(init_position=[0, 0, 149597870.700]), Earth()])

    # _sys = System([Sun(init_position=[849597870.700, 0, 0], init_velocity=[0, 9.79, 0]),
    #                Sun(init_position=[0, 0, 0], init_velocity=[0, -9.79, 0])])

    # _sys = System([Sun(), Earth()])

    _sys = System([Sun(name="sun1", init_position=[849597870.700, 0, 0], init_velocity=[0, 7.0, 0]),
                   Sun(name="sun2", init_position=[0, 0, 0], init_velocity=[0, -8.0, 0]),
                   Sun(name="sun3", init_position=[0, -849597870.700, 0], init_velocity=[18.0, 0, 0]),
                   Earth(init_position=[0, -349597870.700, 0], init_velocity=[15.50, 0, 0])])

    _sim = Simulator(_sys, t)
    _sim.run(t * 100)
