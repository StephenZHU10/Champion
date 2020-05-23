本脚本只适用于FIFA ONLINE 4球王分段， 配合ifuzhu等软件达成自动比赛，并在超过需要的分数时停止自动比赛。
本脚本需要的python库有tesseract (可通过pip install pytesseract自行下载)，opencv2 (可通过pip install opencv-python自行下载)，
PIL（可通过pip install --upgrade pip 或 pip install --upgrade Pillow自行下载）以及tesseract executable (可通过
https://github.com/UB-Mannheim/tesseract/wiki自行下载并安装)。

启动python命令行时（或其他命令行，如jupyter notebook），需以管理员身份运行，否则设置前台/获取句柄/发送指令时将会有“访问被拒绝”报错。
同时需要在运行前打开ifuzhu等辅助（ifuzhu默认启动热键为F9,并把比赛场数设置为1场），以及把游戏分辨率调至1280*720，窗口移动到左上角。
启动运行后每隔15分钟会唤醒游戏到前台判断分数（基本上15分钟内比赛会结束），建议在非工作，娱乐时使用。

有疑问和建议请在群内@延迟
