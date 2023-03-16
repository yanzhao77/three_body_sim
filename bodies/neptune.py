# -*- coding:utf-8 -*-
# title           :海王星
# description     :海王星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Neptune(Body):
    """
    海王星
    ------------------------
    自转轴倾角: 28.32°
      自转周期: 16.11 小时，自转角速度约为 22.3463 度/小时 = 360/(16.11)
    远日点距离: 30.33 天文单位
    近日点距离: 29.81 天文单位
      逃逸速度: 23.5 km/s
    　公转速度: 5.43 km/s
    　天体质量: 1.0241✕10²⁶ kg
    　平均密度: 1.638 g/cm³ -> 1.638×10³ kg/m³
    """

    def __init__(self, name="Neptune", mass=1.0241e26,
                 init_position=[30 * AU, 0, 0],
                 init_velocity=[0, 5.43, 0],
                 texture="neptune.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=22.3463):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.638e3,
            "color": (93, 118, 203),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed
        }
        super().__init__(**params)


if __name__ == '__main__':
    neptune = Neptune()
    print(neptune)
