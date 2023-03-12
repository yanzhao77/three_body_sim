# -*- coding:utf-8 -*-
# title           :冥王星
# description     :冥王星（从太阳系的行星中排除）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Pluto(Body):
    """
    冥王星
    ------------------------
      转轴倾角: 119.591±0.014°
      自转周期: 6.39 地球日，自转角速度约为 -2.3474 度/小时（逆时针自转） = 360/(6.39*24)
    远日点距离: 49.305 天文单位(73.760 亿千米)
    近日点距离: 29.658 天文单位(44.368 亿千米)
      逃逸速度: 1.212 km/s
    　公转速度: 4.7 km/s
    　天体质量: 1.303✕10²² kg(±0.003)
    　平均密度: 1.854 g/cm³(±0.006) -> 1.854×10³ kg/m³
    """

    def __init__(self, name="Pluto", mass=1.303e22,
                 init_position=[40 * AU, 0, 0],
                 init_velocity=[0, 4.7, 0],
                 texture="pluto2.jpg", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=-2.3474):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.854e3,
            "color": (67, 28, 7),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed
        }
        super().__init__(**params)


if __name__ == '__main__':
    pluto = Pluto()
    print(pluto)
