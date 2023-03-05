# -*- coding:utf-8 -*-
# title           :太阳、地球模拟运行
# description     :太阳、地球模拟运行（演示案例）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
# from bodies import Sun, Earth
# from common.consts import SECONDS_PER_WEEK, SECONDS_PER_DAY
# from scenes.func import mayavi_run, mpl_run
# from bodies.body import Body, AU
# """
# 代码用途：模拟3D星空
# 作者：阿黎逸阳
# ​
# """
# from turtle import *
# from random import random,randint
#
# s = Screen()
# width, height = 800, 600
# s.setup(width, height)  # 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例
# s.title("模拟3D星空-阿黎逸阳")  # 设置标题
# s.bgcolor("black")  # 设置背景颜色为黑色
# s.mode("logo")  # 设置乌龟模式（“standard”，“logo”或“world”）并执行重置，logo表示向上
# s.delay(0)  # 设置或返回以毫秒为单位的绘图延迟，这里要设为0，否则很卡
#
# printer = Turtle()
# printer.hideturtle()
# printer.penup()
# printer.color('white')
# printer.goto(-100, -150)
# printer.write("In the whole universe\n\n", move=True, align="left", font=("Italic", 30, "bold"))
# printer.goto(-300, -200)
# printer.write("you're the only star belongs me!\n\n", move=True, align="left", font=("Italic", 30, "bold"))
#
# t = Turtle(visible=False, shape='circle')
# t.pencolor("white")  # 设置画笔的颜色
# t.fillcolor("white")  # 设置图形填充颜色
# t.penup()  # 抬起画笔
# t.setheading(-90)  # 设置当前朝向角度
# t.goto(width / 2, randint(-height / 2, height / 2))  # 把画笔移动到定点
#
#
#
# def bgpic(self, picname=None):
#     if picname is None:
#         return self._bgpicname
#     if picname not in self._bgpics:
#         self._bgpics[picname] = self._image(picname)
#     self._setbgpic(self._bgpic, self._bgpics[picname])
#     self._bgpicname = picname
#
#
#
# from turtle import *
# from random import random, randint
# import os  # 导入设置路径的库
# import sys
# # from pygame.locals import *
#
# # os.chdir('F:/微信公众号/Python/0.已发表/23.绘制星空图/星空图v2')  # 把路径改为数据存放的路径
# screen = Screen()
# width, height = 800, 600
# screen.setup(width, height)  # 输入宽和高为整数时, 表示像素; 为小数时, 表示占据电脑屏幕的比例
# screen.title("模拟3D星空-阿黎逸阳")  # 设置标题
# screen.bgcolor("black")  # 设置背景颜色 darkblue
# # screen.bgpic(r'./aa.gif')
# screen.mode("logo")  # 设置乌龟模式（“standard”，“logo”或“world”）并执行重置，logo表示向上
# screen.delay(0)  # 设置或返回以毫秒为单位的绘图延迟，这里要设为0，否则很卡
#
# printer = Turtle()


# printer.hideturtle()
from PIL import Image
from random import randint
import time
xSize = 2048
ySize = 1024
x = int(xSize/2)
y = int(ySize/2)
im = Image.new('RGBA', (xSize, ySize), 'black')
im.getpixel((x, y))
step = 2000


def move():
    """随机生成并返回12345678个数字，分别代表 上右下左 右上 右下 左下 左上"""
    return randint(0, xSize-1), randint(0,ySize-1)


def color():
    """在所在像素下点涂颜色"""
    global im, x, y
    add_color = 255
    src_str_list = im.load()
    data = src_str_list[x, y]
    data_list = list(data)
    print(data)
    if data_list[0] < 255:
        data_list[0] += add_color
        data_list[1] += add_color
        data_list[2] += add_color
    data = tuple(data_list)
    im.putpixel((x, y), data)


def judge():
    """判断是否已经走到边界上"""
    global x, y, xSize, ySize
    b = int(xSize/2)
    if x >= xSize-1:
        x -= b
    if y >= ySize-1:
        y -= b
    if x <= 1:
        x += b
    if y <= 0:
        y += b

def draw():
    """根据move返回值来移动图片上的像素点"""
    global x, y, im
    x,y = move()
    color()

for i in range(step):
    move()
    draw()
    judge()
im.save(f'RandomMove2D.png')
exit()
