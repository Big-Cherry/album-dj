# ###########################################################
#            Copyright (c) 2020 BigCherry Team
#                   All Rights Reserved 
#
#  filename: scripts.rpy
#  description: (story scripts) DongJi story START
#  Author: Wentian Bu
#  Version: 1.0
#  
# ###########################################################

label dj_start:

scene black with Fade(0.5, 0.5, 0.5)

image text1 = Text("生是你的老百姓", xalign=0.5, yalign=0.45, size=30)
image text2 = Text("死是你的小精灵", xalign=0.5, yalign=0.55, size=30)

show text1 with dissolve
pause 0.5
show text2 with dissolve
pause 1
hide text1
hide text2
with dissolve

pause 2

jump .s01room



label .s01room:

    play music home

    show text "2020年3月9日" at truecenter with dissolve
    pause 1

    scene home room with fade

    "你正在家中赶着毕业论文……"
    "一阵眩晕……" with vpunch
    
    scene home room with Fade(0.1, 0.0, 0.8, color="#fff")

    "啊！？？？难道我感染了新冠病毒？妈妈，救我~~"

    scene home room with Fade(0.0, 1.0, 3.5, color="#000")
    
    "嗯？怎么回事？我刚才晕倒了吗？"

    play sound notify
    
    "群消息""Conway邀请你加入群“小精灵和老百姓”"
    "什么小精灵？什么老百姓？"
    "莫非……"

    menu:
        "要不要加入这个群呢？"
        "虽然有点疑惑，但还是点了加入群聊":
            pass       
        "论文要写不完了……":
            jump dj_endings.end01
        "看来今天身体不太舒服，还是睡觉吧":
            show home room with Fade(2.0, 1.0, 1.5)
            "诶？我还是进了这个群"
            
    han"前四天吧。"
    zheng"我都行"
    lian"那就前四天？"
    nuo"好哇"
    ming"为啥才四天，不是九天假吗？"
    conway"狗屎"
    "……""……"
    "等等……九天假？"
    "他们在讨论毕业旅行吗？"
    "不对，现在是……"
    "2018年8月13日！！！"
    "这是怎么回事！"
    "雷萌萌""为啥叫小精灵和老百姓？"
    conway"生是你的小精灵，死是你的老百姓，这都不知道？"
    bwt"让我看看谁比我渣"
    "……""……"
    "这不是当时去东极岛的群吗？"
    "莫非……"
    lian"我刚才看到樱桃神进来了啊，怎么一直不说话？"
    bwt"@樱桃神 爆个照吧"
    shou"樱桃神你前四天可以吗？"
    menu:
        "怎么回答大家呢？"
        "（冠军表情包）我可以":
            "奇怪……为什么2019年的表情包在这个时间线也能用？"
            
        "（鸽子表情包）一定来，一定来":
            jump dj_endings.end02

        "听说这次行程艰苦，我还是算了吧，溜了溜了":
            jump dj_endings.end01
        
    wqbh"@樱桃神 哇，你就是传说中的樱桃神吗？"
    me"新人学妹爆个照吧！"
    wqbh"我不我就不我偏不，有大佬罩着我"
    "尴尬……竟然被学妹拒绝了"
    conway"@主席，你会做海鲜吗？"
    "主席""……我会瞎煮"
    "果然还是那群敦煌人，话贼多，不一会儿就99+了。"
    "你被万千儿残忍拒绝了，看来这个学妹不太好惹……"
    
    # 要不要带一个学妹呢？
    default dj_withgirl = False

    menu:
        "你是否也要带个学妹呢？"
        "我觉得可以":
            $ dj_withgirl = True
            
        "我觉得不行":
            jump .s02apartment
        "我TM也想带但是没有啊……":
            jump .s02apartment


label .s02apartment:
    scene black with fade

    show text "2018年9月28日" at truecenter with dissolve
    pause 1

    scene domitory with fade
    "时间过的真快...一不小心就到了九月底。"
    "你们约定的旅行时间就要到了，车牌船票和住宿也都妥当。"
    "但原本自告奋勇要煮海鲜的主席和一直想和大家一起玩的子玥姐姐最终选择了咕咕，有一些遗憾呢。"

    play sound opening
    "突然，你的手机响了，是一个来自舟山的电话号码，很奇怪，但你还是接听了。"
    "原来是卖船票的淘宝老板。"

    "老板""那个...你们一起的是有个叫万千儿的是吗？"
    me"是啊...怎么了？"
    "老板""她是个外国人吗？"
    me"可能是吧，而且她还有大佬罩呢"
    "老板""这样啊，没关系，也跟你们确定一下，你们准备预定的船票是10月3日最早的那班对吧？"
    me"是的，没错，最早的那班。对了老板，听说最近有台风“康妮”，会影响吗？"
    "老板""现在也没得个准，但还得看之后政府的公告吧，你们别担心。"
    me"嗯嗯好的。"

    "于是你在群聊里跟大家告知了这个情况"
    yourong"有台风？那不如直奔钓鱼岛，插国旗！"
    yinyin"咱们有plan B吗？"
    lian"Plan B...窝在舟山打污诺？"
    nuo"？？？凭啥打我？"
    zhuang"放心，上海结界"
    wqbh"对了，我们自己做饭吗？"
    "子玥姐姐""本来是该我做饭的，哎...对不起大家"
    "小汪""烧烤的话我没问题，但民宿有烧烤架吗？"
    zhuang"学化学的专业生火"
    zheng"荒岛求生？"
    dan"大吉大利，今晚吃鸡"
    conway"一出好戏……突然有点害怕"
    "你突然也有点害怕"
    "这几天大家都在疯狂水群，看来对行程都十分期待，你也开始收拾行李箱……"

    jump dj_102












