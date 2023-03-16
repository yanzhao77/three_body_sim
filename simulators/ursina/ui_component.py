# -*- coding:utf-8 -*-
# title           :ursina UI组件
# description     :ursina UI组件
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from ursina import Ursina, window, Entity, Grid, Mesh, camera, Text, application, color, mouse, Vec2, Vec3, \
    load_texture, held_keys, Button
from ursina.prefabs.first_person_controller import FirstPersonController
from simulators.ursina.ursina_config import UrsinaConfig
from simulators.ursina.ursina_event import UrsinaEvent
from ursina import WindowPanel, InputField, Button, Slider, ButtonGroup


class UiSlider(Slider):
    def __init__(self, text, min=0.01, max=3, default=1):
        super().__init__(text=text,
                         height=Text.size,
                         y=-.6,
                         step=.01,
                         min=min,
                         max=max,
                         default=default,
                         color=color.rgba(0.0, 0.0, 0.0, 0.5))
        self.label.scale = 1
        self.height = Text.size/1.2
        # self.text_entity
        # self.update()


class SwithButton(ButtonGroup):
    def __int__(self, options, default):
        super().__init__(options, min_selection=1, y=0, default=default,
                    selected_color=color.green, ignore_paused=True,
                    color=color.rgba(0.0, 0.0, 0.0, 0.5))
        self.label.scale = 0.8