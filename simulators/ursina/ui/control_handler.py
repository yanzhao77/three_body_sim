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
from simulators.ursina.ui.ui_panel import UiPanel
from simulators.ursina.ui_component import UiSlider, SwithButton, UiButton, Buttons
from simulators.ursina.ursina_config import UrsinaConfig
from simulators.ursina.ursina_event import UrsinaEvent
from ursina import WindowPanel, InputField, Button, Slider, ButtonGroup, Panel, invoke
from simulators.ursina.ui.event_handler import EventHandler


class ControlHandler(EventHandler):

    def handler_input_init(self):
        self.settings_handler = Entity(ignore_paused=True)
        self.settings_handler.input = self.settings_handler_input
        key_info_str = "方位控制[键盘QWEASD]+[鼠标右键]，按[空格]更多控制"
        key_info = Text(text=key_info_str, font=UrsinaConfig.CN_FONT, position=(-1, 0.5), origin=(-1, 1),
                        background=True)

    def sec_per_time_switch_changed(self):
        # ("默认", "天", "周", "月", "年", "十年", "百年")
        if self.ui.sec_per_time_switch.value == "天":
            UrsinaConfig.seconds_per = SECONDS_PER_DAY
        elif self.ui.sec_per_time_switch.value == "周":
            UrsinaConfig.seconds_per = SECONDS_PER_WEEK
        elif self.ui.sec_per_time_switch.value == "月":
            UrsinaConfig.seconds_per = SECONDS_PER_MONTH
        elif self.ui.sec_per_time_switch.value == "年":
            UrsinaConfig.seconds_per = SECONDS_PER_YEAR
        elif self.ui.sec_per_time_switch.value == "十年":
            UrsinaConfig.seconds_per = SECONDS_PER_YEAR * 10
        elif self.ui.sec_per_time_switch.value == "百年":
            UrsinaConfig.seconds_per = SECONDS_PER_YEAR * 100
        else:
            UrsinaConfig.seconds_per = 0

    def on_off_trail_changed(self):
        if self.ui.on_off_trail.value == self.ui.trail_button_text:
            UrsinaConfig.show_trail = True
        else:
            UrsinaConfig.show_trail = False

    def move_camera_to_entity(self, camera_pos: Vec3, entity_pos: Vec3, _distance: float) -> Vec3:
        # 计算摄像机到实体的向量
        direction = entity_pos - camera_pos
        # 计算当前距离
        current_distance = direction.length()
        # 如果当前距离已经小于等于要求的距离，则直接返回实体坐标
        if current_distance <= _distance:
            return camera_pos
        # 计算需要移动的距离
        _distance = current_distance - _distance
        # 根据需要移动的距离计算移动向量
        move_vector = direction.normalized() * _distance
        # 返回摄像机移动后的坐标
        return camera_pos + move_vector

    def move_camera_to_entity(self, entity, d):
        camera.position = entity.position  # - Vec3(0, 0, d)  # 设置摄像机位置
        camera.world_position = entity.position

    def bodies_button_list_click(self, item):
        if item is not None:
            # TODO: 先找到位置，确定摄像机的位置
            try:
                d = item.planet.scale_x * 20
                self.move_camera_to_entity(item.planet, d)
            except Exception as e:
                self.ui.show_message(f"{item}飞不见了")

        self.bodies_button_list_close()

    def bodies_button_list_close(self):
        if hasattr(self, "bodies_button_list"):
            self.bodies_button_list.enabled = False
            destroy(self.bodies_button_list)

    def on_searching_bodies_click(self):
        results = UrsinaEvent.on_searching_bodies()
        if len(results) > 0:
            sub_name, bodies = results[0]
            if len(bodies) == 0:
                self.show_message("天体都飞不见了，请重新运行。")
                # button_dict = {"天体都飞不见了，请重新运行。": lambda: self.bodies_button_list_click(None)}
                return
            # print(results[0])
            button_dict = {"[关闭]        == 寻找天体 ==": lambda: self.bodies_button_list_click(None)}
            camera = scene.camera
            for body in bodies:
                def callback_action(b=body):
                    self.bodies_button_list_click(b)

                if body.appeared:
                    distance_to_entity = distance(body.planet, camera)
                    d = distance_to_entity / UrsinaConfig.SCALE_FACTOR / AU
                    name = f"{body.name}\t距离：{d:.4f}天文单位"
                    button_dict[name] = callback_action
                else:
                    if hasattr(self, "bodies_button_list"):
                        self.bodies_button_list_close()
                    name = f"{body.name}\t距离太远，找不到了"
                    button_dict[name] = lambda: self.bodies_button_list_click(None)

            if hasattr(self, "bodies_button_list"):
                self.bodies_button_list_close()

            self.bodies_button_list = ButtonList(button_dict, font=UrsinaConfig.CN_FONT, button_height=1.5)

    def on_reset_button_click(self):
        UrsinaEvent.on_reset()

    def on_buttons_changed(self):
        if self.ui.buttons.value == "寻找":
            self.on_searching_bodies_click()
        elif self.ui.buttons.value == "重启":
            self.on_reset_button_click()

    def on_off_switch_changed(self):
        if self.ui.on_off_switch.value == self.ui.pause_button_text:
            self.ui.on_off_switch.selected_color = color.green
            application.paused = True
            for c in self.ui.children:
                if not c.ignore_paused:
                    # c.enabled = True
                    c.disabled = False
        else:
            self.ui.on_off_switch.selected_color = color.red
            application.paused = False
            for c in self.ui.children:
                if not c.ignore_paused:
                    # c.enabled = True
                    c.disabled = False

    def on_slider_trail_length_changed(self):
        UrsinaConfig.trail_length = int(self.ui.slider_trail_length.value)

    def on_slider_control_speed_changed(self):
        application.time_scale = self.ui.slider_control_speed_factor.value

    def on_slider_body_spin_changed(self):
        UrsinaConfig.body_spin_factor = self.ui.slider_body_spin_factor.value

    def on_slider_body_size_changed(self):
        UrsinaConfig.body_size_factor = self.ui.slider_body_size_factor.value

    def on_slider_run_speed_changed(self):
        UrsinaConfig.run_speed_factor = self.ui.slider_run_speed_factor.value

    def settings_handler_input(self, key):
        import sys
        if key == "escape":
            sys.exit()
        # print(key)
        elif key == 'space':
            self.ui.enabled = not self.ui.enabled
        elif key == 'left mouse down':
            print(key)
        elif key == 'y':  # 寻找天体
            if hasattr(self, "bodies_button_list"):
                if self.ui.bodies_button_list.enabled:
                    self.bodies_button_list_close()
                    return
            self.on_searching_bodies_click()
        elif key == 'o':  # 重新开始
            paused = application.paused
            if paused:  # 如果是暂停状态，先不暂停，等重新开始后再暂停
                application.paused = False
            self.on_reset_button_click()
            if paused:
                def application_paused():
                    application.paused = True
                UrsinaEvent.on_application_run_callback_subscription(application_paused)

        elif key == 'i':  # 拖尾开关
            if self.ui.on_off_trail.value == self.ui.trail_button_text:
                self.ui.on_off_trail.value = self.ui.no_trail_button_text
            else:
                self.ui.on_off_trail.value = self.ui.trail_button_text
            self.on_off_trail_changed()
        elif key == 'p':  # 开始、暂停
            if self.ui.on_off_switch.value == self.ui.pause_button_text:
                self.ui.on_off_switch.value = self.ui.start_button_text
            else:
                self.ui.on_off_switch.value = self.ui.pause_button_text
            self.on_off_switch_changed()
        elif key == '+' or key == "= up":
            run_speed_factor = self.ui.slider_run_speed_factor.value + self.ui.slider_run_speed_factor.step * 50
            if run_speed_factor > self.ui.slider_run_speed_factor.max:
                run_speed_factor = self.ui.slider_run_speed_factor.max
            self.ui.slider_run_speed_factor.value = run_speed_factor
            self.ui.slider_run_speed_factor.knob.drop()
        elif key == '-' or key == "- up":
            run_speed_factor = self.ui.slider_run_speed_factor.value - self.ui.slider_run_speed_factor.step * 50
            if run_speed_factor < self.ui.slider_run_speed_factor.min:
                run_speed_factor = self.ui.slider_run_speed_factor.min
            self.ui.slider_run_speed_factor.value = run_speed_factor
            self.ui.slider_run_speed_factor.knob.drop()
