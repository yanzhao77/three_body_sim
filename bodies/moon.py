# -*- coding:utf-8 -*-
# title           :月球
# description     :月球
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies.body import Body, AU
from bodies import Earth


class Moon(Body):
    """
    月球
    ------------------------
    　自转周期: 27.32 地球日，自转角速度约为 0.5487 度/小时 = 360/(27.32*24)
    距地距离约: 363104 至 405696 km
    　逃逸速度: 2.4 km/s
    　公转速度: 1.023 km/s + (地球)29.79 km/s
    　天体质量: 7.342✕10²² kg
    　平均密度: 3.344 g/cm³ -> 3.344✕10³ kg/m³
    """

    def __init__(self, name="月球", mass=7.342e22,
                 init_position=[363104 + 1.12 * AU, 0, 0],
                 init_velocity=[0, 29.79 + 1.023, 0],
                 texture="moon.jpg", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.5487):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 3.344e3,
            "color": (162, 162, 162),
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed
        }
        super().__init__(**params)

    # def ignore_gravity(self, body):
    #     """
    #     是否忽略引力
    #     :param body:
    #     :return:
    #     """
    #     # 月球只对地球有引力，忽略其他的引力
    #     if isinstance(body, Earth):
    #         return False
    #
    #     return True


if __name__ == '__main__':
    moon = Moon()
    print(moon)
