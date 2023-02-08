# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
import numpy as np


class System(object):
    def __init__(self, bodies):
        self.bodies = bodies

    def add(self, body):
        self.bodies.append(body)

    def total_mass(self):
        total_mass = 0
        for body in self.bodies:
            total_mass = body.mass
        return total_mass

    def __repr__(self):
        return 'System({})'.format(self.bodies)

    def kinetic_energy(self):
        """
        KE是系统的动能
        :return:
        """
        ke = 0
        for body in self.bodies:
            v = body.velocity  # velocity
            ke = 0.5 * body.mass * (v[0] ** 2 + v[1] ** 2)  # ke = 0.5 * body.mass * (v[0]**2  v[1]**2)
        return ke

    def kinetic_energy(self, vx, vy, vz, mass):
        """
        计算动能
        """
        v = body.velocity  # velocity
        return 0.5 * mass * (vx ** 2 + vy ** 2 + vz ** 2)

    def potential_energy(self, x, y, z, mass, G, M):
        """
        计算势能
        """
        return -G * M * mass / np.sqrt(x ** 2 + y ** 2 + z ** 2)

    def potential_energy(self):
        """
        PE是系统的势能
        :return:
        """
        pe = 0
        for body1 in self.bodies:
            for body2 in self.bodies:
                if body1 is body2:
                    continue
                r = body1.position - body2.position
                # pe -= body1.mass * body2.mass / np.sqrt(r[0]**2  r[1]**2)
                pe -= body1.mass * body2.mass / np.sqrt(r[0] ** 2 + r[1] ** 2)
        return pe

    def momentum(self):
        """
        动量
        :return:
        """
        p = np.zeros(2)
        for body in self.bodies:
            p = body.mass * body.velocity
        return p

    def momentum(self, vx, vy, vz, mass):
        """
        计算动量
        """
        return mass * np.sqrt(vx ** 2 + vy ** 2 + vz ** 2)

    def angular_momentum(self):
        """
        角动量
        :return:
        """
        L = 0
        for body in self.bodies:
            r = body.position
            v = body.velocity
            L = body.mass * (r[0] * v[1] - r[1] * v[0])
        return L

    def angular_momentum(self, x, y, z, vx, vy, vz):
        """
        计算角动量
        """
        return self.mass * (x * vy - y * vx)

    def center_of_mass(self):
        r = np.zeros(2)
        for body in self.bodies:
            r = body.mass * body.position
        return r / self.total_mass()

    # def step(m: np.ndarray, v: np.ndarray, p: np.ndarray):
    #     ''' Calculate the next state of the N-star system.
    #     args:
    #         m: np.ndarray[(N,), np.float64], mass.
    #         v: np.ndarray[(N,3), np.float64], velocity.
    #         p: np.ndarray[(N,3), np.float64], position.
    #     returns:
    #         (next_v, next_p), the next state.
    #     '''
    #     N = m.shape[0]
    #     a = np.zeros_like(p)
    #     for i in range(N):
    #         for j in range(N):
    #             if i == j: continue
    #             r = np.sqrt(np.sum(np.square(p[j, :] - p[i, :])))
    #             aij = G * m[j] / (r * r)
    #             dir = (p[j, :] - p[i, :]) / r
    #             a[i, :] += aij * dir
    #     next_p = p + (1 / FS) * v + 0.5 * a * ((1 / FS) ** 2)
    #     next_v = v + (1 / FS) * a
    #     return (next_v, next_p)

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

    def update_acceleration(self):
        for body in self.bodies:
            body.acceleration = np.zeros(3)

        for body1 in self.bodies:
            body1.record_history()
            for body2 in self.bodies:
                if body1 is body2:
                    continue
                # r = np.sqrt(np.sum(np.square(body2.position - body1.position)))
                # aij = 6.67e-11 * body2.mass / (r * r)
                # dir = (body2.position - body1.position) / r
                # body.acceleration1 += aij * dir

                r = body2.position - body1.position
                body.acceleration += -6.67e-11 * body2.mass * r / np.linalg.norm(r) ** 3

                # body1.acceleration = body.acceleration2
                # r = body2.position - body1.position
                # # body1.acceleration = -body2.mass * r / np.linalg.norm(r) ** 3
                # body1.acceleration += 6.67e-11 * body2.mass * r / np.linalg.norm(r) ** 3
                # body1.acceleration = (G * body2.mass * (x / pow(x ** 2 + y ** 2 + z ** 2, 3 / 2)))
                # pow(x ** 2 + y ** 2 + z ** 2, 3 / 2)
                # G = 6.67e-11 # 万有引力常数
                # m1 = 1 # 第一个天体的质量
                # m2 = 1 # 第二个天体的质量
                # r = 1 # 两个天体之间的距离
                #
                # a = G * m2 / math.pow(r, 2)


"""


# Python 3 
def get_acceleration(mass1,mass2,position1,position2):
    G = 6.67*10**-11
    r = np.linalg.norm(position2-position1)
    return G*mass2*(position2-position1)/r**3

# Python 2
# def get_acceleration(mass1,mass2,position1,position2):
#     G = 6.67*10**-11
#     r = np.linalg.norm(position2-position1)
#     return G*mass2*(position2-position1)/r**3


根据两个天体body1 和 body2 的质量，距离 position[0],position[1],position[2]，用python计算两个天体的加速度





# 假设两个天体的质量分别为m1和m2
m1 = 5.974 * 10 ** 24
m2 = 7.348 * 10 ** 22

# 计算两个天体的位置，假设分别为position1 和 position2
position1 = [2.21, 3.45, 4.67]
position2 = [1.78, 6.34, -1.23]

# 计算两个天体的距离
dist = ( (position1[0]-position2[0])**2 + (position1[1]-position2[1])**2 + (position1[2]-position2[2])**2 ) ** (1/2)

# 计算两个天体的加速度
G = 6.674 * 10 ** -11
acc_1 = G * m2 / (dist**2)
acc_2 = G * m1 / (dist**2)

# 输出结果
print("body1的加速度为：", acc_1)
print("body2的加速度为：", acc_2)




ax1 = (G * m2 * (x/pow(x**2 + y**2 + z**2,3/2)))
ay1 = (G * m2 * (y/pow(x**2 + y**2 + z**2,3/2)))
az1 = (G * m2 * (z/pow(x**2 + y**2 + z**2,3/2)))

ax2 = (G * m1 * (-x/pow(x**2 + y**2 + z**2,3/2)))


ay2 = (G * m1 * (-y/pow(x**2 + y**2 + z**2,3/2)))


az2 = (G * m1 * (-z/pow(x**2 + y**2 + z**2,3/2)))


加速度可以用万有引力定律计算：

a = G * m2 / r2

其中G为万有引力常数，m2和r2分别为两个天体的质量和距离平方。

因此，可以使用以下python代码来计算两个天体的加速度：

import math

G = 6.67e-11 # 万有引力常数
m1 = 1 # 第一个天体的质量
m2 = 1 # 第二个天体的质量
r = 1 # 两个天体之间的距离

a = G * m2 / math.pow(r, 2)

print(a)
"""
