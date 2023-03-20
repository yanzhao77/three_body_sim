# -*- coding:utf-8 -*-
# title           :ursina天体运行模拟器UI控制
# description     :ursina天体运行模拟器UI控制
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from ursina import Ursina, window, Entity, Grid, Mesh, camera, Text, application, color, mouse, Vec2, Vec3, \
    load_texture, held_keys, Button, ButtonList, destroy, scene, distance, Sequence, Wait, Func
from ursina.prefabs.first_person_controller import FirstPersonController
from common.consts import SECONDS_PER_HOUR, SECONDS_PER_HALF_DAY, \
    SECONDS_PER_DAY, SECONDS_PER_WEEK, SECONDS_PER_MONTH, SECONDS_PER_YEAR
from common.consts import AU
from simulators.ursina.ui_component import UiSlider, SwithButton, UiButton, Buttons
from simulators.ursina.ursina_config import UrsinaConfig
from simulators.ursina.ursina_event import UrsinaEvent
from ursina import WindowPanel, InputField, Button, Slider, ButtonGroup, Panel, invoke
from simulators.ursina.ui.event_handler import EventHandler


class UiPanel(WindowPanel):
    """
    界面面板类
    """
    def __init__(self, handler: EventHandler, position=(0, 0), enabled=False, title=''):
        """

        @param handler: 事件处理类
        @param position: 界面位置
        @param enabled: 是否显示
        @param title: 标题
        """
        self.components = self.component_init()
        self.handler = handler
        self.handler.ui = self
        self.event_handler_init()

        super().__init__(title=title, content=self.components, ignore_paused=True, color=color.rgba(0.0, 0.0, 0.0, 0.5))

        self.y = position[1]  # wp.panel.scale_y / 2 * wp.scale_y  # center the window panel
        self.x = position[0]  # wp.scale_x + 0.1
        self.enabled = enabled
        self.after_component_init()

    def after_component_init(self):
        """
        组件初始化后运行
        """
        pass

    def component_init(self):
        """
        组件初始化
        """
        pass

    def event_handler_init(self):
        """
        事件处理初始化
        @return:
        """
        pass

    def show_message(self, message, close_time=3):
        """
        显示消息框
        :param message: 消息内容
        :param close_time: 定义显示消息框关闭时间
        :return:
        """
        # 创建消息框
        message_box = Text(text=message, font=UrsinaConfig.CN_FONT, background=True, origin=(0, 0), y=.25)
        close_time = close_time * application.time_scale

        # 定义关闭函数
        def close_message():
            destroy(message_box)

        s = Sequence(
            Wait(close_time),
            Func(close_message)
        )
        s.start()
