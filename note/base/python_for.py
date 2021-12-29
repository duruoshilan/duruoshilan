可迭代对象      可循环
index           索引

一、str
s = "hello"   可迭代对象

for i in s:
    print(i)

for i in input():
    print(i)

s = "hello"
for i in range(5):
    print(s[i])

二、range
range(5)        range(0, 5)     [0, 1, 2, 3, 4]
区间 [结束)

range(1, 5)     range(1, 5)     [1, 2, 3, 4]
区间 [开始，结束)

range(1, 5, 2)  range(1, 5, 2)  [1, 3]
区间   [开始，结束，步长)

range(-10, 10, 2)
range(10, -10, -2)

for i in range(10):
    print(i)

三、list
list  列表 [1, 2, 3, 4, 5] 
      下标  0  1  2  3  4
列表使用中括号，下标从0开始。

for i in [1, 2, 3, 4, 5]:
    print(i)

for i in list(range(10)):
    print(i)

for i in input().split():
    print(i)

l = ['h', 'e', 'l', 'l', 'o']
for i in l:
    print(l)

for i in range(5):
    print(l[i])


while 循环
可能大部分用在不知道循环次数的情况。条件循环。

n = 10
while n > 0:
    print(n)
    n -= 1

while True:  循环执行
while False: 循环不执行


循环控制

break       跳出当前循环
continue    直接进入下一次循环，当前循环的后续语句不执行

