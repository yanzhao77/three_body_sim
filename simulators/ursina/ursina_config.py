# -*- coding:utf-8 -*-
# title           :ursina天体运行模拟器
# description     :ursina天体运行模拟器
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina


class UrsinaConfig:
    # 常量定义
    # 天体缩放的因子（不能太大，否则无法容得下大数量级的天体）调整 5e-7 最佳
    SCALE_FACTOR = 5e-7
    # 旋转因子为1，则为正常的转速
    ROTATION_SPEED_FACTOR = 1.0
    # ROTATION_SPEED_FACTOR = 0.01

    # 中文字体（微软雅黑）
    CN_FONT = "msyhl.ttc"  # 'simsun.ttc' 仿宋体
    # CN_FONT = 'simsun.ttc'  #  仿宋体

    # 速度的倍数
    __run_speed_factor = 1.0

    # 天体自旋倍数
    __body_spin_factor = 1.0

    # 摄像机
    __camera_factor = 1.0

    __on_reset_funcs = []

    show_trail = False
    # 拖尾球体的数量
    trail_length = 200
    # 默认秒数（0表示默认）
    seconds_per = 0
    # # 控制摄像机动作速度（天体越大，速度越快，天体越小，速度越慢）
    # control_camera_speed = 1

    __body_size_factor = 1.0

    @property
    @classmethod
    def run_speed_factor(cls):
        return cls.__run_speed_factor

    @run_speed_factor.setter
    @classmethod
    def run_speed_factor(cls, value):
        cls.__run_speed_factor = value

    @property
    @classmethod
    def body_spin_factor(cls):
        return cls.__body_spin_factor

    @body_spin_factor.setter
    @classmethod
    def body_spin_factor(cls, value):
        cls.__body_spin_factor = value

    @property
    @classmethod
    def body_size_factor(cls):
        return cls.__body_size_factor

    @body_size_factor.setter
    @classmethod
    def body_spin_factor(cls, value):
        cls.__body_size_factor = value

    @classmethod
    def on_reset_subscription(cls, fun):
        cls.__on_reset_funcs.append(fun)

    @classmethod
    def on_reset(cls):
        for f in cls.__on_reset_funcs:
            f()


# 初始化
UrsinaConfig.run_speed_factor = 1.0
UrsinaConfig.body_spin_factor = 1.0
UrsinaConfig.body_size_factor = 1.0

if __name__ == '__main__':
    UrsinaConfig.run_speed_factor = 2.0
    print(UrsinaConfig.run_speed_factor)
