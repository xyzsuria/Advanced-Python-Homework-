# 作业要求：
# 在浏览器中打开网址https://www.beijing2022.cn/cn/presscentre/newslist.htm
# 循环将网页中新闻列表的新闻标题用jquery的方法抽取出来

from pyquery import PyQuery as pq
import requests
import os
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def Beautiful(browser):
    print("等待网页响应...")
    # 需要等一下，直到页面加载完成
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, "listZone")))
    print("正在获取下一页网页数据...")
    soup = BeautifulSoup(browser.page_source, "lxml")
    news = soup.find_all('span', class_='news_dp')
    # print(news)
    for i in news:
        # print(type(i)) <class 'bs4.element.Tag'>
        print(i.get_text(), i.find('a')['href'])


def Pages(mainurl, browser):
    browser.get(mainurl)
    print("等待网页响应...")
    # 需要等一下，直到页面加载完成
    Beautiful(browser)
    try:
        while browser.find_element_by_link_text("下一页"):
            browser.find_element_by_link_text("下一页").click()
            Beautiful(browser)
    except:
        pass


def PaQuTitle(url):
    r = requests.get(url)
    r.encoding = 'bg2312'
    html = r.text
    doc = pq(html)
    print(doc)

# 这个方法不行
def PaQuPage(mainurl):
    requests.packages.urllib3.disable_warnings()
    # 解决验证报错 显示
    # InsecureRequestWarning: Unverified HTTPS request is being made.
    # Adding certificate verification is strongly advised.
    r = requests.get(mainurl, timeout=30, verify=False)
    r.encoding ='gbk'
    # 虽然网页title显示为 charset = bg2312，但用这一编码照样乱码
    html = r.text
    doc = pq(html)
    # for i in doc('li').items():
    #     print(i('a').attr.href)
    print(doc('#listZone'))
    # 输出结果是：
    # < div
    # id = "listZone" > < ul > &  # 13;
    # &  # 13;
    # < / ul > < / div > &  # 13; （真是令人窒息）


if __name__ == '__main__':
    mainurl = 'https://www.beijing2022.cn/cn/presscentre/newslist.htm'
    # PaQuPage(mainurl)
    # Beautiful(mainurl)
    browser = webdriver.Chrome()
    # browser = webdriver.PhantomJS()
    print("正在打开网页...")
    Pages(mainurl, browser)
    browser.close()


