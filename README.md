<img src="./seele.png">

# 坐标系转换

- 从笛卡尔坐标转换到屏幕坐标的基本算法是
```
screenX = cartX + screen_width / 2
screenY = screen_height / 2 - cartY
```
-  但正如你提到的，笛卡尔空间是无限的，而你的屏幕空间不是这可以通过改变屏幕空间和笛卡尔空间之间的分辨率来轻松解决上述算法使笛卡尔空间中的1个单位=屏幕空间中的1个单位/像素。如果你允许其他比率，你可以“放大”或在你的屏幕空间，以涵盖所有笛卡尔空间所需。这会将上述算法更改为
```
screenX = zoom_factor * cartX + screen_width / 2
screenY = screen_height / 2 - zoom_factor * cartY
```

- 现在您可以通过修改缩放因子来处理负（或过大）屏幕X和屏幕Y，直到所有笛卡尔坐标都适合屏幕。也可以允许平移坐标空间，也就是说，允许笛卡尔空间的中心偏离屏幕的中心。这也有助于使缩放因子尽可能保持紧密，但也有助于拟合在笛卡尔空间原点周围分布不均匀的数据。这会将算法更改为
```
screenX = zoom_factor * cartX + screen_width / 2 + offsetX
screenY = screen_height / 2 - zoom_factor * cartY + offsetY
```

# ffmpeg 加速播放
```
ffmpeg -i input.mkv -filter:v "setpts=0.5*PTS" output.mkv
ffmpeg -i input.mkv -r 16 -filter:v "setpts=0.25*PTS" output.mkv
ffmpeg -i input.mkv -filter:v "setpts=2.0*PTS" output.mkv
2倍速 4倍速 0.5倍速
n(倍速)/10
```

