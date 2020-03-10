# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
# 说明：该角色表可用于简化对话的书写。可以只在这里添加常用角色。
# 该部分之后可能会被移动到单独的文件。

define conway = Character("冠军")
define lian = Character("连南")
define bwt = Character("小萝卜")
define nuo = Character("诺诺")
define ming = Character("小明")
define wqbh = Character("万千儿")
define shou = Character("兽兽")
define tea = Character("小茶")
define lei = Character("雷永宁")
define han = Character("韩韩")
define zhuang = Character("壮壮")
define yourong = Character("有容")
define yinyin = Character("淫淫")
define zheng = Character("郑瑜坤")



default gugu_value = 0
default dunhuang_value = 0
# 游戏在此开始。

label start:
    image text1 = Text("生是你的老百姓", xalign=0.5, yalign=0.45, size=30)
    image text2 = Text("死是你的小精灵", xalign=0.5, yalign=0.55, size=30)

    show text1
    with dissolve
    pause 0.5
    show text2
    with dissolve
    pause 1
    hide text1
    hide text2
    with dissolve

    pause 2
    play music "audio/main.mp3"

    show text "2020年3月9日" at truecenter
    with dissolve
    pause 1

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。
    scene bg room
    with fade

    "你正在家中赶着毕业论文……"

    
    "一阵眩晕……" with vpunch
    
    show bg room
    with Fade(0.1, 0.0, 0.8, color="#fff")

    "啊！？？？难道我感染了新冠病毒？妈妈，救我~~"

    show bg room
    with Fade(0.1, 0.0, 3.5, color="#fff")
    
    "嗯？怎么回事？我刚才晕倒了吗？"

    play sound "audio/qqddd.mp3"
    
    "群消息""Conway邀请你加入群“小精灵和老百姓”"

    "什么小精灵？什么老百姓？"
    "莫非……"

menu:
    "虽然有点疑惑，但还是点了加入群聊":
        jump lb1
    
    "论文要写不完了……":
        jump badend

    "看来今天身体不太舒服，还是睡觉吧":
        jump slp
        
label slp:
    show bg room
    with Fade(0.1, 0.0, 1.5, color="#000")

    "诶？我还是进了这个群"

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。
label lb1:

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

    lei"为啥叫小精灵和老百姓？"
    conway"生是你的小精灵，死是你的老百姓，这都不知道？"
    bwt"让我看看谁比我渣"
    "……""……"

    "这不是当时去东极岛的群吗？"
    "莫非……"

    lian"我刚才看到樱桃神进来了啊，怎么一直不说话？"
    bwt"@樱桃神 爆个照吧"
    shou"樱桃神你前四天可以吗？"

    "怎么回答大家呢？"

menu:
    "（表情包）我可以":
        "奇怪……为什么2019年的表情包在这个时间线也能用……"

    "（表情包）一定来，一定来":
        jump gugu
    
label cnt:
    show sylvie tea

    # 此处显示各行对话。

    tea "您已创建一个新的 Ren'Py 游戏。"

    tea "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    return

label gugu:
    "你咕咕了群友们，弄哭了冠军。"
    $ gugu_value += 10
    "当前咕咕值：[gugu_value]，当前敦煌值：[dunhuang_value]"

    # 此处为游戏结尾。
label badend:
    "游戏结束了。"
    return
