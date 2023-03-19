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
from simulators.ursina.ui.control_handler import ControlHandler
from simulators.ursina.ui.ui_panel import UiPanel
from simulators.ursina.ui_component import UiSlider, SwithButton, UiButton, Buttons
from simulators.ursina.ursina_config import UrsinaConfig
from simulators.ursina.ursina_event import UrsinaEvent
from ursina import WindowPanel, InputField, Button, Slider, ButtonGroup, Panel, invoke


class ControlUI(UiPanel):
    def component_init(self):
        self.start_button_text = "●"  # 》●▲○◎
        self.pause_button_text = "〓"  # 〓 || ‖
        self.no_trail_button_text = "○ "
        self.trail_button_text = "○--"

        self.slider_body_spin_factor = UiSlider(text='自转速度', min=0.01, max=30, default=1)
        self.slider_body_size_factor = UiSlider(text='天体缩放', min=0.1, max=100, step=0.1, default=1)
        self.slider_run_speed_factor = UiSlider(text="运行速度", min=0.01, max=80, default=1)
        self.slider_control_speed_factor = UiSlider(text="控制速度", min=0.01, max=20, default=application.time_scale)
        self.slider_trail_length = UiSlider(text="拖尾长度", min=30, max=500, step=10, default=UrsinaConfig.trail_length)

        self.on_off_switch = SwithButton((self.pause_button_text,
                                          self.start_button_text),
                                         default=self.start_button_text,
                                         tooltips=('暂停(P)', '运行(P)'))
        self.on_off_switch.selected_color = color.red

        self.sec_per_time_switch = SwithButton(("默认", "天", "周", "月", "年", "十年", "百年"),
                                               default="默认",
                                               tooltips=("系统默认", "每秒相当于1天", "每秒相当于1周",
                                                         "每秒相当于1个月",
                                                         "每秒相当于1年", "每秒相当于十年", "每秒相当于1百年"))

        self.on_off_trail = SwithButton((self.no_trail_button_text, self.trail_button_text),
                                        default=self.no_trail_button_text,
                                        tooltips=('天体运行无轨迹', '天体运行有拖尾轨迹'))

        self.point_button = UiButton(text='寻找天体(Y)', on_click=None)
        self.reset_button = UiButton(text='重新开始(O)', on_click=None)

        content = (
            # InputField(name='name_field'),
            # Button(text='Submit', color=color.azure),
            self.point_button,
            self.reset_button,
            # self.buttons,
            self.sec_per_time_switch,
            self.on_off_switch,
            self.on_off_trail,
            self.slider_trail_length,
            self.slider_body_size_factor,
            self.slider_body_spin_factor,
            self.slider_run_speed_factor,
            self.slider_control_speed_factor

        )

        return content

    def after_component_init(self):
        self.sec_per_time_switch.x = -0.4
        self.on_off_switch.x = 0.2
        self.on_off_trail.x = 0.2  # -0.4

    def event_handler_init(self):
        self.slider_body_size_factor.on_value_changed = self.handler.on_slider_body_size_changed
        self.slider_body_spin_factor.on_value_changed = self.handler.on_slider_body_spin_changed
        self.slider_run_speed_factor.on_value_changed = self.handler.on_slider_run_speed_changed
        self.slider_control_speed_factor.on_value_changed = self.handler.on_slider_control_speed_changed
        self.slider_trail_length.on_value_changed = self.handler.on_slider_trail_length_changed
        self.on_off_trail.on_value_changed = self.handler.on_off_trail_changed
        self.on_off_switch.on_value_changed = self.handler.on_off_switch_changed
        self.point_button.on_click = self.handler.on_searching_bodies_click
        self.reset_button.on_click = self.handler.on_reset_button_click
        self.sec_per_time_switch.on_value_changed = self.handler.sec_per_time_switch_changed


if __name__ == '__main__':
    app = Ursina()
    ctl = ControlUI(ControlHandler(), position=(0.6, 0.5), enabled=True)
    app.run()
