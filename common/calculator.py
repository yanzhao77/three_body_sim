# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
import numpy as np
import math


class MechanicalCalculator:
    """
    力学计算器：
        牛顿引力常数就有万有引力常数：G=6.67x10^-11 (N·m^2 /kg^2）
        计算万有引力时会用到
        万有引力公式：F=G*m1*m2/r*
    """

    @staticmethod
    def getAcc(pos, mass, G, softening):
        """
        Calculate the acceleration on each particle due to Newton's Law
        pos  is an N x 3 matrix of positions
        mass is an N x 1 vector of masses
        G is Newton's Gravitational constant
        softening is the softening length
        a is N x 3 matrix of accelerations


        """
        # positions r = [x,y,z] for all particles
        x = pos[:, 0:1]
        y = pos[:, 1:2]
        z = pos[:, 2:3]

        # matrix that stores all pairwise particle separations: r_j - r_i
        dx = x.T - x
        dy = y.T - y
        dz = z.T - z

        # matrix that stores 1/r^3 for all particle pairwise particle separations
        inv_r3 = (dx ** 2 + dy ** 2 + dz ** 2 + softening ** 2)
        inv_r3[inv_r3 > 0] = inv_r3[inv_r3 > 0] ** (-1.5)

        ax = G * (dx * inv_r3) @ mass
        ay = G * (dy * inv_r3) @ mass
        az = G * (dz * inv_r3) @ mass

        # pack together the acceleration components
        a = np.hstack((ax, ay, az))

        return a

    @staticmethod
    def getEnergy(pos, vel, mass, G):
        """
        Get kinetic energy (KE) and potential energy (PE) of simulation
        pos is N x 3 matrix of positions
        vel is N x 3 matrix of velocities
        mass is an N x 1 vector of masses
        G is Newton's Gravitational constant
        KE is the kinetic energy of the system
        PE is the potential energy of the system
        """
        # Kinetic Energy:
        KE = 0.5 * np.sum(np.sum(mass * vel ** 2))

        # Potential Energy:

        # positions r = [x,y,z] for all particles
        x = pos[:, 0:1]
        y = pos[:, 1:2]
        z = pos[:, 2:3]

        # matrix that stores all pairwise particle separations: r_j - r_i
        dx = x.T - x
        dy = y.T - y
        dz = z.T - z

        # matrix that stores 1/r for all particle pairwise particle separations
        inv_r = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        inv_r[inv_r > 0] = 1.0 / inv_r[inv_r > 0]

        # sum over upper triangle, to count each interaction only once
        PE = G * np.sum(np.sum(np.triu(-(mass * mass.T) * inv_r, 1)))

        return KE, PE;
