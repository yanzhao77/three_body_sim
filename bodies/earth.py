# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from bodies.body import Body


class Earth(Body):
    """
    地球
    ------------------------
     远日点距离: 152097701 km
     近日点距离: 147098074 km
     　逃逸速度: 11.186 km/s
     　公转速度: 29.79 km/s
     　天体质量: 5.97237✕10²⁴ kg
     　平均密度: 5507.85 kg/m³
    """

    def __init__(self, name="earth", mass=5.97237e24,
                 init_position=[149597870.700, 0, 0],
                 init_velocity=[0, 29.79, 0],
                 texture="", size_scale=1.0, distance_scale=1.0):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 5507.85,
            "color": [
                125,
                125,
                125
            ],
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale
        }
        super().__init__(**params)


if __name__ == '__main__':
    earth = Earth()
    print(earth)
