# -*- coding:utf-8 -*-
# title           :模拟器用功能库
# description     :模拟器用功能库
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import ticker

from common.consts import SECONDS_PER_WEEK
from common.system import System

COSMIC_BG_COLOR = "#002563"
COSMIC_FORE_COLOR = "white"


def get_default_colors(styles={}):
    """

    :param styles:
    :return:
    """
    bg_color = styles["bg_color"] if "bg_color" in styles else "white"  # COSMIC_BG_COLOR
    fore_color = styles["fore_color"] if "fore_color" in styles else "black"  # COSMIC_FORE_COLOR
    # bg_color = styles["bg_color"] if "bg_color" in styles else COSMIC_BG_COLOR
    # fore_color = styles["fore_color"] if "fore_color" in styles else COSMIC_FORE_COLOR
    styles["bg_color"] = bg_color
    styles["fore_color"] = fore_color
    return bg_color, fore_color


def create_fig_ax(styles={}):
    """

    :param styles:
    :return:
    """
    bg_color, fore_color = get_default_colors(styles)

    plt.rcParams['patch.facecolor'] = bg_color
    plt.rcParams['xtick.color'] = fore_color
    plt.rcParams['ytick.color'] = fore_color

    plt.rcParams['axes.labelcolor'] = fore_color
    plt.rcParams['axes.edgecolor'] = fore_color

    plt.rcParams['axes.facecolor'] = fore_color
    plt.rcParams['figure.facecolor'] = fore_color

    if bg_color is None:
        fig = plt.figure('天体模拟运行效果', figsize=(20, 12))
    else:
        fig = plt.figure('天体模拟运行效果', figsize=(20, 12), facecolor=bg_color)
    ax = fig.gca(projection="3d")

    # 调整子图区域
    plt.subplots_adjust(left=-0.8, right=1.8, bottom=0.0, top=0.95)

    # # 设置窗口大小
    # fig.set_size_inches(20, 12)
    # ax.set_box_aspect([2, 1, 1])  # 将三个轴设置为等比例缩放

    return fig, ax


def update_ax_styles(ax, styles={}):
    """

    :param ax:
    :param styles:
    :return:
    """
    plt.cla()
    bg_color, fore_color = get_default_colors(styles)

    # # 设置 x 轴刻度
    # ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5))
    # ax.xaxis.set_minor_locator(ticker.MultipleLocator(base=0.01))
    #
    # # 设置 y 轴刻度
    # ax.yaxis.set_major_locator(ticker.MultipleLocator(base=5))
    # ax.yaxis.set_minor_locator(ticker.MultipleLocator(base=0.01))
    #
    # # 设置 z 轴刻度
    # ax.zaxis.set_major_locator(ticker.MultipleLocator(base=5))
    # ax.zaxis.set_minor_locator(ticker.MultipleLocator(base=0.01))

    # ax.w_xaxis.line.set_color(fore_color)
    # ax.w_yaxis.line.set_color(fore_color)
    # ax.w_zaxis.line.set_color(fore_color)
    # ax.xaxis.label.set_color(fore_color)
    # ax.yaxis.label.set_color(fore_color)
    # ax.zaxis.label.set_color(fore_color)

    # ax.tick_params(axis='both', colors=fore_color)
    # ax.tick_params(axis='x', colors=fore_color)  # only affects
    # ax.tick_params(axis='y', colors=fore_color)  # tick labels
    # ax.tick_params(axis='z', colors=fore_color)  # not tick marks
    # ax.margins(x=1e20, y=None, z=None, tight=False)
    ax.patch.set_color(bg_color)  # 设置 ax 区域背景颜色
    bg_color = mcolors.to_rgba(bg_color)
    fore_color_alpha = mcolors.to_rgba(fore_color, alpha=0.3)
    # bg_color = (0.2, 0.2, 1.0, 1.0)
    # 设置网格背景颜色
    # ax.grid(color=fore_color)
    # ax.grid(color=fore_color, linestyle='dashed', linewidth=1, alpha=0.1)
    ax.xaxis._axinfo["grid"]['color'] = fore_color_alpha
    ax.yaxis._axinfo["grid"]['color'] = fore_color_alpha
    ax.zaxis._axinfo["grid"]['color'] = fore_color_alpha
    ax.xaxis._axinfo["grid"]['linestyle'] = 'dashed'
    ax.yaxis._axinfo["grid"]['linestyle'] = 'dashed'
    ax.zaxis._axinfo["grid"]['linestyle'] = 'dashed'
    ax.xaxis._axinfo["grid"]['linewidth'] = 0.5
    ax.yaxis._axinfo["grid"]['linewidth'] = 0.5
    ax.zaxis._axinfo["grid"]['linewidth'] = 0.5
    # ax.xaxis._axinfo["grid"]['alpha'] = 0.1
    # ax.yaxis._axinfo["grid"]['alpha'] = 0.1
    # ax.zaxis._axinfo["grid"]['alpha'] = 0.1

    ax.w_xaxis.set_pane_color(bg_color)
    ax.w_yaxis.set_pane_color(bg_color)
    ax.w_zaxis.set_pane_color(bg_color)
    # ax.axes.yaxis.grid(color='red', linestyle='--', linewidth=1, alpha=1)
    # ax.axes.yaxis.gridlines
    # ax.set_bgcolor('red')
    # ax.xaxis.grid(color='r', linestyle='--', linewidth=1, alpha=1)
    # ax.axes.yaxis.grid(color='r', linestyle='--', linewidth=1, alpha=1)
    # ax.spines['right'].set_color('blue')
    # ax.spines['top'].set_color('none')
    # axs0=plt.subplot(221,axisbg='#FFDAB9')

    ax.set_title('天体模拟运行效果', loc='center', pad=0, fontsize="24", color=fore_color)
    # ax.set_title('Title', )

    ax.set_xlabel('X(天文单位:AU)', fontsize="18", color=fore_color)
    ax.set_ylabel('Y(天文单位:AU)', fontsize="18", color=fore_color)
    ax.set_zlabel('Z(天文单位:AU)', fontsize="18", color=fore_color)
