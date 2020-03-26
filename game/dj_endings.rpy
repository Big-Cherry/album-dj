# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: endings.rpy
#  description: (story scripts) Dongji Endings
#　Story Author: Alan Li, Conway Tan, Wentian Bu
#  Script Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

label dbgend:
    scene dbg dev
    "前方施工，禁止通行"
    "好吧，看来前面还没有开发完呢，下次再来看吧。"
    return

label dj_endings:
label .end01: # By Alan Li
    # 跳过回忆
    "End 01 - 你的毕业论文得了优秀。"
    return

label .end02: # By Wentian Bu
    # 咕咕结局
    "【End 02】 你咕咕了群友们，弄哭了冠军。"
    $ gugu_value += 10
    "当前咕咕值：[gugu_value]，当前敦煌值：[dunhuang_value]"
    "游戏结束了。"
    return

label .end03: # By Alan Li
    # 逃离失败成为难民
    "你们逃离失败被困在舟山客运站，过上了难民生活。"
    "End 03 - 难民的麦当劳"
    return

label .end04: # By Conway Tan
    "特别关注""万千儿：❤❤❤"
    "特别关注""万千儿：[[分享歌曲]一见钟情"
    "难道……她看出来了我的心思？这一切来得太突然了……"
    "还是试探性回复一下吧……"
    me"等等我"
    "特别关注""万千儿：好"
    "嗯……找个借口先走吧，顺便叫辆滴滴。"
    me"我有个同学家在宁波，他刚才邀请我去玩儿。"
    conway"啊？那你不和我们走了？"
    me"嗯，我已经把票给改了。"
    yinyin"好吧，台风来了，你路上小心。"
    # 上车场景
    scene bg taxi
    with fade
    "还是看看票吧，兴许运气好还有剩的呢？"
    "？！还有一张票！天助我也！管他呢，买了再说！"
    # 到达宁波站场景
    scene bg station
    with fade
    "车快开了，得赶快了。" 
    # 脚步声
    wqbh"桃神！桃神！" with vpunch
    wqbh"桃神你真的来了啊！"
    wqbh"欸桃神你拉我去哪儿啊"
    me"去珠海啊！快误车了，赶紧进去吧！"
    wqbh"欸欸欸？……"
    "……""……"
    hide bg with dissolve
    "你和万千儿一起前往了珠海，这一路上你们聊了很多！你们感觉和彼此情投意合，恭喜你们在一起了！"
    "End 04 - 意外的美好"
    return


label .end05:
    scene bg train
    me"呼……终于上车了，看看敦煌人们发的照片吧。"
    "有点头晕……"
    "那间鬼宅……海底古墓、鬼宅密室，奇怪的铃铛声和带着海腥味的异想、神秘的人人网消息，杭州密云东极敦煌，又究竟意味着什么秘密？"
    "……"
    "还是去洗个脸吧。"
    "诶？厕所门口那两个人一长一短好熟悉啊……"
    me"有容？？你不是昨天就走了吗？！"
    yourong"啥玩意！好巧啊桃神！你也是这班车？"
    me"小杰瑞？你又是哪冒出来的"
    "小杰瑞""我们没买到座位，只有无座了，只能在厕所门槛混了一晚上，太求惨了..."

    play sound "audio/sound/qqddd.mp3"
    "群通知""Conway邀请你加入群聊"
    "怎么还是这些熟人？"
    me"@Conway 这又建了个什么群？"
    "列车广播""前方到达北京站，此次列车终点——"
    pause 1
    "列车广播""密云"

    "End 05 - 行进的列车"
