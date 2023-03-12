# -*- coding:utf-8 -*-
# title           :水星
# description     :水星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Mercury(Body):
    """
    水星
    ------------------------
      转轴倾角: 0.034°
      自转周期: 58.65 地球日，自转角速度约为 0.2558 度/小时 = 360/(58.65*24)
    远日点距离: 0.466697 天文单位
    近日点距离: 0.307499 天文单位
      逃逸速度: 4.25 km/s
    　公转速度: 47.87 km/s
    　天体质量: 3.3011✕10²³ kg
    　平均密度: 5.427 g/cm³ -> 5.427×10³ kg/m³
    """

    def __init__(self, name="Mercury", mass=3.3011e23,
                 init_position=[0.4 * AU, 0, 0],
                 init_velocity=[0, 47.87, 0],
                 texture="mercury.jpg", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.2558):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 5.427e3,
            "color": (1, 89, 162),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed
        }
        super().__init__(**params)


if __name__ == '__main__':
    mercury = Mercury()
    print(mercury)
