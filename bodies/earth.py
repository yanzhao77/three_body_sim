# -*- coding:utf-8 -*-
# title           :地球
# description     :地球
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Earth(Body):
    """
    地球
    ------------------------
      转轴倾角: 23.44°
      自转周期: 23.93 小时，自转角速度约为 15 度/小时
    远日点距离: 152097701 km
    近日点距离: 147098074 km
    　逃逸速度: 11.186 km/s
    　公转速度: 29.79 km/s
    　天体质量: 5.97237✕10²⁴ kg
    　平均密度: 5507.85 kg/m³
    """

    def __init__(self, name="Earth", mass=5.97237e24,
                 init_position=[1.12 * AU, 0, 0],
                 init_velocity=[0, 29.79, 0],
                 texture="earth1.jpg", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=15):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 5507.85,
            "color": (1, 89, 162),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed
        }
        super().__init__(**params)


if __name__ == '__main__':
    earth = Earth()
    print(earth)
