# -*- coding:utf-8 -*-
# title           :太阳系场景模拟3
# description     :太阳系场景模拟（展示的效果非太阳系真实的距离和大小，加入了小行星的演示效果）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from bodies import Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Asteroid
from bodies.body import AU
from common.consts import SECONDS_PER_WEEK
from common.func import get_positions_velocitys
from scenes.func import mayavi_run
import numpy as np

if __name__ == '__main__':
    # 八大行星：木星(♃)、土星(♄)、天王星(♅)、海王星(♆)、地球(⊕)、金星(♀)、火星(♂)、水星(☿)
    # 排列顺序
    # 1、体积：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 1330：745：65：60：1：0.86：0.15：0.056
    # 2、质量：(以地球为1)木星 ：土星 ：天王星 ：海王星 ：地球 ：金星 ：火星 ：水星 = 318：95：14.53：17.15：1：0.8：0.11：0.0553
    # 3、离太阳从近到远的顺序：水星、金星、地球、火星、木星、土星、天王星、海王星
    #  =====================================================================
    #  以下展示的效果非太阳系真实的距离和大小
    #  1、由于宇宙空间尺度非常大，按照实际的大小无法看到行星天体，因此需要对天体的尺寸进行放大
    #  2、为了达到最佳的显示效果，对每个行星天体的距离进行了缩放
    #  3、加入了小行星的演示效果

    # region 1.构建4个小行星 -------------
    # asteroids = [
    #     Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
    #              init_position=[1.6 * AU, 0, 0],
    #              init_velocity=[0, 25.37, 0],
    #              distance_scale=1),
    #     Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
    #              init_position=[-1.6 * AU, 0, 0],
    #              init_velocity=[0, -25.37, 0],
    #              distance_scale=1),
    #     Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
    #              init_position=[0, 1.6 * AU, 0],
    #              init_velocity=[-25.37, 0, 0],
    #              distance_scale=1),
    #     Asteroid(size_scale=1e9,  # 小行星放大 1000000000 倍，距离保持不变
    #              init_position=[0, -1.6 * AU, 0],
    #              init_velocity=[25.37, 0, 0],
    #              distance_scale=1),
    # ]
    # endregion 1 --------------------------

    # region 2.随机构建 60 小行星，注意：太多的小行星会影响电脑性能
    NUM_OF_ASTEROIDS = 60
    asteroids = []
    angles = np.linspace(0, 40 * np.pi, NUM_OF_ASTEROIDS)
    pxs, pys, vxs, vys = get_positions_velocitys(angles,
                                                 radius=1.60 * AU,
                                                 velocity=23.37,
                                                 radius_offset=0.1 * AU,
                                                 velocity_offset=0.2)
    for i, px in enumerate(pxs):
        py, fx, fy = pys[i], vxs[i], vys[i]
        asteroids.append(Asteroid(size_scale=5e9,  # 小行星放大 5000000000 倍，距离放大 1.4 倍
                                  init_position=[px, py, 0],
                                  init_velocity=[fx, fy, 0],
                                  distance_scale=1.4))
    # endregion 2

    # region 3.构建太阳系
    bodies = [
        Sun(size_scale=0.8e2),                            # 太阳放大 80 倍
        Mercury(size_scale=4e3, distance_scale=1.3),      # 水星放大 4000 倍，距离放大 1.3 倍
        Venus(size_scale=4e3, distance_scale=1.3),        # 金星放大 4000 倍，距离放大 1.3 倍
        Earth(size_scale=4e3, distance_scale=1.3),        # 地球放大 4000 倍，距离放大 1.3 倍
        Mars(size_scale=4e3, distance_scale=1.3),         # 火星放大 4000 倍，距离放大 1.3 倍
        Jupiter(size_scale=0.68e3, distance_scale=0.65),  # 木星放大 680 倍，距离缩小到真实距离的 0.65
        Saturn(size_scale=0.68e3, distance_scale=0.52),   # 土星放大 680 倍，距离缩小到真实距离的 0.52
        Uranus(size_scale=0.8e3, distance_scale=0.36),    # 天王星放大 800 倍，距离缩小到真实距离的 0.36
        Neptune(size_scale=1e3, distance_scale=0.27),     # 海王星放大 1000 倍，距离缩小到真实距离的 0.27
        Pluto(size_scale=10e3, distance_scale=0.23),      # 冥王星放大 10000 倍，距离缩小到真实距离的 0.23(从太阳系的行星中排除)
    ]
    # 增加小行星到太阳系
    bodies += asteroids
    # endregion 3

    # mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45)
    mayavi_run(bodies, SECONDS_PER_WEEK, view_azimuth=-45, view_distance=3e9, view_focalpoint=[5e2, 5e2, 5e2])
