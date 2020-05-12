# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: scripts.rpy
#  description: (story scripts) Game starts from here
#  Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

# 全局属性定义区：

default dunhuang_value = 0
default dj_tips = "empty"

# 特殊图像

image black = Solid("#000")

# 常用转场

define phototake = Fade(0.1, 0.0, 0.1)
define fade = Fade(1.0, 1.0, 1.0)

init python:
    import random

    # 注册歌唱通道
    renpy.music.register_channel('sing', mixer='music', loop=False, stop_on_mute=True)

# 游戏启动时的Splash界面

label splashscreen:
    $ renpy.movie_cutscene('video/splash.avi')
    scene splash with fade
    pause
    return

# 游戏在此开始。

label start:

    stop music fadeout 1.0    
    # 开始东极岛故事线
    jump dj_start
