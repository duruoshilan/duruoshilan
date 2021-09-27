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

- 配置shadowsocks-libev
```
# install dependencies
yum install epel-release -y
yum install gcc gettext autoconf libtool automake make pcre-devel asciidoc xmlto udns-devel libev-devel -y

cd /etc/yum.repos.d/
wget https://copr.fedoraproject.org/coprs/librehat/shadowsocks/repo/epel-7/librehat-shadowsocks-epel-7.repo
yum update
yum install shadowsocks-libev

shadowsocks-libev 本地服务   shadowsocks-libev-local
shadowsocks-libev server服务 shadowsocks-libev-server
配置文件 /etc/sysconfig/shadowsocks-libev
配置文件 /etc/shadowsocks-libev/config.json

systemctl enable shadowsocks-libev
systemctl start shadowsocks-libev-local
systemctl status shadowsocks-libev-local
```
