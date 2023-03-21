# -*- coding:utf-8 -*-
# title           :天体系统
# description     :天体系统，多个天体就是一个系统
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
import numpy as np
import math
from common.consts import AU, G
from bodies import Body, Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto
from common.func import calculate_distance


class System(object):
    """
    天体系统
    """

    def __init__(self, bodies, max_distance=200 * AU, ignore_mass=False):
        """

        :param bodies:
        :param max_distance:系统的最大范围，超出范围的天体就不显示了
        """
        self.bodies = bodies
        if ignore_mass:
            for body in self.bodies:
                body.ignore_mass = True
        # self.adjust_distance_and_velocity()
        self.max_distance = max_distance

    @staticmethod
    def calc_body_new_velocity_position(body, sun_mass=1.9891e30, G=6.674e-11):
        old_velocity = body.init_velocity
        old_position = body.init_position

        old_distance = np.linalg.norm(old_position - [0, 0, 0], axis=-1)
        new_distance = old_distance * body.distance_scale
        new_position = old_position * body.distance_scale

        new_velocity = System.get_new_velocity(old_velocity, old_distance, new_distance, body.mass)

        return new_velocity, new_position

    @staticmethod
    def get_new_velocity(old_velocity, old_distance, new_distance, mass, sun_mass=1.9891e30, G=6.674e-11):
        # 计算原速度的模长
        old_speed = np.linalg.norm(old_velocity * 1000)
        # 计算原动能和原势能
        old_kinetic_energy = 0.5 * mass * old_speed ** 2
        old_potential_energy = - G * mass * sun_mass / old_distance

        new_potential_energy = - G * mass * sun_mass / new_distance

        # 计算新动能
        new_kinetic_energy = old_kinetic_energy
        # 计算新速度的模长
        new_speed = math.sqrt(2 * (new_kinetic_energy - old_potential_energy) / mass)
        # 计算新速度向量
        new_velocity = old_velocity / old_speed * new_speed / 1000
        return new_velocity

    def get_new_velocity1(old_velocity, old_distance, new_distance, mass, sun_mass=1.9891e30, G=6.674e-11):
        # 计算原来的速度
        old_speed = math.sqrt(G * sun_mass / old_distance)
        # 计算新的速度
        new_speed = math.sqrt(G * sun_mass / new_distance)
        # 计算原来的动能
        old_kinetic_energy = 0.5 * mass * old_velocity ** 2
        # 计算新的动能
        new_kinetic_energy = old_kinetic_energy * new_speed ** 2 / old_speed ** 2
        # 计算新的速度
        new_velocity = math.sqrt(2 * new_kinetic_energy / mass)
        return new_velocity

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

    def save_to_json(self, json_file_name, params=None):
        """

        :param json_file_name:
        :param params:
        :return:
        """
        import json
        import os
        # json_file = os.path.join("../data", json_file_name)
        filed_names = ["name", "mass", "init_position", "init_velocity",
                       "density", "color", "texture",
                       "size_scale", "distance_scale",  # "parent"
                       "rotation_speed", "ignore_mass", "is_fixed_star"]
        bodies = []
        for b in self.bodies:
            body = {}
            for filed_name in filed_names:
                filed_value = getattr(b, filed_name)
                if type(filed_value) is np.ndarray:
                    filed_value = filed_value.tolist()
                body[filed_name] = filed_value
            bodies.append(body)
        data = {"bodies": bodies}
        if params is not None:
            data["params"] = params
        json_str = json.dumps(data, indent=2, ensure_ascii=False, separators=(',', ': '))
        with open(json_file_name, "w", encoding='utf-8') as f:
            f.write(json_str)

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
            # if self.max_distance > 0:
            #     # 超过了 max_distance 距离，则不显示，并消失
            #     if calculate_distance(body.position) > self.max_distance:
            #         body.appeared = False
            #         return False

            return True

        # self.bodies = list(filter(valid_body, self.bodies))

        for body1 in self.bodies:
            if body1.ignore_mass:
                continue
            if not valid_body(body1):
                continue
            acceleration = np.zeros(3)
            for body2 in self.bodies:
                if body2.ignore_mass:
                    continue
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
    # body_sys = System([
    #     Sun(),  # 太阳
    #     Mercury(),  # 水星
    #     Venus(),  # 金星
    #     Earth(),  # 地球
    #     Mars(),  # 火星
    #     Jupiter(),  # 木星
    #     Saturn(),  # 土星
    #     Uranus(),  # 天王星
    #     Neptune(),  # 海王星
    #     Pluto()  # 冥王星(从太阳系的行星中排除)
    # ])
    # import math
    #
    # mass = 2e30
    # r = 2 * AU
    # # p = 14.9
    # p = 14.89
    # bodies = [
    #     Sun(name="太阳A红色", mass=mass,
    #         init_position=[0, r * math.sqrt(3), 0],  # 位置
    #         init_velocity=[-p, 0, 0],  # 速度（km/s）
    #         size_scale=5e1, texture="sun2.jpg", color=(255, 0, 0)),  # 太阳放大 100 倍
    #     Sun(name="太阳B绿色", mass=mass,
    #         init_position=[-r, 0, 0],
    #         init_velocity=[1 / 2 * p, -math.sqrt(3) / 2 * p, 0],
    #         size_scale=5e1, texture="sun2.jpg", color=(0, 255, 0)),  # 太阳放大 100 倍
    #     Sun(name="太阳C蓝色", mass=mass,
    #         init_position=[r, 0, 0],
    #         init_velocity=[1 / 2 * p, math.sqrt(3) / 2 * p, 0],
    #         size_scale=5e1, texture="sun2.jpg", color=(0, 0, 255)),  # 太阳放大 100 倍
    #     Earth(name="地球",
    #           # init_position=[0, -AU * -2, 5 * AU],
    #           init_position=[0, math.sqrt(3) * r / 6, 5 * AU],
    #           init_velocity=[0, 0, -10],
    #           size_scale=4e3, distance_scale=1),  # 地球放大 4000 倍，距离保持不变
    # ]
    # body_sys = System(bodies)
    # print(body_sys.save_to_json("../data/tri_bodies_sim_perfect_01.json"))
    earth = Earth(name="地球",
                  # init_position=[0, -AU * -2, 5 * AU],
                  init_position=[0, 1000000, 500000],
                  init_velocity=[0, 0, -10],
                  size_scale=4e3, distance_scale=1)
    new_velocity, new_position = System.calc_body_new_velocity_position(earth)

    print(new_velocity, new_position)
    print(earth.init_velocity, earth.init_position)
