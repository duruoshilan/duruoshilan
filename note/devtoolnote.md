# 开发工具

- 配置 python pip
```
默认情况下可能未安装 pip 一种可选解决方案是

python -m ensurepip --default-pip
pip install --upgrade pip

```

- 配置pip socket 代理
```
pip install pysocks
```

- visual studio code 配置
```
- 安装 sudo pacman -S code

- code 终端字体: NotoSansMono Nerd Font

- 拓展无法连接网络
    cd .vscode-oss
    vim argv.json
    添加一行： "enable-browser-code-loading": false
```

- 配置docker
```
- 安装 sudo pacman -S docker

- 设置权限
    sudo usermod -aG docker $USER
    重启系统 reboot

- docker 容器内代理

    FROM Ubuntu:18.04
    ENV MY_PROXY_URL="http://{username}:{password}@{proxy_ip}:{proxy_port}/"
    ENV HTTP_PROXY=$MY_PROXY_URL \
        HTTPS_PROXY=$MY_PROXY_URL \
        FTP_PROXY=$MY_PROXY_URL \
        http_proxy=$MY_PROXY_URL \
        https_proxy=$MY_PROXY_URL \
        ftp_proxy=$MY_PROXY_URL

    编译运行容器
    docker build -t proxy-test .
    docker run -it --rm --name proxy-test proxy-test /bin/bash
```

- 配置vim
```
vim ~/.vimrc

set ts=4         4个空格
set expandtab    tab换空格
set autoindent   自动缩进
syntax on        语法高亮
```