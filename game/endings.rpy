# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: endings.rpy
#  description: (story scripts)  Endings
#  Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

label endings:

label .end01:
    # 跳过回忆
    "【End 01】 你的毕业论文得了优秀。"
    "游戏结束了。"
    return

label .end02:
    # 咕咕结局
    "【End 02】 你咕咕了群友们，弄哭了冠军。"
    $ gugu_value += 10
    "当前咕咕值：[gugu_value]，当前敦煌值：[dunhuang_value]"
    "游戏结束了。"
    return

label .end03:
    # 和学妹在一起了
    "【End 03】 经过这次旅行，小茶解开了心结，也投入了你的怀抱。"
    "Good Ending"
    return


