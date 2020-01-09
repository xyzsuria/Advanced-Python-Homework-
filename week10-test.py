# 作业要求：
# 使用selenium webdriver调用chrome,
# 访问www.baidu.com，并用程序控制在检索框输入自己的姓名，
# 抽取搜索结果列表的内容和分页的链接列表。
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# 因为这个网页跳转太快了


def Search(name):
    driver = webdriver.Chrome()
    print("正在打开网页")
    url = 'https://www.baidu.com/'
    driver.get(url)
    driver.find_element_by_id("kw").send_keys(name)
    driver.find_element_by_id("su").click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, "content_left")))
    soup = BeautifulSoup(driver.page_source, 'lxml')
    # content = soup.find('div', id_='content_left')
    titles = soup.find_all('div', class_='result')
    # print(titles)
    pages = soup.find('div', id_='page')
    for i in titles:
        print(i.find('a').get_text(), i.find('a')['href'])
    # 这么多人跟我同名，实在是想换一个独一无二的名字，哈哈哈。


if __name__ == '__main__':
    name = input("请输入你想搜索的名字：")
    Search(name)






