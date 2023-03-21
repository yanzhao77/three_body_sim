# -*- coding:utf-8 -*-
# title           :北河三
# description     :北河三
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar, Sun
from common.consts import MO


class Procyon(FixedStar):
    """
    TODO： 南河三(Procyon）
    质量：1.5太阳质量
    密度：1.8 g/cm³
    颜色值：#F5E8D5
    直径：1.84倍太阳直径

    中文名南河三外文名Procyon别    名小犬座α分    类恒星发现者未知发现时间史前视星等约0.34绝对星等约2.67赤    经7时39分18.1秒赤    纬+5°13′29″距地距离约 11.46 光年半长轴1.18"离心率0.36轨道倾角31.9 度年    龄约1.7×1000000000年星表编号HIP 37279光谱类型F5 IV-V星    座小犬座星    官南河（井宿，朱雀）
    ------------------------
    == 太阳参数 ==
    自转周期: 24.47 地球日，自转角速度约为 0.6130 度/小时 = 360/(24.47*24)
    天体质量: 1.9891×10³⁰ kg
    平均密度: 1.408×10³ kg/m³
    """

    def __init__(self, name="南河三", mass=1.5 * MO,
                 init_position=[0, 0, 0],
                 init_velocity=[0, 0, 0],
                 color=(0xF5, 0xE8, 0xD5),
                 texture="fixed_star.png", size_scale=1.0, distance_scale=1.0,
                 rotation_speed=0.1, ignore_mass=False):
        params = {
            "name": name,
            "mass": mass,
            "init_position": init_position,
            "init_velocity": init_velocity,
            "density": 0.5e3,
            "color": color,
            "texture": texture,
            "size_scale": size_scale,
            "distance_scale": distance_scale,
            "rotation_speed": rotation_speed,
            "ignore_mass": ignore_mass
        }
        super().__init__(**params)


if __name__ == '__main__':
    fixed_star = Procyon()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)