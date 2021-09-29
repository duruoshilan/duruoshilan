# 安装 manjaro 后配置软件

- vmware workstation 安装 manjaro

 - 按e,添加 driver=intel 然后 ctrl+x 保存退出


- 开机启动 sshd
```
    systemctl enable sshd
```
 - 如果要取消开机自动启动则用下面的命令
```
    systemctl disable sshd
```

- 中断pacman
```
sudo rm /var/lib/pacman/db.lck
```

- 配置输入法

    - 参考代码 https://wiki.archlinux.org/title/Fcitx5_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)


    1. 安装软件包 fcitx5
    ```
    sudo pacman -S fcitx5
    ```

    2. 安装输入法引擎
    ```
    sudo pacman -S fcitx5-chinese-addons
    ```

    3. 安装输入法模块
    ```
    fcitx5-qt：对 Qt 程序的支持
    sudo pacman -S fcitx5-config-qt 输入法配置
    ```
    4. 配置

    欲在程序中正常启用 Fcitx5, 须设置以下环境变量，并重新登陆：
    ```
    vim ~/.pam_environment
    ---------------------------
    GTK_IM_MODULE DEFAULT=fcitx
    QT_IM_MODULE  DEFAULT=fcitx
    XMODIFIERS    DEFAULT=@im=fcitx
    INPUT_METHOD  DEFAULT=fcitx
    SDL_IM_MODULE DEFAULT=fcitx
    ```

    5. 开机启动

    - 如果您使用的桌面环境是兼容 XDG 的（例如 KDE、GNOME、Xfce、LXDE等），则 无需 此步骤。
    想要 fcitx5 开机自启，执行
    ```
    /usr/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart/
    ```

    - 在 gnome-terminal中 Ctrl + Space 不能调出输入法。

    使用 GDM 3.16 启动 GNOME，可能在某些程序中无法使用 Ctrl + Space 调出输入法。解决方法是修改GSettings配置

    终端输入
    ```
    gsettings set \
    org.gnome.settings-daemon.plugins.xsettings overrides \
    "{'Gtk/IMModule':<'fcitx'>}"
    ```

# ubuntu 的一些系统管理

- 查看磁盘空间
```
df -h
```

- 更新系统
```
apt update
apt upgrade
do-release-upgrade
```

- 基本清理
```
apt clean		# 清理apt缓存内容
apt autoremove		# 清理任何未用的依赖项
apt autoclean		# 清理不完整的软件包
apt autoremove app-name # 卸载应用
```

- 删除旧内核
```
apt remove --purge $(dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/\(.*\)-\([^0-9]\+\)/\1/")"'/d;s/^[^ ]* [^ ]* \([^ ]*\).*/\1/;/[0-9]/!d')
```

- 域名无法解析
```
# 查看DNS Server
cat /etc/resolv.conf
# 只有一个DNS Server的地址 127.0.0.53，我们可以采取如下方法给其配置DNS Server。

# vim /etc/resolv.conf 添加如下内容
nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 127.0.0.1

/etc/init.d/networking restart  # 重启网络
```

