import requests
from lxml import etree

def get_one_chapter(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}
    #url = "http://www.biquge.se/24901/41015693.html"
    response = requests.get(url, headers=headers)
    res_xpath = etree.HTML(response.text)
    title1 = res_xpath.xpath('//h1/text()')[0]
    title = title1.strip()  #去掉文本前后空格
    content = res_xpath.xpath("//div[@id='content']/text()")
    with open(file="绝世战神.txt", mode='a+', encoding='UTF-8') as f:
        f.write("\n\n")
        f.write(title)
        f.write("\n")
        for line in content:
            line = line.strip()  #去掉文本前后空格
            f.write(line)
        print(title,"下载完成")


response = requests.get('http://www.biquge.se/24901/')
res_xpath = etree.HTML(response.text)
urls = res_xpath.xpath("//*[@id='list']/dl/dd/a/@href")
for i,url in enumerate(urls):
    if i>159:
        get_one_chapter("http://www.biquge.se"+url)
        print("http://www.biquge.se"+url)
    else:
        pass



