# -*- coding:utf-8 -*-
# title           :ursina天体运行模拟器事件传递
# description     :ursina天体运行模拟器事件传递
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
        UrsinaEvent.on_searching_bodies_funcs = []
        UrsinaEvent.on_application_run_callback = []

    @staticmethod
    def on_application_run_callback_subscription(fun):
        UrsinaEvent.on_application_run_callback.append(fun)

    @staticmethod
    def on_searching_bodies_subscription(subscription_name, fun):
        UrsinaEvent.on_searching_bodies_funcs.append((subscription_name, fun))

    @staticmethod
    def on_reset_subscription(fun):
        UrsinaEvent.on_reset_funcs.append(fun)

    @staticmethod
    def on_reset():
        for f in UrsinaEvent.on_reset_funcs:
            f()

    @staticmethod
    def on_application_run():
        if len(UrsinaEvent.on_application_run_callback) == 0:
            return
        for f in UrsinaEvent.on_application_run_callback:
            f()
        UrsinaEvent.on_application_run_callback.clear()

    @staticmethod
    def on_searching_bodies(**kwargs):
        results = []
        for subscription_name, fun in UrsinaEvent.on_searching_bodies_funcs:
            results.append((subscription_name, fun(**kwargs)))
        return results


UrsinaEvent.init()
