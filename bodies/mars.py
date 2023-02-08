# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Mars(Body):
    """
    火星
    ------------------------
    远日点距离: 1.666 天文单位
    近日点距离: 1.382 天文单位
    逃逸速度: 5.027 km/s
    　公转速度: 24.13 km/s
    　天体质量: 6.4171✕10²³
    　平均密度: 3.9335 g/cm³ -> 3.9335✕10³ kg/m³
    """
    def __init__(self, name="Mars", mass=6.4171e23,
                 init_position=[1.5 * AU, 0, 0],
                 init_velocity=[0, 24.13, 0],
                 texture="", size_scale=1.0, distance_scale=1.0):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 3.9335e3,
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
    mars = Mars()
    print(mars)