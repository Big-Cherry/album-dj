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

label display_value:
    "你的敦煌值是：[dunhuang_value]，超过了99%%的玩家，真NB！"
    return

label dj_endings:
label .end01: # By Alan Li
    scene bg end01_1 with fade
    "你的毕业论文得了优秀。"
    scene bg end01_2 with dissolve
    "End 01 - 优秀的毕业论文"
    scene black with Fade(3.0, 1.0, 0.0)
    jump display_value

label .end04: # By Conway Tan
    stop music fadeout 2.0
    play sound notify
    "特别关注""万千儿：{image=images/other/heart.png}"
    play sound notify
    "特别关注""万千儿：{image=images/other/yjzq.png}"
    "难道……她看出来了我的心思？这一切来得太突然了……"
    "还是试探性回复一下吧……"
    play music express_love fadein 1.0
    me"等等我"
    play sound notify
    "特别关注""万千儿：好"
    "嗯……找个借口先走吧，顺便叫辆滴滴。"
    me"我有个同学家在宁波，他刚才邀请我去玩儿。"
    conway"啊？那你不和我们走了？"
    me"嗯，我已经把票给改了。"
    yinyin"好吧，台风来了，你路上小心。"

    scene taxi night with fade
    "还是看看票吧，兴许运气好还有剩的呢？"
    "？！还有一张票！天助我也！管他呢，买了再说！"

    scene nb station night with fade
    "车快开了，得赶快了。" 
    play sound run_step
    wqbh"桃神！桃神！" with vpunch
    wqbh"桃神你真的来了啊！"
    wqbh"诶桃神你拉我去哪儿啊"
    me"去珠海啊！快误车了，赶紧进去吧！"
    wqbh"诶诶诶？……"
    "……""……"
    scene bg end04 with fade
    "你和万千儿一起前往了珠海，这一路上你们聊了很多！你们感觉和彼此情投意合，恭喜你们在一起了！"
    "End 04 - 意外的美好"
    stop music fadeout 3.0
    scene black with Fade(3.0, 1.0, 0.0)
    jump display_value


label .end05:
    scene bg end05 with fade
    me"呼……终于上车了，看看敦煌人们发的照片吧。"
    "有点头晕……"
    "那间鬼宅……海底古墓、鬼宅密室，奇怪的铃铛声和带着海腥味的异想、神秘的人人网消息，杭州密云东极敦煌，又究竟意味着什么秘密？"
    "……"
    "还是去洗个脸吧。"
    "诶？厕所门口那两个人一长一短好熟悉啊……"
    me"有容？？你不是昨天就走了吗？！"
    yourong"啥玩意！好巧啊桃神！你也是这班车？"
    me"小杰瑞？你又是哪冒出来的"
    "小杰瑞""我们没买到座位，只有无座了，只能在厕所门口混了一晚上，太求惨了..."

    play sound notify
    "群通知""Conway邀请你加入群聊"
    "怎么还是这些熟人？"
    me"@Conway 这又建了个什么群？"
    "列车广播""前方到达北京站，此次列车终点——"
    pause 1
    "列车广播""密云"

    "End 05 - 行进的列车"
    scene black with Fade(3.0, 1.0, 0.0)
    jump display_value

label .g_end06:
    scene dj villa room day with fade
    play music everything_settled fadein 3.0
    """
    你睁开眼睛，发现天已经大亮，一看手机快十点了。昨天晚上居然和小茶在一张床上和衣睡着了。

    小茶也醒了，正红着脸看着你，却又忍不住笑了。

    你突然想起来今天的返程船票是十一点多的，该收拾东西准备走了。

    你整理好衣服走出房间，对面的房间传出连南的磨牙声，还有壮壮的鼾声。突然啪的一声，应该是冠军又梦中扇人了。

    你看了一下群消息，发现他们四点多起床去看了日出。群里还有人说：“@樱桃神 666啊，那就不打扰了/斜眼笑”。

    看来他们都发现了啊……
    """
    me"他们今天去看日出了呢。"
    tea"嗯，我看到他们的说说了。"
    me"遗憾吗？"
    tea"有…那么一点点。不过，跟你在一起，我也一样开心呢。"
    
    scene dj road leave with fade
    """
    你和小茶收好行李离开了民宿，向码头走去。

    今天风有点大，太阳也被云层挡住了，海面上也并不平静，台风快要来了。

    路上很多旅客拖着行李，行色匆匆地前往码头方向，看来大家都想抢在台风来临前离岛。
    """
    scene ship middle with fade
    "返程的票是中等舱。海上风浪有点大，你感觉有点晕船。"
    tea"怎么了？看你好像有点不太舒服，是不是晕船啊？"
    me"嗯，有一点。今天浪比较大，晃得难受。"
    tea"我去找工作人员要点晕船药吧。"
    me"不用了，就是有一点头疼。"
    tea"那你在我肩膀上靠着睡一会儿吧，稍微好受一点。"
    me"你太瘦了，压在你肩膀上你会很累的。"
    "小茶傲娇了起来："
    tea"哼，爱靠不靠。"
    "然而很快又轻轻拉起了你的手，"
    tea"桃桃，你还是靠一会儿吧，我不累的。我也想成为你可以依靠的人啊。"

    scene zs station with fade
    """
    轮船抵达了舟山市，风更大了，天上的云在翻滚着，台风真的要来了。你们吃了点麦当劳，然后立即坐车前往了宁波。

    到达宁波已经快要晚上八点。一路舟车劳顿，今天居然只吃了一顿饭。

    等赶到酒店安顿下来，已经九点了。
    """
    scene zs hotel with fade
    me"好饿啊，我们赶紧点外卖吧，再晚的话可就真没得吃了。"
    tea"哼，跟你出来我尽在赶路挨饿，男朋友当得一点都不合格哦。"
    me"这不是怕台风来了嘛，不然我们就去商圈吃完再回来了。"
    me"而且…某人之前说要做饭给我吃，不也没做嘛。"
    tea"那不是因为某人缠着我在房间里聊天吗？啧啧啧"
    me"好啦好啦，美团饿了么上这么多好吃的，你看你想吃什么呀？"
    tea"嗯…我想吃花甲粉！"
    tea"下次我们单独出来玩订一个民宿，我做给你吃。小茶做的蛋炒饭超好吃哦！"
    "吃完外卖，已经十一点了。赶了一天的路，两个人都很累，于是打了会儿王者就早早休息了。"
    "……"
    
    scene taxi day with Fade(2.0, 2.0, 1.0)
    """
    醒来已经是中午了。收拾好行李来到楼下，发现台风真的来了。

    外面下着大雨，树木在狂风中摇摆着，街边的自行车被吹倒一片。

    舟山所有的客运大巴都停运了，群里昨天在舟山享受大别墅的朋友们现在纷纷后悔没有早点走，现在只好高价包了四辆出租车，在跨海大桥上风雨飘摇。
    
    你们叫了辆滴滴前往火车站。
    """
    me"跟你早走一天可太正确了，他们现在好惨，一辆车七百好不容易才打到车。"
    tea"他们晚点应该就能到宁波了吧？"
    me"是的。要是我们的票稍微再晚一点，说不定还能和他们一起吃海底捞。你不是还没吃过吗？"
    tea"切，南京又不是没有。"
    me"大家一起捞才热闹嘛。"
    tea"可是人家第一次想和你单独去吃啦。"
    me"那我们明天到了就去吃？仙林大学城店好像离你们学校挺近的，据说冠军在那里一个人吃成了黑海会员。"
    tea"好呀！刚才诺诺姐在群里说伊比利亚黑猪肉超好吃诶，我也想吃！"
    scene nb station plat with fade
    """
    站台上，狂风夹杂着雨点再一次肆虐。你们牵着手走上了前往南京的列车。

    列车启动了，窗外的景物在风雨中摇晃着缓缓后退。

    过去的三个月里，如遇知己的聊天、怦然心动的瞬间、默默埋藏的暗恋、紧紧相拥的夜晚……
    
    甜蜜美好的未来画卷，正在徐徐展开……

    Good Ending - 徐徐展开的画卷
    """
    stop music fadeout 3.0
    scene black with Fade(3.0, 1.0, 0.0)
    jump display_value

label .g_end07:
    scene dj villa room day with Fade(1.0, 1.0, 2.0)
    play music lonely_walk fadein 2.0
    "门外传来一群人凌乱的脚步声和说话声，还有人砰砰砰地敲门。"
    "你迷迷糊糊起床打开门，发现是连南。"
    lian"你醒啦，我们四点多看日出，敲你们门敲了半天都没反应。二人世界怎么样？"
    me"有毒吧，啥都没有。咋了？"
    lian"就跟你说一声，你们的票是十一点的千万别睡过了。困死爸爸了。"
    lian"这会儿都十点了，你们别睡了，当心误船。"
    me"好，我知道了。"
    "回到房间里，发现小茶刚才也醒了，正在看手机。"
    tea"啊！他们今天早晨去看日出了？为啥没人跟我们说啊。"
    me"嗯。他们四点多起来的。连南说早晨敲了半天门，我们俩都没听到，只好作罢。"
    tea"都怪你，昨天晚上在外面说那么晚害得我没起来。我也想去看日出啊！"
    me"对不起，昨天晚上我该提前问问他们的。我记得之前他们有人做了旅游攻略，结果我没有细看。"

    scene dj road leave with fade
    """
    收拾好行李，你和小茶走在去码头的路上。

    今天的风大了许多，天上的云翻涌着，海面也不再平静，台风就要来了。

    小茶穿着一件运动外套，在大风下显得很是单薄。

    你轻轻牵起小茶的指尖，她的手有点凉。
    """
    me"风这么大，你冷吗？"
    tea"嗯……有点儿。"
    me"那我把外套给你披着吧。"
    """
    你脱下外套披在她身上。大风瞬间撕碎了仅存的一点热量，然后肆无忌惮穿过短袖的袖口。

    还是咬咬牙吧，上船就不冷了。
    """
    me"我们走快点吧，十一点的船票，时间有点紧张了。"
    tea"可是我的行李好重啊。"
    "你松开了牵着她的左手，把她的背包背在背上，然后又接过了箱子。"

    scene ship middle with fade
    """
    码头入口排着长队，人头攒动，你尽力将她护在身前的一小片区域。

    中舱位于甲板之下，入口的楼梯又高又窄。

    离开船还有十分钟，你们终于找到了座位坐定下来。
    """
    tea"哥哥，我好饿啊，早饭都没吃还走了好远。"
    me"我背包里还有巧克力，我给你拿。"
    tea"女孩子巧克力吃多了不好。"
    me"总比饿着好吧，你吃一块儿稍微垫一下，我们下船了就去吃饭。"
    me"而且为什么女孩子巧克力吃多了不好啊，我从来没听说过这种说法。"
    tea"算了，下船再吃吧。我也不记得了，反正就是不好。"
    tea"哥哥你真不会照顾女孩子。这次跟你出来我都是饥一顿饱一顿的，天天赶路饿肚子。我之前跟小殷在一起他就特别体贴我。"
    me"……对不起，这次出来玩确实舟车劳顿的比较辛苦。以后我们单独出去行程可以更轻松些。"
    """
    开船了，海上风浪有点大，晃得你有点晕船，你昏昏沉沉地靠在座位上睡着了。

    一觉醒来船已经在舟山码头靠岸，你们下了船，在附近吃了些东西，然后去了客运站，准备坐大巴车前往宁波。

    大巴车一路颠簸，到了宁波客运站已经是晚上八点。上次吃饭还是下午两点多，你们都已经饥肠辘辘。

    等到了酒店安顿下来，已经九点多了。
    """
    
    scene zs hotel with fade
    tea"我好饿啊，跟你出来玩我可太惨了，一路上饿肚子。"
    me"哎，怪我没想到，当时上车前应该买点东西带着的。刚才坐出租车来酒店的时候感觉这酒店附近挺荒凉的，我们还是点外卖吧。"
    "打开美团饿了么看了一圈，发现附近真的没有什么好吃的，无奈之下还是选择了麦当劳。"
    "吃完饭以后，小茶坐在床上刷手机。"
    tea"哥哥，要不你把明天的票改成回北京的吧。"
    me"怎么了？不是说好了去南京陪你几天的吗？"
    tea"小陶他们回襄阳了。刚才小陶他们在群里约聚会呢，我已经买了明天回襄阳的车票了。"
    me"是你们暑假办衔接班的朋友们？"
    tea"对。我好久没见到他们了，挺想念的。而且后天是小陶的生日！我差点搞忘了！"
    me"小殷不去吗？"
    tea"他也去。"
    me"你现在不是和他……挺尴尬的嘛。"
    tea"就当是朋友一起庆生吃个饭吧。做不了恋人还是可以做朋友的嘛。"
    me"……好吧，那我把票改了，等以后有机会再来陪你吧。"
    tea"嗯嗯，哥哥最好了！"
    "……"

    scene nb station day with fade
    "次日中午，你和小茶一起来到了车站。"
    "小茶的车是下午两点，候车室的检票口前已经排起了长队。小茶拖着行李站到了队伍里。"
    tea"哥哥，我下个月过生日你会来陪我吗？"
    me"emmmmm，我不知道，也许会来吧。"
    tea"……好吧，我还以为你肯定会来呢。我超想哥哥陪我过生日的。"
    "开始检票了，人流正在缓缓向前移动。"
    tea"哥哥，再抱一下好吗？"
    me"嗯。"
    """
    你轻轻抱住了小茶，熟悉的清香再一次勾起了你的回忆……
    
    襄阳街头的初见，彻夜不眠的畅谈，民宿清晨的相拥，星光璀璨的夜空……
    
    过去的三个月里，这段感情亲如兄妹一般；而埋藏在心底的喜欢，未来又该何去何从？

    Normal Ending - 埋藏心底的感情
    """
    stop music fadeout 3.0
    scene black with Fade(3.0, 1.0, 0.0)
    jump display_value


label .g_end08:
    scene dj villa room day with Fade(1.0, 3.0, 3.0)
    play music fragile_tenderness fadein 2.0
    "你迷迷糊糊听到一阵嘈杂，睁开眼睛发现是众人回来了。"
    me"你们干什么去啊？"
    zhuang"你才醒啊，我们早晨四点多本来准备叫你，"
    zhuang"结果你睡得跟死猪似的根本叫不醒，只好由你继续睡了。"
    lian"困死爸爸了。对了，你和小茶的返程船票是十一点多的，千万别误船了。我们先睡了。"
    """
    你一看手机，发现已经九点多了……

    你的心里还是很乱很乱，经历了昨天晚上的事情，你甚至有点不知道该怎么面对小茶了。

    也许，这是一起旅行的第一次，也是最后一次了吧……

    ……
    """
    
    scene dj road leave with fade
    """
    转眼十点多了，你和小茶拖着行李箱走在路上，两人都沉默无言。
    
    今天的风大了许多，天边的云在翻涌，海面也不再平静，台风快要来了。
    """

    scene ship middle with fade
    """
    返程的船票是中等舱，海上浪有点大，你有点晕船，昏昏沉沉地靠在座位上。
    
    虽然没有网，但是身边的小茶却一直在手机上看些什么，再也没有和你聊天。
    
    你试着跟她说了几句话，却再也没有曾经聊天的畅快，只剩下冷淡的回应和尴尬的氛围……
    
    昨天的中午你们坐船上岛时，还是像情侣一样聊天、一起依靠着休息；
    
    而经历了这短短二十四小时，却再也回不到过去那样亲密无间……
    
    大脑充斥着这些混乱的片段，你迷迷糊糊地睡着了。
    """

    scene nb street with fade
    """
    轮船回到了舟山市，天阴沉得厉害，风越来越大了。

    你们坐大巴车赶回了宁波，到的时候已经是晚上七点了。

    原本你们在这里订了一间酒店暂住一晚，但是目前这种尴尬的气氛，你也不知道到底应该怎么办……
    """
    tea"刚才我社长通知我，后天的辩论赛有一名辩手临时有事参加不了，需要我尽快赶回去替补。"
    tea"我已经改签了今晚九点返程的车票，时间有点紧张，我就先走了。"
    me"好，需要我送你去车站吗？"
    tea"不用了，我刚才叫了辆滴滴，直接坐车去就行了。"
    tea"现在也不早了，台风快来了，你也尽快回酒店休息吧。"
    me"那你路上注意安全，到车站了在群里发个消息，这样大家也放心。"
    tea"嗯嗯。"
    """
    小茶拖着箱子向路边走去。天色越发地昏暗，大风席卷着树叶和灰尘沿街飞扬。

    惨白的路灯照在车站前的广场上，那个小小的身影渐行渐远……
    
    也许，过去三个月的记忆，
    
    那无话不谈的日子，那怦然心动的感觉，那亲如兄妹的感情，那清新甜蜜的发香，本该是一场幻梦吧……

    Bad Ending - 渐行渐远的背影
    """
    stop music fadeout 3.0
    scene black with Fade(3.0, 1.0, 0.0)
    jump display_value
