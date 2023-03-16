# -*- coding:utf-8 -*-
# title           :matplotlib天体视图
# description     :matplotlib天体视图（天体效果展示用）
# author          :Python超人
# date            :2023-02-11
# link            :https://gitcode.net/pythoncr/
# python_version  :3.8
# ==============================================================================
import os
import matplotlib.pyplot as plt
from common.func import get_dominant_colors

from simulators.views.body_view import BodyView
import numpy as np


class MplView(BodyView):
    """
    matplotlib天体视图（天体效果展示用）
    """

    def update(self):
        pass

    def appear(self):
        if hasattr(self.body, "torus_stars"):
            # 暂不支持环状小行星群
            return

    def disappear(self):
        pass
