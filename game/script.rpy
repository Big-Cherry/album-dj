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

# 游戏在此开始。

label start:
    
    # 开始东极岛故事线
    jump dj_start
