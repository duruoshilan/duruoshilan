if 语句 - 如果那么，如果那么否则

1、输入一个整数，判断这个数字是奇数还是偶数。

n = int(input())
if n % 2 == 0:    # 当条件为 True 时执行。
    print("偶数")
else:
    print("奇数")

pass 空语句

2、用户名、密码、验证码。
if u == "张三" and p == 12345678:
    if v == 2345:
        print("登录成功")
    else:
        print("验证码错误")
else:
    print("用户名或密码错误")

else 是 if 对应条件的反条件。

3、对成绩判断。 0 ～ 100 分。
n = 100
if n > 10:
    print(10)
if n > 20:
    print(20)
if n > 80:
    print(80)
if n > 100:
    print(100)

4、对成绩判断。 0 ～ 100 分。
n = 100
if n > 10:
    print(10)
elif n > 20:
    print(20)
elif n > 80:
    print(80)
else:
    print(100)

等价于

n = 100
if n > 10:
    print(10)
else:
    if n > 20:
        print(20)
    else:
        if n > 80:
            print(80)
        else:
            print(100)









