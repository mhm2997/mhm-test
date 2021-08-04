import random
money = 5000
num = random.randint(1,100)
login = 1
while True:
    if input("请输入用户名：") == "admin" and input("请输入密码：") == "123456":
        print("登录成功，登录",login,"次,下面开始猜数字：")
        print("您的初始金额为：￥",money)
        break
    else:
        print("登录失败",login,"次，账号或密码不正确，请重试。")
        login = login + 1
while True:
    guess = int(input("请输入您猜的数字:"))
    if num > guess and money > 0:
        money = money - 500
        print("小了","剩余￥",money)
    elif num < guess and money > 0:
        money = money - 500
        print("大了","剩余￥",money)
    elif num == guess:
        money = money + 10000
        print("恭喜您猜对了,奖励￥10000", "剩余￥", money)
        chose = input("您好，是否开启第新一轮游戏(是：1,不是：2)：")
        if chose == "1":
            num = random.randint(1, 100)
        else:
            print("游戏结束，再见。")
            break
    else:
        print("账户余额不足，游戏结束。")