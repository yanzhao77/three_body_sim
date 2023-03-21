# -*- coding:utf-8 -*-
# title           :船底座V382
# description     :船底座V382
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class CarinaeV382(FixedStar):
    """
    TODO： 船底座V382（CarinaeV382）
    质量:为20太阳质量  质    量20 M⊙ [2]
    大小:为350太阳半径    半    径700 ± 250 R☉
    颜色:为0xFF, 0xBF, 0x00
    密度:为0.008 g/cm³

    中文名船底座V382外文名V382 Carinae别
    名船底座x、海石增四分    类黄特超巨星
    质    量20 M⊙ [2]
    表面温度5200 K [2] 视星等3.93 等绝对星等-9 等 [1] 赤    经11时08分35.39秒 [3] 赤    纬-58°58′30.14″ [3] 距地距离约 8900 光年 [1]
    半    径700 ± 250 R☉ [4] 光    度316,000 L☉ [1]
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="船底座V382", mass=20 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xFF, 0xBF, 0x00),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 1.408e3,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    from bodies import Sun
    fixed_star = CarinaeV382()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)