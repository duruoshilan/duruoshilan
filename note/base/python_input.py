一、数据：12345，hello，%\#。

    1、数据分类。
        字符串/文本（类型标识符：str）。
            'hello', "hello", 
            """
            h9q82
            37oridello
            """         (三重引号可以换行)

        数字
            - 整数（类型标识符：int）。
                23784，23490，-234
            - 浮点数（类型标识符：float）。
                3.14，0.618 （小数）
            - 复数（类型标识符：complex）。
                考试不考，但是是数字的一种。

    2、数据的类型转换。
          int(3.14)    :  float -> int
          str(3.14)    :  float -> str
                          int -> float 
                          int -> str
                          str -> int
                          str -> float

          int(float("3.14"))  str -> float -> int

二、变量：存储数据

    1、定义变量。
        命名规则：
         - 由字母、数字、下划线组成。
         - 不得以数字开头。
         - 区分大小写。
         - 不得以 关键字/保留字 命名。import break continue
                                      if return while or is

    2、数据存储。
        通过赋值号( = )存储数据。必须先定义，再赋值。
           - 赋值号从右向左计算。

           number = 5
            - 定义了一个变量，名字为number
            - 将5赋值给number

    3、数据读取。

        number   直接写变量名就是取其中的值。

        print(number)   print是输出函数。

    4、数据转换。
        变量的类型由变量中的数据决定。
        a = 5       int
        a = 5.1     float
        a = "hello" str

        a = 5
        a = float(a)   a: int -> float , 5.0

三、计算

    1、算术运算。

        +、-、*、/、**、//、%

        pow(x, y)   求幂   和  ** 相同   pow(5, 6)  5 ** 6
        abs(x)   求绝对值
        round(x[, n]) 保留小数位，会四舍五入。  round(5.123, 2)
        divmod(x, y)   (x // y, x % y)
        
        int()          直接去除小数点后面所有内容
        import math
        math.ceil()    天花板   向上取整
        math.floor()   地板     向下取整
        math.trunc()   截断    

        运算结果：数值计算的结果。

    2、关系运算。

        >、<、<=、>=、==、!=

        运算结果：布尔值 (True 1 真, False 0 假)，非0即真。
                          1 真
                          2 真
                          0 假
                         -1 真
        5 > 2  ----> True
        5 < 2  ----> False
        5 == 2 ----> False

    3、逻辑运算。
    
        and(与) or(或) not(非)

        运算结果：
            1、not的结果是布尔值（True，False）。
                not 1 ----> False
                not 0 ----> True
                not 5 > 2 ----> False
            2、and 和 or 的结果由左右两边的值决定（短路特性）。
                - and 两边同时为真即为真。
                    5 and 2  ----> 2
                    5 and 1  ----> 1
                    1 > 0 and 5 > 2 ----> True and True ----> True
                    0 > 1 and 5 > 2 ----> False and True ----> False

                - or 两边只要有一个真，即为真。
                    5 > 10 or 10 < 20 ---> True
                    5 + 10 or 10 - 5 ---> 15

四、输入输出

    1、输入
        
        input()
        input("请输入...")

          （输入） ---> input() ---> str
             5     ---> input() ---> '5'
             1.1   ---> input() ---> '1.1'
             'h'   ---> input() ---> 'h'

        n = input()      #  n -> str
        n = input("请输入一个数字")  # n -> str
        n = int(input()) # (输入) -> input() -> str -> int -> n
        输入完后，要根据题目进行类型转换。


        分割：split()
            - 分割是对字符串进行处理，默认以空格隔开。
            - 分割后的类型是 list（列表）。
            - list(列表) 下标从0开始。
    
            'hello world'.split() ---> ['hello', 'world']
                                            0       1
            'abacadaeafad'.split('a') ---> ['', 'b', 'c', 'd', 'e', 'f', 'd']
                                             0   1    2    3    4    5    6
            input().split() <=> "".split()

            value = input().split() # "hello world".split()
            value # ['hello', 'world']
            f = value[0]  # hello
            s = value[1]  # world
    
    2、输出

        print()    
        print("hello, world")

        a, b, c, d = 1, 2, 3, 4
        print(a, b, c, d)  # 1 2 3 4

        print(a, b, c, d, end="-_-||")
        print(a, b, c, d, end="-_-||")
        1 2 3 4-_-|| 1 2 3 4-_-||
        end 指明该行结束符号，默认是 \n。  \n 表示换行。\t 表示tab  转义字符。

        print(a, b, c, d, sep="----")
        1----2----3----4
        sep 指明该行中多个输出之间的间隔符，默认是空格。

    3、格式化输出。

        左边格式，右边值。

        a, b, c = 1, 2.3, "hello"
        "a = %d, b = %f, c = %s" % (a, b, c)

        占位符
        %d   int
        %f   float
        %.2f float 保留2位小数
        %g   float 去掉无效0  (5.0->5)
        %s   str

五、刷题


