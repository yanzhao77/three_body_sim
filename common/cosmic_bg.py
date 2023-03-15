# -*- coding:utf-8 -*-
# title           :宇宙背景星空图片生成
# description     :宇宙背景星空图片生成
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================

from PIL import Image
from random import randint
import time

# xSize = 2048
# ySize = 1024

xSize = 800
ySize = 60

# x = int(xSize / 2)
# y = int(ySize / 2)
# im = Image.new('RGBA', (xSize, ySize), (0, 0, 0, 0))
# im.getpixel((x, y))
# step = 2000
#
#
# def move():
#     """随机生成并返回12345678个数字，分别代表 上右下左 右上 右下 左下 左上"""
#     return randint(0, xSize - 1), randint(0, ySize - 1)
#
#
# def color():
#     """在所在像素下点涂颜色"""
#     global im, x, y
#     add_color = 255
#     src_str_list = im.load()
#     data = src_str_list[x, y]
#     data_list = list(data)
#     # print(data)
#     if data_list[0] < 255:
#         data_list[0] += add_color
#         data_list[1] += add_color
#         data_list[2] += add_color
#     # data = tuple(data_list)
#     data = (255, 255, 255, 0)
#     im.putpixel((x, y), data)
#
#
# def judge():
#     """判断是否已经走到边界上"""
#     global x, y, xSize, ySize
#     b = int(xSize / 2)
#     if x >= xSize - 1:
#         x -= b
#     if y >= ySize - 1:
#         y -= b
#     if x <= 1:
#         x += b
#     if y <= 0:
#         y += b
#
#
# def draw():
#     """根据move返回值来移动图片上的像素点"""
#     global x, y, im
#     x, y = move()
#     color()
#
#
# for i in range(step):
#     move()
#     draw()
#     judge()

# im.save(f'asteroids.png')

from PIL import Image, ImageDraw, ImageFont

image = Image.new(mode='RGBA', size=(xSize, ySize))

draw_table = ImageDraw.Draw(im=image)

for i in range(500):
    x,y = randint(0, xSize - 1), randint(0, ySize - 1)
    draw_table.point(xy=(x, y), fill='#FFFFFF')

image.show() # 直接显示图片

image.save('asteroids.png', 'PNG') # 保存在当前路径下，格式为PNG

image.close()