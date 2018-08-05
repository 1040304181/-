# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 17:28:28 2018

@author: jukuo
"""
#-*- coding: utf-8 -*-                    
from aip import AipSpeech
import make_wav

""" 你的 APPID AK SK """
APP_ID = '***'
API_KEY = '***'
SECRET_KEY = '** '

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
r = GenAudio()
r.num_samples = 2000    #pyaudio内置缓冲大小
r.sampling_rate = 16000  #取样频率
r.level = 1500          #声音保存的阈值
r.count_num = 20        #count_num个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
r.save_length = 8       #声音记录的最小长度：save_length * num_samples 个取样
r.time_count = 10        #录音时间，单位s
r.read_audio()
r.save_wav("./test.wav")
result=client.asr(get_file_content('test.wav'), 'pcm', 16000, {
    'dev_pid': 1536,
})
print(result['result'][0])