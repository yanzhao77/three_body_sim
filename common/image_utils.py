# -*- coding:utf-8 -*-
# title           :图片处理工具类
# description     :图片处理工具类
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
from PIL import Image, ImageColor, ImageEnhance, ImageStat
import math
import os
import numpy as np
import colorsys

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)


def image_file_enhance(imageFilePath, bright, contrast, color, sharpness, saveFolderPath):
    """
    图像增强之亮度、对比度与饱和度调整
    :param imageFilePath: 图像文件路径
    :param bright: 亮度
    :param contrast: 对比度
    :param color: 饱和度
    :param sharpness: 清晰度
    :param saveFolderPath: 结果保存路径
    :return:
    """
    imageFileName = os.path.basename(imageFilePath)
    imageOriginal = Image.open(imageFilePath)
    # 亮度调整
    brightEnhancer = ImageEnhance.Brightness(imageOriginal)
    imageBright = brightEnhancer.enhance(bright)
    imageBrightFileName = "Bright-%0.2f_" % bright + imageFileName
    imageBrightFilePath = os.path.join(saveFolderPath, imageBrightFileName)
    imageBright.save(imageBrightFilePath)
    # 对比度调整
    contrastEnhancer = ImageEnhance.Contrast(imageOriginal)
    imageContrast = contrastEnhancer.enhance(contrast)
    imageContrastFileName = "Contrast-%0.2f_" % contrast + imageFileName
    imageContrastFilePath = os.path.join(saveFolderPath, imageContrastFileName)
    imageContrast.save(imageContrastFilePath)
    # 饱和度调整
    colorEnhancer = ImageEnhance.Color(imageOriginal)
    imageColor = colorEnhancer.enhance(color)
    imageColorFileName = "Color-%0.2f_" % color + imageFileName
    imageColorFilePath = os.path.join(saveFolderPath, imageColorFileName)
    imageColor.save(imageColorFilePath)
    # 清晰度调整
    SharpnessEnhancer = ImageEnhance.Sharpness(imageOriginal)
    imageSharpness = SharpnessEnhancer.enhance(sharpness)
    imageSharpnessFileName = "Sharpness-%0.2f_" % sharpness + imageFileName
    imageSharpnessFilePath = os.path.join(saveFolderPath, imageSharpnessFileName)
    imageSharpness.save(imageSharpnessFilePath)
    return


def image_enhance(imageOriginal, bright=0, contrast=0, color=0, sharpness=0):
    """
    图像增强之亮度、对比度与饱和度调整
    :param imageFilePath: 图像文件路径
    :param bright: 亮度
    :param contrast: 对比度
    :param color: 饱和度
    :param sharpness: 清晰度
    :param saveFolderPath: 结果保存路径
    :return:
    """
    image = imageOriginal
    if bright > 0:
        # 亮度调整
        brightEnhancer = ImageEnhance.Brightness(image)
        image = brightEnhancer.enhance(bright)

    if contrast > 0:
        # 对比度调整
        contrastEnhancer = ImageEnhance.Contrast(image)
        image = contrastEnhancer.enhance(contrast)

    if color > 0:
        # 饱和度调整
        colorEnhancer = ImageEnhance.Color(image)
        image = colorEnhancer.enhance(color)

    if sharpness > 0:
        # 清晰度调整
        SharpnessEnhancer = ImageEnhance.Sharpness(image)
        image = SharpnessEnhancer.enhance(sharpness)

    return image


def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h = hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr


def colorize_color(src_image, color):
    h, s, v = rgb_to_hsv(*color)
    # img_hsv = src_image.convert('HSV')
    return colorize(src_image, h * 255)


def colorize(src_image, hue):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = Image.open(src_image)
    img = img.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue / 360.).astype('uint8'), 'RGBA')

    return new_img


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


def gen_fixed_star_texture(color, save_file, fixed_star_img="fixed_star.png", bright=None, contrast=None):
    bright = 1.1 if bright is None else bright
    contrast = 3.2 if contrast is None else contrast
    fixed_star_img = find_texture(fixed_star_img)
    if fixed_star_img is None:
        err_msg = "未找到纹理图片：" % fixed_star_img
        raise Exception(err_msg)
    trans_img = trans_png(fixed_star_img)
    bg_img = create_image(trans_img.width, trans_img.height, color)
    mixed = mix(bg_img, trans_img)
    mixed = image_enhance(mixed, bright=bright, contrast=contrast)
    mixed.save(save_file, 'PNG')
    return mixed


def gray_to_mono(gray_img, color_val):
    """
    将灰度图片转为单色图片，颜色值为 color_val

    参数：
        gray_img: 灰度图片，PIL Image对象
        color_val: 单色值，RGB颜色值的元组，例如(255, 0, 0)表示红色

    返回值：
        单色图片，PIL Image对象
    """
    # 创建一个白色图片，用于后续的alpha通道处理
    white_img = Image.new('RGB', gray_img.size, (255, 255, 255))

    # 将灰度图片转换为单色图片
    mono_img = gray_img.convert('L').convert('RGBA')

    # 用单色值替换灰色部分
    for y in range(mono_img.height):
        for x in range(mono_img.width):
            r, g, b, a = mono_img.getpixel((x, y))
            if r == g == b:
                # 灰度颜色值范围：0~255
                gray_val = r
                # 将灰度值映射到颜色值范围内
                color_r = int((gray_val / 255) * color_val[0])
                color_g = int((gray_val / 255) * color_val[1])
                color_b = int((gray_val / 255) * color_val[2])
                mono_img.putpixel((x, y), (color_r, color_g, color_b, a))

    # 将白色部分替换回去
    alpha_img = white_img.convert('RGBA')
    alpha_img.paste(mono_img, (0, 0), mono_img)
    return alpha_img


if __name__ == '__main__':
    # gray_img = Image.open("../textures/fixed_star.png")
    # mono = gray_to_mono(gray_img, (0, 0, 255)).show()
    # image_enhance(mono,bright=1,contrast=2).show()

    gen_fixed_star_texture((198, 29, 3), "xxx.png",bright=2.2,contrast=3).show()

    # fixed_star_img = find_texture("sun.png")
    # colorize_color(fixed_star_img,(0,0xff,0xff)).show()

# def brightness(src_img):
#     if isinstance(src_img, str):
#         im = Image.open(src_img)
#     else:
#         im = src_img
#     im = im.convert('L')
#     stat = ImageStat.Stat(im)
#     return stat.mean[0]
#
#
# def brightness(src_img):
#     if isinstance(src_img, str):
#         im = Image.open(src_img)
#     else:
#         im = src_img
#     im = im.convert('L')
#     stat = ImageStat.Stat(im)
#     return stat.rms[0]
#
#
# def brightness(src_img):
#     if isinstance(src_img, str):
#         im = Image.open(src_img)
#     else:
#         im = src_img
#     stat = ImageStat.Stat(im)
#     r, g, b = stat.mean
#     return math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))
#
#
# def brightness(src_img):
#     if isinstance(src_img, str):
#         im = Image.open(src_img)
#     else:
#         im = src_img
#     stat = ImageStat.Stat(im)
#     r, g, b = stat.rms
#     return math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2))


# def brightness(src_img):
#     if isinstance(src_img, str):
#         im = Image.open(src_img)
#     else:
#         im = src_img
#     stat = ImageStat.Stat(im)
#     gs = (math.sqrt(0.241 * (r ** 2) + 0.691 * (g ** 2) + 0.068 * (b ** 2)) for r, g, b in im.getdata())
#     return sum(gs) / stat.count[0]

#
#
# def auto_adjust_contrast_brightness_xxx(src_img):
#     """
#     自适应地调整图片的对比度和亮度。
#
#     :param image_path: 图像路径。
#     :return: 调整后的图像对象。
#     """
#     if isinstance(src_img, str):
#         image = Image.open(src_img)
#     else:
#         image = src_img
#     # 打开图像文件
#     # image = Image.open(image_path)
#
#     # 获取图像直方图
#     histogram = image.histogram()
#
#     # 计算直方图的最小和最大值
#     min_value, max_value = 0, 255
#     for i in range(256):
#         if histogram[i] > 0:
#             min_value = i
#             break
#     for i in range(255, -1, -1):
#         if histogram[i] > 0:
#             max_value = i
#             break
#
#     # 计算调整参数
#     mid_value = 127.5
#     contrast_factor = 127.5 / (max_value - min_value)
#     brightness_factor = mid_value - contrast_factor * (min_value + max_value) / 2
#
#     # 调整对比度和亮度
#     contrast_enhancer = ImageEnhance.Contrast(image)
#     contrast_image = contrast_enhancer.enhance(contrast_factor)
#     brightness_enhancer = ImageEnhance.Brightness(contrast_image)
#     brightness_image = brightness_enhancer.enhance(brightness_factor)
#
#     return brightness_image
#
#
#
# def auto_adjust_contrast_brightness333(src_img):
#     """
#     自适应地调整图片的对比度和亮度。
#
#     :param image_path: 图像路径。
#     :return: 调整后的图像对象。
#     """
#     if isinstance(src_img, str):
#         image = Image.open(src_img)
#     else:
#         image = src_img
#
#     # 计算图像平均亮度
#     brightness = 0
#     pixels = image.load()
#     width, height = image.size
#     for x in range(width):
#         for y in range(height):
#             r, g, b = pixels[x, y]
#             brightness += 0.299 * r + 0.587 * g + 0.114 * b
#     brightness /= width * height
#
#     # 计算调整参数
#     mid_value = 127.5
#     contrast_factor = mid_value / brightness
#     brightness_factor = mid_value - brightness * contrast_factor
#
#     # 调整对比度和亮度
#     contrast_enhancer = ImageEnhance.Contrast(image)
#     contrast_image = contrast_enhancer.enhance(contrast_factor)
#     brightness_enhancer = ImageEnhance.Brightness(contrast_image)
#     brightness_image = brightness_enhancer.enhance(brightness_factor)
#
#     return brightness_image
#
#
# def auto_adjust_contrast_brightness(src_img):
#     """
#     自适应地调整图片的对比度和亮度。
#
#     :param image_path: 图像路径。
#     :return: 调整后的图像对象。
#     """
#     if isinstance(src_img, str):
#         image = Image.open(src_img)
#     else:
#         image = src_img
#
#     # 获取图像直方图
#     histogram = image.histogram()
#
#     # 计算直方图的最小和最大值
#     min_value, max_value = 0, 255
#     for i in range(256):
#         if histogram[i] > 0:
#             min_value = i
#             break
#     for i in range(255, -1, -1):
#         if histogram[i] > 0:
#             max_value = i
#             break
#
#     # 计算调整参数
#     mid_value = 127.5
#     contrast_factor = mid_value / (max_value - min_value)
#     brightness_factor = mid_value - contrast_factor * (min_value + max_value) / 2
#
#     # 调整对比度和亮度
#     contrast_enhancer = ImageEnhance.Contrast(image)
#     contrast_image = contrast_enhancer.enhance(contrast_factor)
#     brightness_enhancer = ImageEnhance.Brightness(contrast_image)
#     brightness_image = brightness_enhancer.enhance(brightness_factor)
#
#     return brightness_image
