# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 21:33:11 2023

@author: Stone
"""
#%%
import pandas as pd

#%% 一个翻译的函数
import json
import requests
import re

def translator(str):
    """
    input : str 需要翻译的字符串
    output：translation 翻译后的字符串
    """
    # API
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数， i为要翻译的内容
    key = {
        'type': "AUTO",
        'i': str,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 通过 json.loads 把返回的结果加载成 json 格式
        result = json.loads(response.text)
#         print ("输入的词为：%s" % result['translateResult'][0][0]['src'])
#         print ("翻译结果为：%s" % result['translateResult'][0][0]['tgt'])
        translation = result['translateResult'][0][0]['tgt']
        return translation
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None

#%%
filename=r'E:\code\python\data_analysis\20230313-翻译\原始文件\翻译.xlsx'
putname=r'E:\code\python\data_analysis\20230313-翻译\原始文件\翻译结果.xlsx'
data=pd.read_excel(filename)
data['中文标题']=data['英文标题']
for i in range (len(data)):
    data['中文标题'][i]=translator(data['英文标题'][i])
data.to_excel(putname,encoding='gbk',index=False)