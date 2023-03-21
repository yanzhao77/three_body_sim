# -*- coding:utf-8 -*-
# title           :金星
# description     :金星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Venus(Body):
    """
    金星
    ------------------------
      轨道倾角: 3.39458 度
      自转周期: 243 地球日，自转角速度约为 -0.0617 度/小时（逆时针自转） = 360/(243*24)
    远日点距离: 0.728213 天文单位
    近日点距离: 0.718440天文单位
      逃逸速度: 10.36 km/s
    　公转速度: 35 km/s
    　天体质量: 4.8675✕10²⁴ kg
    　平均密度: 5.24g/cm3 -> 5.24×10³ kg/m³
    """

    def __init__(self, name="金星", mass=4.8675e24,
                 init_position=[0.72 * AU, 0, 0],
                 init_velocity=[0, 35, 0],
                 texture="venus.jpg", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=-0.0617):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 5.24e3,
            "color": (173, 81, 5),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed
        }
        super().__init__(**params)


if __name__ == '__main__':
    venus = Venus()
    print(venus)
