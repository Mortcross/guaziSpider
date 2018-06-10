# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 14:44
# @Author  : Winspain
# @File    : test.py
# @Software: PyCharm
import re
import os
import requests
def get_url():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    cook = {
        "Cookie": 'uuid=293e9e9b-f00d-4ad0-aadc-20a72f482502; antipas=57866720l4063156O0UP9uO28717; ganji_uuid=7833959649036177932110; close_finance_popup=2018-06-10; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1528601313; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1528601362; cityDomain=anqing; clueSourceCode=10103000312%2300; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22guazi%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3Anull%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22293e9e9b-f00d-4ad0-aadc-20a72f482502%22%2C%22sessionid%22%3A%22e08c478e-f0cf-4f60-bff3-24d392ac9562%22%7D; preTime=%7B%22last%22%3A1528603441%2C%22this%22%3A1528558172%2C%22pre%22%3A1528558172%7D; lg=1; sessionid=e08c478e-f0cf-4f60-bff3-24d392ac9562'}

    with open('carname_url.txt','r') as f:
        # print(len(f.readlines()))
        for i in range(4,5):
            readTxt = f.readline().split() #["('路特斯Exige", '2015款', '3.5T', 'S', '硬顶版"']
            cardata = readTxt[:-2]
            urldata = str(readTxt[-1])[1:-2]
            ss = ''
            carname = str(i+1) + '.' + ss.join(cardata)[2:-1]
            # os.makedirs(carname)
            url = 'https://www.guazi.com'+urldata
            response = requests.get(url, headers=headers, cookies=cook)
            responses = response.content.decode('utf-8')
            # print(responses)
            if response.status_code == 200:
                # data = re.findall(r'图模(.*)<ul class="fourtab threetab">', responses, re.S)
                # # print(data)
                # data = re.findall(r'<img data-src="(.*)\"',str(data).replace('\\r','').replace('\\n','').replace('\\',''))
                # data = re.findall(r'(.*),',str(str(data).split()))
                # print(data[0])
                data = re.findall(r'<img data-src=(.*)', responses)
                print(data[30:37])


if __name__ == '__main__':
    get_url()
