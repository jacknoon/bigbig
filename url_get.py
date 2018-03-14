# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 10:19:27 2018

@author: ghwin
"""
import os
import urllib
#from lxml import etree
from urllib import request
from bs4 import BeautifulSoup
import re

#keyword = "love"
maxpage=1
#keyword  = input("请输入关键词:")
#maxpage_input  = input("请输入下载页数:")

def mkdir(path):

    # 判断路径是否存在
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print (path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print (path + ' 目录已存在')
        return False



def url_get(page):  #获取url
    url = 'http://www.169ku.com/xingganmeinv/list_1_1.html'

    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0'
    header = {'User-Agent': user_agent}
    target_req = request.Request(url=url, headers=header)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    soup = BeautifulSoup(target_html, 'html.parser')
    for data in soup.find_all("a", {"class": "pic"}):
        title = data.text
        html = data['href']
        print(title)
        #with open('a.txt','a') as f:
        #   f.write(title +'\n')
        get_img(html,title)




#去图片总页数和网址
def get_img(img_url,title):


    img_url1=img_url

    # http://www.169ku.com/xingganmeinv/2018/0312/40883_2.html
    # http://www.169ku.com/xingganmeinv/2018/0312/40883_13.html
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0'
    header = {'User-Agent': user_agent}
    target_req = request.Request(url=img_url1, headers=header)
    target_response = request.urlopen(target_req)
    target_html = target_response.read().decode('gbk','ignore')
    soup = BeautifulSoup(target_html, 'html.parser')

    for img_pages in soup.find_all("div", {"class": "dede_pages"}):
        a = img_pages.li.a.string
        totalCount = re.sub("\D", "", a)

    for data in soup.find_all("p", {"align": "center"}):
        img_url = data.img['src']
        with open('urltxt/'+title +'.txt', 'a') as f:
            f.write(img_url+'\n')
        print(img_url)
    get_img2(img_url1,totalCount,title)

def get_img2(url1,count,title):
    url_base = url1.split(".html")[0]


    for m in range(2, int(count) + 1):
        img_url2 = url_base + '_' + str(m) + '.html'
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:58.0) Gecko/20100101 Firefox/58.0'
        header = {'User-Agent': user_agent}
        target_req = request.Request(url=img_url2, headers=header)
        target_response = request.urlopen(target_req)
        target_html = target_response.read().decode('gbk', 'ignore')
        soup = BeautifulSoup(target_html, 'html.parser')

        for data in soup.find_all("p", {"align": "center"}):
            img_url = data.img['src']
            with open('urltxt/'+title +'.txt', 'a') as f:
                f.write(img_url+'\n')
            print(img_url)



    print("下载完成")





def main():
    """
    遍历每一页
    """
    #maxpage = int(maxpage_input)
    #os.makedirs(keyword)
    mkdir('urltxt')
    mkdir('pic')
    for i in range(1, maxpage + 1):
        url_get(i)
    print("爬取结束")


if __name__ == '__main__':
    main()

