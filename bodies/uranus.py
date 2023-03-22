# -*- coding:utf-8 -*-
# title           :天王星
# description     :天王星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Uranus(Body):
    """
    天王星
    ------------------------
      转轴倾角: 97.77°
      自转周期: 17.24 小时，自转角速度约为 -20.8816 度/小时（逆时针自转） = 360/(17.24)
    远日点距离: 20.11 天文单位
    近日点距离: 18.33 天文单位
      逃逸速度: 21.3 km/s
    　公转速度: 6.81 km/s
    　天体质量: 8.681✕10²⁵ kg(±0.0013)
    　平均密度: 1.27 g/cm³ -> 1.27×10³ kg/m³
    """

    def __init__(self, name="天王星", mass=8.681e25,
                 init_position=[19 * AU, 0, 0],
                 init_velocity=[0, 6.81, 0],
                 texture="uranus.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=-20.8816, ignore_mass=False, trail_color=None):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.27e3,
            "color": (94, 124, 193),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass,
            "trail_color": trail_color
        }
        super().__init__(**params)


if __name__ == '__main__':
    uranus = Uranus()
    print(uranus)
