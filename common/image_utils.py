# -*- coding:utf-8 -*-
# title           :图片处理工具类
# description     :图片处理工具类
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from PIL import Image, ImageColor
import os


# 图片背景透明化
def trans_png(src_image, alpha=100):
    img = Image.open(src_image)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = list()

    for item in datas:
        r = item[0] if item[0] < 255 else 255
        b = item[1] if item[1] < 255 else 255
        g = item[2] if item[2] < 255 else 255

        newData.append((r, b, g, alpha))
    img.putdata(newData)
    return img


# 图片融合
def mix(img1, img2, coordinator=(0, 0)):
    im = img1
    mark = img2
    layer = Image.new('RGBA', im.size, (0, 0, 0, 0))
    layer.paste(mark, coordinator)
    out = Image.composite(layer, im, layer)
    return out


# verse = transPNG("")
#
# mix("file", verse).save('xxx.png', 'PNG')
#
#
# from PIL import Image

def create_image(width, height, color):
    """
    创建指定大小和背景颜色的图片对象

    参数：
    width: 图片宽度
    height: 图片高度
    color: 背景颜色，可以是RGB元组或颜色名称字符串

    返回：
    Image对象
    """
    # 创建图片对象
    image = Image.new('RGB', (width, height), color)
    return image


def rgb_to_hex(rgb):
    r, g, b = rgb
    hex_color = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_color


def find_texture_root_path():
    paths = [os.path.join('.', 'textures'), os.path.join('..', 'textures'), os.path.join('..', '..', 'textures')]
    for path in paths:
        if os.path.exists(path):
            return path
    return None


def find_texture(texture):
    """
    尝试在多个路径下寻找纹理图片
    :param texture: 纹理图片
    :return: 纹理图片的路径
    """
    if os.path.exists(texture):
        return texture
    paths = [os.path.join('.', 'textures'), os.path.join('..', 'textures'), os.path.join('..', '..', 'textures')]
    for path in paths:
        p = os.path.join(path, texture)
        if os.path.exists(p):
            return p

    return ""


def gen_fixed_star_texture(color, save_file, fixed_star_img="fixed_star.png"):
    fixed_star_img = find_texture(fixed_star_img)
    if fixed_star_img is None:
        err_msg = "未找到纹理图片：" % fixed_star_img
        raise Exception(err_msg)
    trans_img = trans_png(fixed_star_img)
    bg_img = create_image(trans_img.width, trans_img.height, color)
    mix(bg_img, trans_img).save(save_file, 'PNG')


if __name__ == '__main__':
    gen_fixed_star_texture((100, 100, 255), "xxx.png")
