# -*- coding:utf-8 -*-
# title           :
# description     :
# author          :Python超人
# date            :2023-01-22
# notes           :
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Asteroid(Body):
    """
    小行星
质量 (kg):~4.1×1010 kg
密度 :2.3±0.3 g/cm&sup3;
    ------------------------
    小行星带距离太阳约2.17-3.64天文单位的空间区域内，聚集了大约50万颗以上的小行星。
    这么多小行星能够被凝聚在小行星带中，除了太阳的引力作用以外，木星的引力也起着作用。
    [小行星25143的数据如下]:
     远日点距离: 253.520Gm (1.695AU)
     近日点距离: 142.568Gm (0.953AU)
       逃逸速度: 0.0002 km/s
     　公转速度: 25.37 km/s
     　天体质量: 4.1✕10¹⁰ kg
     　平均密度: 2.3✕10³ kg/m³
    """

    def __init__(self, name="Asteroid", mass=4.1e10,
                 init_position=[1.5 * AU, 0, 0],
                 init_velocity=[0, 25.37, 0],
                 texture="", size_scale=1.0, distance_scale=1.0):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 2.3e10,
            "color": (179, 231, 255),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale
        }
        super().__init__(**params)


if __name__ == '__main__':
    asteroid = Asteroid()
    print(asteroid)
