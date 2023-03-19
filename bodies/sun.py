# -*- coding:utf-8 -*-
# title           :太阳
# description     :太阳
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body


class Sun(Body):
    """
    太阳
    ------------------------
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="Sun", mass=1.9891e30,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(170, 98, 25),
                 texture="sun2.jpg", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.6130):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.408e3,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed
        }
        super().__init__(**params)

    @property
    def is_fixed_star(self):
        """
        太阳为恒星
        :return:
        """
        return True


if __name__ == '__main__':
    print(Sun())
