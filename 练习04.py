import re
import json
import requests
import os
import openpyxl
from openpyxl import workbook
"""
1.定义爬取范围的关键是要分析原网址的规律
2.然后最好带上饼干，还有请求头
3.然后用正则提取出电影的信息（电影的名称，评分，还有经典台词），中途使用判断语句来过滤掉评分小于9.5的电影
4.最后利用openpyxl库来对信息进行Excel表格的存储



"""



n = int(input("用户输出自己想要浏览的页码数"))*25-25

url = f"https://movie.douban.com/top250?start={n}&filter="
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
temp = 'bid=aqzRYzRQCEE; viewed="37292083"; _vwo_uuid_v2=DDBE0EF031B7E6288E13B34C38FFC5362|8e4b4d3a8e4d1db3eba6b197318d8afa; ll="118251"; _pk_id.100001.4cf6=4b0fab36611bb202.1754790670.; __yadk_uid=9z8YZO37qKQ4FdMBpNOPfT57h0jANepw; _pk_ses.100001.4cf6=1; __utma=30149280.1991891077.1754224048.1754790670.1782830429.3; __utmb=30149280.0.10.1782830429; __utmc=30149280; __utmz=30149280.1782830429.3.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.298029130.1754790670.1754790670.1782830429.2; __utmb=223695111.0.10.1782830429; __utmc=223695111; __utmz=223695111.1782830429.2.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ap_v=0,6.0'
cookie_list = temp.split(";")
cookies = {}
for cookie in cookie_list:
    cookies[cookie.split("=")[0]] =cookie.split("=")[1]

response = requests.get(url,headers=headers,cookies=cookies)
# print(response.text)
html = response.text
result = re.findall(r' <span\sclass="title">(.*?)</span>.*?<span\sclass="rating_num"\sproperty="v:average">(.*?)</span>.*?<p\sclass="quote">.*?<span>(.*?)</span>.*?</p>',html,re.S)
a = [i for i in result if float(i[1])>9.4]
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "电影评分数据"
headers = ["电影名称",'评分','经典台词']
ws.append(headers)
for item in a:
    ws.append(item)
wb.save("电影数据.xlsx")
print("数据成功录用！！")

