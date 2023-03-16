# -*- coding:utf-8 -*-
# title           :ursina天体运行模拟器
# description     :ursina天体运行模拟器
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina


class UrsinaEvent:
    """

    """

    @staticmethod
    def init():
        if hasattr(UrsinaEvent, "on_reset_funcs"):
            return
        UrsinaEvent.on_reset_funcs = []

    @staticmethod
    def on_reset_subscription(fun):
        UrsinaEvent.on_reset_funcs.append(fun)

    @staticmethod
    def on_reset():
        for f in UrsinaEvent.on_reset_funcs:
            f()


UrsinaEvent.init()
