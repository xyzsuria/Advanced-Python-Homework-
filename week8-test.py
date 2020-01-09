import requests
设置代理
proxies = {
  "http": "http://10.10.1.10:3128",
  "https": "http://10.10.1.10:1080",
}
requests.get("http://example.org", proxies=proxies)

# 修改请求头
url = 'https://www.baidu.com/s?wd=python'
headers = {
        'Content-Type': 'text/html;charset=utf-8',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }
r = requests.get(url,headers=headers)