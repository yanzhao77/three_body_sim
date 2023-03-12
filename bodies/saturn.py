# -*- coding:utf-8 -*-
# title           :土星
# description     :土星
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU


class Saturn(Body):
    """
    土星
    ------------------------
      自转倾角: 26.73 度
      自转周期: 10小时33分38秒
    远日点距离: 10.1238 天文单位
    近日点距离: 9.0412 天文单位
      逃逸速度: 35.49 km/s
    　公转速度: 9.64 km/s
    　天体质量: 5.6834✕10²⁶ kg
    　平均密度: 0.687 g/cm³ -> 0.687×10³ kg/m³
    """

    def __init__(self, name="Saturn", mass=5.6834e26,
                 init_position=[10 * AU, 0, 0],
                 init_velocity=[0, 9.64, 0],
                 texture="saturn.jpg", size_scale=1.0, distance_scale=1.0):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.687e3,
            "color": (219, 189, 159),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale
        }
        super().__init__(**params)

    @property
    def has_rings(self):
        """
        土星带光环的天体
        :return:
        """
        return True

    @property
    def rings_color(self):
        """
        土星光环的颜色
        :return:
        """
        return 173, 121, 92


if __name__ == '__main__':
    saturn = Saturn()
    print(saturn)
