# 配置代理

- 取消manjaro默认终端代理
```
unset ALL_PROXY
unset all_proxy
```

- 安装 shadowsocks-qt5

- 安装 proxychains-ng
```
vim /etc/proxychains.conf
socks5 127.0.0.1 1080
```

- 配置 .zshrc
```    
alias pc="proxychains4"
```