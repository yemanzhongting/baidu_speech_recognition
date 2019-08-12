# -*- coding: UTF-8 -*-
__author__ = 'zy'
__time__ = '2019/8/4 11:41'
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '16693047'
API_KEY = 'XRbLPy0dBN1dSrhgxGbQRoGy'
SECRET_KEY = 'xjv1QqqMgB7dI7hc2h1EoOTY2YPoFbzY'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()



# 参数	类型	描述	是否必须
# speech	Buffer	建立包含语音内容的Buffer对象, 语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写	是
# format	String	语音文件的格式，pcm 或者 wav 或者 amr。不区分大小写。推荐pcm文件	是
# rate	int	采样率，16000，固定值	是
# cuid	String	用户唯一标识，用来区分用户，填写机器 MAC 地址或 IMEI 码，长度为60以内	否
# dev_pid	Int	不填写lan参数生效，都不填写，默认1537（普通话 输入法模型），dev_pid参数见本节开头的表格


# 识别本地文件
print(
    client.asr(get_file_content('16k-23850.amr'), 'amr', 16000, {
    'dev_pid': 1536,
    })
      )

# dev_pid 返回参数列表
#
# dev_pid	语言	模型	是否有标点	备注
# 1536	普通话(支持简单的英文识别)	搜索模型	无标点	支持自定义词库
# 1537	普通话(纯中文识别)	输入法模型	有标点	支持自定义词库
# 1737	英语		有标点	不支持自定义词库
# 1637	粤语		有标点	不支持自定义词库
# 1837	四川话		有标点	不支持自定义词库
# 1936	普通话远场	远场模型	有标点	不支持

#
# pydub是python的高级一个音频处理库，可以让你以一种不那么蠢的方法处理音频。---开发者原话
#
# https: // github.com / jiaaro / pydub
# 附上开发者的github地址
#
# 安装：
#
# pip
# install
# pydub
# 如果在pycharm中也可以这样安装：
#
# setting - ---Project
# Interpreter - ---右边绿色 + 号
#
# Python
# pydub库对mp3与wav格式进行互转
#
# 点一下install
# package
#
# 依赖安装：
#
# 作者在github
# 上说，依赖可以安装libav or ffmpeg
# 关于这两个东西的爱恨情仇可以自行百度
#
# 我们安装其一就行
#
# Mac(using
# homebrew):
#
# # libav
# brew
# install
# libav - -
# with-libvorbis - -with-sdl --with-theora
#
# #### OR #####
#
# # ffmpeg
# brew
# install
# ffmpeg - -
# with-libvorbis - -with-sdl2 --with-theora
# Linux(using
# aptitude):
#
# # libav
# apt - get
# install
# libav - tools
# libavcodec - extra - 53
#
# #### OR #####
#
# # ffmpeg
# apt - get
# install
# ffmpeg
# libavcodec - extra - 53
# 上面是MAC和Linux
# 的安装方法，由于我开发环境用的是windows
# 系统，对libac支持不大好，我采用了ffmpeg
#
# 先去ffmpeg官网下载
#
# https: // ffmpeg.zeranoe.com / builds /
# Linking
# 选择Static ，好了之后解压缩，随便解压到哪，我们配一下环境变量
#
# Python
# pydub库对mp3与wav格式进行互转
#
# 把刚刚解压的路径配到Path里面，重开IDE
#
# 注意点：开IDE时候需要选择用管理员权限运行
#
# 代码：
#
# from pydub import AudioSegment
#
#
# def trans_mp3_to_wav(filepath):
#     song = AudioSegment.from_mp3(filepath)
#     song.export("now.wav", format="wav")
#
#
# 简单封装了一个方法，把mp3路径扔进去，就能输出一个now.wav文件。
#
# 以上这篇Python使用pydub库对mp3与wav格式进行互转的方法就是小编分享给大家的全部内容了，希望能给大家一个参考，也希望大家多多支持脚本之家。