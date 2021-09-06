# python笔记

- python文件/文件夹操作
```
# 文件夹不存在时自动创建
os.makedirs(path) 创建多级目录。父目录不存在时会创建。
os.makedir(path)  创建单级目录。父目录不存在时不会创建。

# 文件夹不存在时自动创建
if not os.path.exists(path):
    os.makedirs(path)

# 获取 home 目录路径
os.path.expanduser("~")

# 返回路径 path 的目录名称
os.path.dirname(path)

# 如果 path 指向一个已存在的路径或已打开的文件描述符，返回 True。对于失效的符号链接，返回 False。
os.path.exists(path)

# 如果 path 是 现有的 常规文件，则返回 True。
os.path.isfile(path)

# 如果 path 是 现有的 目录，则返回 True。
os.path.isdir(path)
```

|字符  |意义|
|:-----|:-----|
|'r'|读取（默认）|
|'w'|写入，并先截断文件|
|'x'|排它性创建，如果文件已存在则失败|
|'a'|写入，如果文件存在则在末尾追加|
|'b'|二进制模式|
|'t'|文本模式（默认）|
|'+'|打开用于更新（读取与写入）|








