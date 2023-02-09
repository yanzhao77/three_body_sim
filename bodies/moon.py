# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Moon(Body):
    """
    月球
    ------------------------
     距地距离约 363104 至 405696 km
     　逃逸速度: 2.4 km/s
     　公转速度: 1.023 km/s + (地球)29.79 km/s
     　天体质量: 7.342✕10²² kg
     　平均密度: 3.344 g/cm³ -> 3.344✕10³ kg/m³
    """

    # 质    量约  [1] 平均密度约 3.344 g/cm³ [1] 质    量约 7.342✕1022 kg [1]
    def __init__(self, name="Moon", mass=7.342e22,
                 init_position=[363104 + 1.12 * AU, 0, 0],
                 init_velocity=[0, 29.79 + 1.023, 0],
                 texture="moon.jpg", size_scale=1.0, distance_scale=1.0):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 3.344e3,
            "color": (162, 162, 162),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale
        }
        super().__init__(**params)


if __name__ == '__main__':
    earth = Earth()
    print(earth)
