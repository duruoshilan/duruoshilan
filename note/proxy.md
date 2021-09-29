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
# centos 安装
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

```
# ubuntu 安装
apt install shadowsocks-libev

# 备份/etc/shadowsocks-libev/config.json
# 修改客户端systemd服务单元配置文件 /lib/systemd/system/shadowsocks-libev-local@.service 中 ss-local加载的配置文件名
# 编辑 /etc/shadowsocks-libev/下的配置文件
{
    "server":"server ip", 
    "mode":"tcp_and_udp", 
    "server_port": 8888 , 
    "local_address":"127.0.0.1", 
    "local_port":1080, 
    "password":" ACRrobo9ymXb ", 
    "timeout":60, 
    "method":"chacha20-ietf-poly1305" 
}

systemctl start shadowsocks-libev-local@service

apt install proxychains4
# 编辑 /etc/proxychains4.conf 配置文件
# 修改 socket5
```

