
  数据：字母、数字、符号 ....

  数据分类
    1、数据类型：文本（str），数字（int, float, complex）
    2、数据之间转换：
        str -> int
        str -> float
        int -> str
        int -> float
        float -> int
        float -> str

    int('123')

变量：存储数据。

    1、如何存储。 '='     n = 5
    2、变量类型。  n = 5   n = 1.2  n = 'hello'
    3、变量类型转换。   n = int(n)  n = str(n)
    4、变量的命名规则。
        - 字母、数字、下划线组成。
        - 不得以数字开头
        - 区分大小写
        - 不得以关键字/保留字命名
    
    变量如何获取数据？
        n = 10
        n = input()
    变量如何显示自己的数据？
        n
        m = n
        print(n)

    
输入 input()

    1、input("请输入****")
    2、input 返回值。    n = input()   返回str类型
    3、input 和 split 之间的关系。
        input 输入 ---> str
        split 分割 str ---> list 列表  默认以空格切割

        input().split()
        "hello world".split()   ['hello', 'world']







