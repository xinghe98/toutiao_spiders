import json
import requests
from urllib.parse import urlencode
import time
from selenium import webdriver
import re

class TouTiao(object):
    """
    工厂类
    文章获取方式与存储方式使用此类
    """

    def __init__(self):
        self.path = './chromedriver.exe'
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36"
        }
        self.timestamp = int(time.time())

    def article_info(self, offset, keyword):
        """
        :param offset:
        :param keyword:
        :return: 文章详细信息
        """
        params={
                    "aid": 24,
                    "app_name": "web_search",
                    "offset": offset,
                    "format": "json",
                    "keyword": keyword,
                     "autoload": "true",
                    "count": 20,
                    "en_qc": 1,
                    "cur_tab": 1,
                    "from": "search_tab",
                    "pd": "synthesis",
                    "timestamp":self.timestamp
      }
        url = 'https://www.toutiao.com/api/search/content/?'+urlencode(params)
        res = requests.get(url,headers = self.headers)
        data = json.loads(res.text)
        data = data['data']
        return data

    def decode(self,match):
        """将Unicode转为字符串"""
        return (bytes(match.group(), encoding='utf-8').decode('unicode-escape'))

    def validateTitle(title):
        """去除tiitle中非法字符"""
        rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
        new_title = re.sub(rstr, "_", title)  # 替换为下划线
        return new_title

    def download_article(self,url, title):
        br = webdriver.Chrome(executable_path=self.path)
        br.get(url)
        str = br.page_source
        br.close()
        print(url)
        data = re.search(r'content: \'&quot;(.*?)&quot;\'\.slice\(6, -6\),', str)
        try:
            data = re.sub(r'\\u00..', self.decode, data.group(1))
            data = data.replace('&#x3D;', '=')
            data = data.replace('\\&quot;', '"')
        except AttributeError:
            return None
        with open('{}.html'.format(title), 'w', encoding='utf-8') as f:
            f.write(data)
        return data
