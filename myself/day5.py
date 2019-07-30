import random
import easygui as g
g.msgbox("嗨，欢迎进入第一个界面小游戏^^")
secret=random.randint(1,10)
msg="不妨猜一下小甲鱼现在心里想的是哪个数字（1-10）:"
title="数字小游戏"
guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
while True:
    if guess==secret:
        g.msgbox("恭喜，猜中了")
        break
    else:
        if guess>secret:
            g.msgbox("猜大了。。。")
        else:
            g.msgbox("猜小了。。。")
        guess=g.integerbox(msg,title,lowerbound=1,upperbound=10)
g.msgbox("游戏结束")