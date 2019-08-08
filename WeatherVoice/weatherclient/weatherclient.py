from datetime import date
from os import path


import os

from playsound import playsound

from WeatherVoice.weatherclient import bd_voice_PB



def speechweather(weather):
    re = bd_voice_PB.get_bd_voice(weather)  # 通过百度API将文字转换为语音  re返回为语音mp3文件全路径

    # 播放转换后的语音 linux下
    try:
        os.system('/usr/bin/mplayer -cache-min 80 -volume 80 "%s"' % (re))
    except Exception as e:
        print('Exception', e)

    # 播放转换后的语音 windows下
    playsound('TheVoice.mp3')


if __name__ == "__main__":
    weather = "当前所选城市为深圳市,明日天气多云,夜间天气多云,室外温度33,风向无风向风,强度≤3级,后天天气多云,夜间天气多云,室外温度33,风向无风向风"
    speechweather(weather)