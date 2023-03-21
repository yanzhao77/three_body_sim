# -*- coding:utf-8 -*-
# title           :太阳
# description     :太阳
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body


class DysenSphere(Body):
    """
    戴森球
    ------------------------
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="戴森球", mass=2e28,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(170, 98, 25),
                 texture="dysen_sphere.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1,
                 parent=None):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.6,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "parent": parent
        }
        super().__init__(**params)
        self.ignore_mass = True
        # 灯光禁用
        self.light_disable = True

    def ignore_gravity(self, body):
        """
        是否忽略引力
        :param body:
        :return:
        """
        return True


if __name__ == '__main__':
    print(DysenSphere())
