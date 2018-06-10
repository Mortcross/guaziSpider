# -*- coding: utf-8 -*-
# @Time    : 2018/6/10 11:23
# @Author  : Winspain
# @File    : gz_spider.py
# @Software: PyCharm

import requests
import re
import json
import time
import threading

'''买车页面请求'''


def get_carurl(start, end):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    cook = {
        "Cookie": 'uuid=293e9e9b-f00d-4ad0-aadc-20a72f482502; antipas=57866720l4063156O0UP9uO28717; ganji_uuid=7833959649036177932110; close_finance_popup=2018-06-10; Hm_lvt_936a6d5df3f3d309bda39e92da3dd52f=1528601313; Hm_lpvt_936a6d5df3f3d309bda39e92da3dd52f=1528601362; cityDomain=anqing; clueSourceCode=10103000312%2300; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_i%22%3A%22-%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22-%22%2C%22ca_campaign%22%3A%22-%22%2C%22ca_kw%22%3A%22guazi%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22ca_transid%22%3Anull%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22293e9e9b-f00d-4ad0-aadc-20a72f482502%22%2C%22sessionid%22%3A%22e08c478e-f0cf-4f60-bff3-24d392ac9562%22%7D; preTime=%7B%22last%22%3A1528603441%2C%22this%22%3A1528558172%2C%22pre%22%3A1528558172%7D; lg=1; sessionid=e08c478e-f0cf-4f60-bff3-24d392ac9562'}
    # pages = 'o1/'
    for i in range(start, end):
        urls = 'https://www.guazi.com/www/buy/0{}/'.format(i + 1)
        response = requests.get(urls, headers=headers, cookies=cook)
        responses = response.content.decode('utf-8')
        if response.status_code == 200:
            data = re.findall(r'<a title="(.*)href="(.*)#', responses)
            print(i + 1)
            with open('carname_url.txt', 'a') as f:
                for i in range(40):
                    f.writelines(str(data[i]) + '\n')
        else:
            # time.sleep(3)
            response_try = requests.get(urls, headers=headers, cookies=cook)
            responses_try = response_try.content.decode('utf-8')
            if response_try.status_code == 200:
                data = re.findall(r'<a title="(.*)href="(.*)#', responses_try)
                print(i + 1)
                with open('carname_url.txt', 'a') as f2:
                    for i in range(40):
                            f2.writelines(str(data[i]) + '\n')
            else:
                with open('fail.txt', 'a') as f3:
                    f3.writelines(urls + '\n')




# t1 = threading.Thread(target=get_carurl(1,4000),args=())
# t2 = threading.Thread(target=get_carurl(4000,7294),args=())
# threads.append(t1)
# threads.append(t2)
threads = []
# for i in range(11):
#     t = threading.Thread(target=get_carurl, args=(500 * i, 500 * (i + 1)))
#     threads.append(t)
t1 = threading.Thread(target=get_carurl, args=(0, 3000))
threads.append(t1)
t2 = threading.Thread(target=get_carurl, args=(3000, 7293))
threads.append(t2)
# t3 = threading.Thread(target=get_carurl, args=(2000, 3000))
# threads.append(t3)
# t4 = threading.Thread(target=get_carurl, args=(3000, 4000))
# threads.append(t4)
# t5 = threading.Thread(target=get_carurl, args=(4000, 5000))
# threads.append(t5)
# t6 = threading.Thread(target=get_carurl, args=(5000, 6000))
# threads.append(t6)
# t7 = threading.Thread(target=get_carurl, args=(6000, 7293))
# threads.append(t7)
if __name__ == '__main__':
    # for i in range(7294):
    #     t1 = time.time()
    #     page = 'o{}/'.format(i)
    #     get_carurl(pages=page)
    #     t = time.time()-t1
    #     print(i,t)

    try:
        t1 = time.time()
        for j in threads:
            j.setDaemon(True)
            j.start()
        for j in threads:
            j.join()
            print(time.time() - t1)
    except TimeoutError:
        print('[WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应，连接尝试失败。')