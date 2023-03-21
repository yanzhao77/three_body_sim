# -*- coding:utf-8 -*-
# title           :北河三
# description     :北河三
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import FixedStar
from common.consts import MO


class Procyon(FixedStar):
    """
    TODO： 南河三(Procyon）
    质量：1.5太阳质量
    密度：1.8 g/cm³
    颜色值：#F5E8D5
    直径：1.84倍太阳直径

    中文名: 南河三
    外文名: Procyon
    别名: 小犬座α
    分类: 恒星
    发现者: 未知发现时间史前视星等约0.34绝对星等约2.67
    赤经: 7时39分18.1秒
    赤纬: +5°13′29″
    距地距离: 约 11.46 光年
    半长轴: 1.18"
    离心率: 0.36
    轨道倾角: 31.9 度
    年龄: 约1.7×1000000000年
    星表编号: IP 37279
    光谱类型: F5 IV-V
    星座: 小犬座
    星官: 南河（井宿，朱雀）
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
    from bodies import Sun
    fixed_star = Procyon()
    sun = Sun()
    print(fixed_star)
    print("质量倍数", fixed_star.mass / sun.mass)
    print("半径倍数", fixed_star.raduis / sun.raduis)