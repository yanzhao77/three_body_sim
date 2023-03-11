<p align="center">
  <strong>Python三体模拟器</strong>
</p> 

# 介绍
《三体》是刘慈欣创作的长篇科幻小说，文中提到的三体问题比较复杂和无解。
该项目代码就是利用 Python 来模拟三体的运行，此项目代码完全共享，欢迎下载。

我们可以自己通过调整天体的初始坐标、质量和矢量速度等等参数来自定义各种场景来控制天体的运行效果。

# 效果图
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/dev/images/solar_system_3.png" width="80%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/solar_system_1.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/solar_system_2.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/three_body_1.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/three_body_2.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/sun_earth_jupiter.py.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/two_body_1.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/three_body_3.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/three_body_4.png" width="40%">
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/bodies_run.gif" width="90%">

# 抖音课堂：
<img src="https://gitcode.net/pythoncr/three_body_sim/-/raw/master/images/douyin_x.jpg" width="40%">

# 课程下载
https://gitcode.net/pythoncr/three_body_sim

# 目录说明

**bodies** 天体类、包含太阳以及太阳系中的所有行星
 
**common** 公共库代码
  
**data** 构建天体的 JSON 数据
   
**scenes**  各种天体系统运行场景 **演示入口**

**textures**  天体纹理图片

**simulators** 天体系统运行模拟器
    
**images** 图片

# 安装 Python 库
```shell script
# 先安装基础包
pip install -i http://pypi.douban.com/simple/ --trusted-host=pypi.douban.com ursina pyqt5 pyglet mayavi
```

# 支持三种模拟器
```shell script
# 进入当前代码的根目录
cd e:\three_body_sim\
SET PYTHONPATH=%CD%

# matplotlib 模拟器（支持动画和导出 gif 文件）
python simulators\mpl_simulator.py

# mayavi模拟器
python simulators\mayavi_simulator.py

# ursina模拟器
python simulators\ursina_simulator.py
```

# 模拟场景运行
```shell script
# 进入当前代码的根目录
cd e:\three_body_sim\
SET PYTHONPATH=%CD%

# 场景
# 从运行demo开始
python scenes/demo.py

# 三体场景
# 3个太阳、1个地球（效果1）
python scenes/three_body_01.py

# 3个太阳、1个地球（效果2）
python scenes/three_body_02.py

# 太阳系场景
# 以下展示的效果为太阳系真实的距离
# 由于宇宙空间尺度非常大，如果按照实际的天体大小，则无法看到天体，因此需要对天体的尺寸进行放大
python scenes/solar_system_1.py

# 以下展示的效果非太阳系真实的距离和大小
# 1、由于宇宙空间尺度非常大，如果按照实际的天体大小，则无法看到天体，因此需要对天体的尺寸进行放大
# 2、为了达到最佳的显示效果，对每个行星天体的距离进行了缩放
python scenes/solar_system_2.py

# 以下展示的效果非太阳系真实的距离和大小
# 1、由于宇宙空间尺度非常大，按照实际的大小无法看到行星天体，因此需要对天体的尺寸进行放大
# 2、为了达到最佳的显示效果，对每个行星天体的距离进行了缩放
# 3、加入了小行星的演示效果
python scenes/solar_system_3.py

# 太阳、地球运行效果
python scenes/sun_earth.py

# 太阳、地球、木星运行效果
python scenes/sun_earth_jupiter.py 
```

# 免责声明
* 本项目开源代码和资料主要用于教学，任何直接或间接因使用我方的任何内容所导致的全部后果与我方无关，若使用者无法对使用我方内容后的任何后果负责，请不要使用我方的任何内容。若我方的任何内容侵犯了您的法律权益，请联系pythoncr@126.com，作者会第一时间删除侵权内容。