# 配置 git

- 配置ssh公钥
```
    ssh-keygen -o
```

- 配置 git .gitconfig
```
    [alias]
        co = checkout
        ci = commit
        br = branch
        st = status
    [user]
        name = Your Name
        email = your@email.com
```

- 更新 win git
```
git 2.16.1 以后
git update-git-for-windows
```

- git 设置和取消代理
```
git config --global https.proxy http://127.0.0.1:1080

git config --global https.proxy https://127.0.0.1:1080

git config --global http.proxy 'socks5://127.0.0.1:1080'

git config --global https.proxy 'socks5://127.0.0.1:1080'

git config --global --unset http.proxy

git config --global --unset https.proxy
```