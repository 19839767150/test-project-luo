import re
import json
import os

import requests

"""
1.首先要爬取到对方网站下面查看具体情况
2.抓取要求的内容进行正则表达式筛选
3.然后根据文章的要求将上面爬取的内容写入到json文件里面
4.把图片以jpg的后缀来保存

"""
s = int(input('请输入你要爬取那一页?(1-10页)'))
print(type(s))

l = 'bid=oXNnL6nci0Q; _pk_id.100001.3ac3=4b4ed85eae97e1b2.1781528441.; _pk_ses.100001.3ac3=1; ap_v=0,6.0; __utma=30149280.1876794759.1781528441.1781528441.1781528441.1; __utmc=30149280; __utmz=30149280.1781528441.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt_douban=1; __utma=81379588.670166244.1781528441.1781528441.1781528441.1; __utmc=81379588; __utmz=81379588.1781528441.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; __utmb=30149280.8.10.1781528441; __utmb=81379588.8.10.1781528441'

cookies = {l.split('=')[0]:l.split("=")[-1] for l in l.split(";")}


headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',

}

url = f'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={s}&updated_at='
response = requests.get(url,headers=headers,cookies=cookies)
# print(response.text)
html = response.text



result = re.findall(r'<div\sclass="media__img">.*?<a\shref=".*?"><img\sclass="subject-cover"\salign="left"\ssrc="(.*?)"/></a>.*?</div>.*?<div\sclass="media__body">.*?<h2\sclass="clearfix">.*?<a\sclass="fleft"\shref="(.*?)">(.*?)</a>.*?</h2>.*?<p\sclass="subject-abstract\scolor-gray">(.*?)</p>',html,re.S)
print(len(result))
n=1
for i in result:


    # print(f"第{n}个",i)
    photo = i[0]
    title_link = i[1]
    title = i[2]
    auth_details = i[3].strip()

    # 保存数据
    # 将文字信息保存在普通文本中
    with open('data.text', 'a', encoding='utf-8') as f:
        f.write(title + "\n")
        f.write(title_link + "\n")
        f.write(auth_details + "\n")
        f.write(photo + "\n")
    img_data = requests.get(photo,headers=headers).content
    if  not os.path.exists("imgdata"):
        os.mkdir("imgdata")
    with open("imgdata/{}.jpg".format(title),'wb') as f:
        f.write(img_data)

