# -*- coding:utf-8 -*-
# title           :天体系统
# description     :天体系统，多个天体就是一个系统
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
import numpy as np
from common.consts import AU, G
from bodies import Body, Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
from common.func import calculate_distance


class System(object):
    """
    天体系统
    """

    def __init__(self, bodies, max_distance=200 * AU):
        """

        :param bodies:
        :param max_distance:系统的最大范围，超出范围的天体就不显示了
        """
        self.bodies = bodies
        self.max_distance = max_distance

    def add(self, body):
        self.bodies.append(body)

    def total_mass(self):
        """
        总质量
        :return:
        """
        total_mass = 0.0
        for body in self.bodies:
            total_mass += body.mass
        return total_mass

    def __repr__(self):
        return 'System({})'.format(self.bodies)

    def center_of_mass(self):
        """
        质心
        :return:
        """
        r = np.zeros(2)
        for body in self.bodies:
            r = body.mass * body.position
        return r / self.total_mass()

    def evolve(self, dt):
        """

        :param dt:
        :return:
        """
        self.calc_bodies_acceleration()

        for body in self.bodies:
            # acceleration 加速度
            body.velocity += body.acceleration * dt
            # body.position += 0.5 * body.acceleration * (dt ** 2)
            body.position += body.velocity * dt

    def calc_bodies_acceleration(self):
        """
        计算加速度
        :return:
        """

        def valid_body(body):
            """
            判断是否为有效的天体
            :param body:
            :return:
            """
            if not body.appeared:  # 不显示
                return False
            if self.max_distance > 0:
                # 超过了 max_distance 距离，则不显示，并消失
                if calculate_distance(body.position) > self.max_distance:
                    body.appeared = False
                    return False

            return True

        # self.bodies = list(filter(valid_body, self.bodies))

        for body1 in self.bodies:
            if not valid_body(body1):
                continue
            acceleration = np.zeros(3)
            for body2 in self.bodies:
                if self.max_distance > 0:
                    if calculate_distance(body1.position) > self.max_distance:  # 超过了max_distance距离，则消失
                        body1.appeared = False
                    if calculate_distance(body2.position) > self.max_distance:  # 超过了max_distance距离，则消失
                        body2.appeared = False

                if False == body1.appeared or body2.appeared == False:
                    continue

                if body1 is body2:
                    continue
                elif body1.ignore_gravity(body2) or body2.ignore_gravity(body1):
                    continue

                r = body2.position - body1.position
                # G = 6.67e-11 # 万有引力常数
                # m/s² = kg * m / m**3
                # km/s² = kg * m / m**3 / 1e9
                # acceleration = G * body2.mass * dx / (d ** 3)
                acceleration += (G * body2.mass * r / np.linalg.norm(r) ** 3) / 1e9

            body1.acceleration = acceleration


if __name__ == '__main__':
    body_sys = System([
        Sun(),  # 太阳
        Mercury(),  # 水星
        Venus(),  # 金星
        Earth(),  # 地球
        Mars(),  # 火星
        Jupiter(),  # 木星
        Saturn(),  # 土星
        Uranus(),  # 天王星
        Neptune(),  # 海王星
        Pluto()  # 冥王星(从太阳系的行星中排除)
    ])

    print(body_sys)
