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
    船底座V382（CarinaeV382）
    --------------- 维基百科 ---------------
    船底座V382
    V382 Carinae.jpg
    船底座V382位于照片中央
    观测资料
    历元 J2000.0
    星座	船底座
    星官	近南极星区 海石
    赤经	11h08m35.4s
    赤纬	−58°58′30″
    视星等（V）	+3.93
    特性
    光谱分类	G0I-a0 var
    U−B 色指数	+0.94
    B−V 色指数	+1.23
    变星类型	造父变星
    天体测定
    径向速度 (Rv)	+7 km/s
    自行 (μ)	赤经：−5.03 mas/yr
    赤纬：2.09 mas/yr
    视差 (π)	0.55 ± 0.54 mas
    距离	> 5900 ly
    (> 1800 pc)
    绝对星等 (MV)	−7.36
    详细资料
    质量	39 M☉
    半径	747 R☉
    亮度	71500（可见光）L⊙/480000（辐射热）L⊙ L☉
    温度	5550或4420 (以B-V) K
    其他命名
    x Carinae, HR 4337, HD 96918, CP−58°3189, FK5 1289, HIP 54463, SAO 238813, GC 15329
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="船底座V382", mass=39 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(255, 172, 40),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.26, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.0001317362984479511,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = CarinaeV382()
    print(fixed_star)
    fixed_star.compare_with_sun()
    fixed_star.density_by_radius(num_sun_raduis=747)
