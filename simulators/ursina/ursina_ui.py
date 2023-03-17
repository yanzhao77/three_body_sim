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

from common.consts import AU
from simulators.ursina.ui_component import UiSlider, SwithButton, UiButton
from simulators.ursina.ursina_config import UrsinaConfig
from simulators.ursina.ursina_event import UrsinaEvent
from ursina import WindowPanel, InputField, Button, Slider, ButtonGroup, Panel, invoke


class UrsinaUI:

    def ui_component_init(self):

        self.start_button_text = "●"  # 》●▲○◎
        self.pause_button_text = "〓"  # 〓 || ‖
        self.no_trail_button_text = "○ "
        self.trail_button_text = "○--"

        application.time_scale = 0.5
        self.slider_body_spin_factor = UiSlider(text='自转速度', min=0.01, max=30, default=1)
        self.slider_body_size_factor = UiSlider(text='天体缩放', min=0.01, max=10, default=1)
        self.slider_run_speed_factor = UiSlider(text="运行速度", min=0.01, max=800, default=1)
        self.slider_control_speed_factor = UiSlider(text="控制速度", min=0.01, max=30, default=application.time_scale)
        self.slider_trail_length = UiSlider(text="拖尾长度", min=30, max=500, default=UrsinaConfig.trail_length)

        self.slider_body_size_factor.on_value_changed = self.on_slider_body_size_changed
        self.slider_body_spin_factor.on_value_changed = self.on_slider_body_spin_changed
        self.slider_run_speed_factor.on_value_changed = self.on_slider_run_speed_changed
        self.slider_control_speed_factor.on_value_changed = self.on_slider_control_speed_changed
        self.slider_trail_length.on_value_changed = self.on_slider_trail_length_changed

        self.on_off_switch = SwithButton((self.pause_button_text,
                                          self.start_button_text),
                                         default=self.start_button_text,
                                         tooltips=('暂停', '运行'))
        self.on_off_switch.selected_color = color.red

        self.sec_per_time_switch = SwithButton(("默认", "天", "周", "月", "年", "十年", "百年"),
                                               default="默认",
                                               tooltips=("系统默认", "每秒相当于1天", "每秒相当于1周",
                                                         "每秒相当于1个月",
                                                         "每秒相当于1年", "每秒相当于十年", "每秒相当于1百年"))

        self.on_off_trail = SwithButton((self.no_trail_button_text, self.trail_button_text),
                                        default=self.no_trail_button_text,
                                        tooltips=('天体运行无轨迹', '天体运行有拖尾轨迹'))
        self.on_off_trail.on_value_changed = self.on_off_trail_changed

        self.point_button = UiButton(text='寻找', on_click=self.on_searching_bodies_click)
        self.reset_button = UiButton(text='重置', on_click=self.on_reset_button_click)

        # button1 = Button(text='Button 1', scale=(0.1, 0.1), position=(-0.1, 0))
        # button2 = Button(text='Button 2', scale=(0.1, 0.1), position=(0.1, 0))

        # btn_settings = UiButton(text='操作设置', on_click=self.on_point_button_click)
        # btn_settings.position = window.top_left
        # btn_settings.y = 0.5
        # # btn_settings.scale = (0.1,0.1)
        # # btn_settings.y = 0
        # btn_settings.scale = (.25, .025),
        # btn_settings.origin = (-.5, .5),
        # btn_settings.pressed_scale = 1,
        # if btn_settings.text_entity:
        #     btn_settings.text_entity.x = .05
        #     btn_settings.text_entity.origin = (-.5, 0)
        #     btn_settings.text_entity.scale *= .8

        self.on_off_switch.on_value_changed = self.on_off_switch_changed
        wp = WindowPanel(
            title='',
            content=(
                Text('方位控制: Q W E A S D + 鼠标右键', font='msyhl.ttc'),
                # InputField(name='name_field'),
                # Button(text='Submit', color=color.azure),
                self.point_button,
                self.reset_button,
                self.sec_per_time_switch,
                self.on_off_switch,
                self.on_off_trail,
                self.slider_trail_length,
                self.slider_body_size_factor,
                self.slider_body_spin_factor,
                self.slider_run_speed_factor,
                self.slider_control_speed_factor

            ), ignore_paused=True, color=color.rgba(0.0, 0.0, 0.0, 0.5)  # , popup=True
        )
        self.sec_per_time_switch.x = -0.5
        self.on_off_switch.x = -0.2
        self.on_off_trail.x = -0.2
        wp.y = 0.5  # wp.panel.scale_y / 2 * wp.scale_y  # center the window panel
        wp.x = 0.6  # wp.scale_x + 0.1
        # wp.x = 0#wp.panel.scale_x / 2 * wp.scale_x
        self.wp = wp
        self.wp.enabled = False

    def __init__(self):
        self.ui_component_init()

        self.settings_handler = Entity(ignore_paused=True)
        # 加载中文字体文件

        # text_time_scale = "1"
        # self.text_time_scale_info = None
        self.settings_handler.input = self.settings_handler_input
        # self.show_text_time_scale_info()
        key_info_str = "按[空格]设置"
        key_info = Text(text=key_info_str, font=UrsinaConfig.CN_FONT, position=(-0.5, 0.5), origin=(-1, 1),
                        background=True)
        # # self.show_button()
        # slider_text = Text(text='自转速度', scale=1, position=(-0.6, 0.3))
        # slider = Slider(scale=0.5, position=(-0.6, 0), min=0, max=10, step=1, text=slider_text)

    def show_message(self, message, close_time=3):
        """
        创建消息框
        :param message: 消息内容
        :param close_time: 定义关闭时间
        :return:
        """
        # 创建消息框
        message_box = Text(text=message, font=UrsinaConfig.CN_FONT, background=True, origin=(0, 0), y=.25)

        # 定义关闭函数
        def close_message():
            destroy(message_box)

        s = Sequence(
            Wait(3),
            Func(close_message)
        )
        s.start()
        # # 使用 time 模块来实现定时关闭
        # invoke(close_message, delay=close_time)

    def on_off_trail_changed(self):
        if self.on_off_trail.value == self.trail_button_text:
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

    def move_camera_to_entity(self,entity,d):
        import math
        # print("before",camera.position, entity.position)
        camera.position = entity.position #- Vec3(0, 0, d)  # 设置摄像机位置
        camera.world_position = entity.position
        # camera.rotation = (0, 0, 0)  # 重置摄像机旋转角度

        # print("after",camera.position,entity.position)

        # # 获取相机和实体之间的向量
        # target_vector = entity.position - camera.position
        # target_vector.y = 0  # 假设实体在 x-z 平面上，将 y 坐标设为 0
        #
        # # 计算旋转角度
        # angle = math.degrees(math.atan2(target_vector.z, target_vector.x))
        # camera.rotation_y = angle  # 旋转相机

        # camera.look_at(entity.position)  # 对准指定实体

    def bodies_button_list_click(self, item):
        if item is not None:
            # TODO: 先找到位置，确定摄像机的位置
            # print("select->", item)
            # UrsinaConfig.SCALE_FACTOR
            # import copy
            # camera_rotation = copy.deepcopy(camera.rotation)
            d = item.planet.scale_x * 20
            self.move_camera_to_entity(item.planet, d)
            # d = distance(camera.position, item.planet.position)
            # camera.look_at(item.planet)
            # if d > 1.5 * x:
            #     move_to = self.move_camera_to_entity(camera.position, item.planet.position, x)
            #     camera.position = move_to

            # camera_rotation = copy.deepcopy(camera.rotation)
            # camera.rotation = (camera_rotation[0], camera_rotation[1], 0)
            # camera.forward = (1, 0, 0)  # 设置相机的方向向量为x轴方向

        destroy(self.bodies_button_list)

    # my_entity = Entity(model='cube', color=color.red, position=(0, 1, 5))
    #
    # # 获取当前摄像机
    # camera = scene.camera
    #
    # # 计算 Entity 和摄像机之间的距离
    # distance_to_entity = distance(my_entity, camera)
    #
    # print('距离:', distance_to_entity)

    def on_searching_bodies_click(self):
        results = UrsinaEvent.on_searching_bodies()
        if len(results) > 0:
            sub_name, bodies = results[0]
            if len(bodies) == 0:
                self.show_message("天体都飞不见了，请重新运行。")
                # button_dict = {"天体都飞不见了，请重新运行。": lambda: self.bodies_button_list_click(None)}
                return
            # print(results[0])
            button_dict = {"[关闭]": lambda: self.bodies_button_list_click(None)}
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
                        destroy(self.bodies_button_list)
                    name = f"{body.name}\t距离太远，找不到了"
                    button_dict[name] = lambda: self.bodies_button_list_click(None)

            if hasattr(self, "bodies_button_list"):
                destroy(self.bodies_button_list)

            self.bodies_button_list = ButtonList(button_dict, font=UrsinaConfig.CN_FONT, button_height=1.5)
            # self.bodies_button_list.input = self.bodies_button_list_input

    def on_reset_button_click(self):
        UrsinaEvent.on_reset()

    def on_off_switch_changed(self):
        if self.on_off_switch.value == self.pause_button_text:
            self.on_off_switch.selected_color = color.green
            application.paused = True
            for c in self.wp.children:
                if not c.ignore_paused:
                    # c.enabled = True
                    c.disabled = False
        else:
            self.on_off_switch.selected_color = color.red
            application.paused = False
            for c in self.wp.children:
                if not c.ignore_paused:
                    # c.enabled = True
                    c.disabled = False

    def on_slider_trail_length_changed(self):
        UrsinaConfig.trail_length = int(self.slider_trail_length.value)

    def on_slider_control_speed_changed(self):
        application.time_scale = self.slider_control_speed_factor.value

    def on_slider_body_spin_changed(self):
        UrsinaConfig.body_spin_factor = self.slider_body_spin_factor.value

    def on_slider_body_size_changed(self):
        UrsinaConfig.body_size_factor = self.slider_body_size_factor.value

    def on_slider_run_speed_changed(self):
        UrsinaConfig.run_speed_factor = self.slider_run_speed_factor.value

    # def show_text_time_scale_info(self):
    #     if self.text_time_scale_info is not None:
    #         self.text_time_scale_info.disable()
    #     text_time_scale = "控制倍率:" + str(application.time_scale).ljust(4, " ")
    #     text_time_scale_info = Text(text=text_time_scale, position=(-0.8, 0.5), origin=(-1, 1), background=True)

    # def show_button(self):
    #     b = Button(scale=(0, .25), text='zzz')

    #  if key == "escape":
    #             if mouse.locked:
    #                 self.on_disable()
    #             else:
    #                 sys.exit()

    # 按空格键则暂停
    def settings_handler_input(self, key):
        import sys
        if key == "escape":
            sys.exit()
        # print(key)
        elif key == 'space':
            self.wp.enabled = not self.wp.enabled
        elif key == 'left mouse down':
            print(key)
        #     application.paused = not application.paused  # Pause/unpause the game.
        # elif key == 'tab':
        #     # application.time_scale 属性控制游戏时间流逝的速度。
        #     # 具体来说，它是一个浮点数，用于调整游戏时间流逝速度的比例，其默认值为 1.0，表示正常速度。
        #     # 当你将它设置为小于 1.0 的值时，游戏时间会变慢，而设置为大于 1.0 的值时，游戏时间则会变快。
        #     for idx, time_scale in enumerate(time_scales):
        #         if float(application.time_scale) == time_scale:
        #             if idx < len(time_scales) - 1:
        #                 application.time_scale = time_scales[idx + 1]
        #                 break
        #             else:
        #                 application.time_scale = time_scales[0]
        # elif key == '+':
        #     UrsinaConfig.run_speed_factor *= 2
        # elif key == "= up":
        #     UrsinaConfig.body_spin_factor *= 2
        #     # if application.time_scale in time_scales:
        #     #     idx = time_scales.index(application.time_scale)
        #     #     if idx < len(time_scales) - 1:
        #     #         application.time_scale = time_scales[idx + 1]
        # elif key == '-':
        #     UrsinaConfig.run_speed_factor *= 0.5
        # elif key == "- up":
        #     UrsinaConfig.body_spin_factor *= 0.5
        #     # if application.time_scale in time_scales:
        #     #     idx = time_scales.index(application.time_scale)
        #     #     if idx > 0:
        #     #         application.time_scale = time_scales[idx - 1]
        #
        # self.show_text_time_scale_info()
