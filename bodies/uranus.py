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
      自转周期: 17时14分24秒
    远日点距离: 20.11 天文单位
    近日点距离: 18.33 天文单位
      逃逸速度: 21.3 km/s
    　公转速度: 6.81 km/s
    　天体质量: 8.681✕10²⁵ kg(±0.0013)
    　平均密度: 1.27 g/cm³ -> 1.27×10³ kg/m³
    """

    def __init__(self, name="Uranus", mass=8.681e25,
                 init_position=[19 * AU, 0, 0],
                 init_velocity=[0, 6.81, 0],
                 texture="uranus.jpg", size_scale=1.0, distance_scale=1.0):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.27e3,
            "color": (94, 124, 193),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale
        }
        super().__init__(**params)


if __name__ == '__main__':
    uranus = Uranus()
    print(uranus)
