# coding:utf-8
# 解析器
from bs4 import BeautifulSoup
import requests
import bs4

# 1.提取网页数据
def getHtmlText(url):
    try:
        data = requests.get(url, timeout=30)
        # # 查看状态码
        print(data.status_code)
        # 自定义抛出异常
        data.raise_for_status()
        data.encoding = data.apparent_encoding
        return data.text
    except:
        print('获取失败')


# 2.将网页数据放到合适的数据结构
def html_list(list_, html):
    Soup = BeautifulSoup(html, 'html.parser')
    for i in Soup.find('tbody').children:
        # 判断类型
        if isinstance(i, bs4.element.Tag):
            tds = i('td')
            list_.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])



# 3.利用数据结构展示输出
def print_list(show_):
    tplt = "{0:^10}\t{1:^10}\t{2:^10}\t{3:^5}"
    print(tplt.format("排名", "学校名称", "省份", "总分", chr(12288)))
    for i in range(len(show_)):
        x = show_[i]
        print(tplt.format(x[0], x[1], x[2], x[3]), chr(12288))


def main():
    list_ = []
    url = 'http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'

    html_list(list_=list_, html=getHtmlText(url))

    print_list(list_)


if __name__ == '__main__':
    main()
