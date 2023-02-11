# -*- coding:utf-8 -*-
# title           :木星
# description     :木星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Jupiter(Body):
    """
    木星
    ------------------------
    远日点距离: 5.4588 天文单位
    近日点距离: 4.9501 天文单位
    　逃逸速度: 59.5 km/s
    　公转速度: 13.06 km/s
    　天体质量: 1.8982✕10²⁷ kg(317.8 M⊕)
    　平均密度: 1.326 g/cm³ -> -> 1.326✕10³ kg/m³
    """

    def __init__(self, name="Jupiter", mass=1.8982e27,
                 init_position=[5.2 * AU, 0, 0],
                 init_velocity=[0, 13.06, 0],
                 texture="jupiter1.jpg", size_scale=1.0, distance_scale=1.0):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.326e3,
            "color": (173, 121, 92),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale
        }
        super().__init__(**params)


if __name__ == '__main__':
    jupiter = Jupiter()
    print(jupiter)
