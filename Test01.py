import requests

url = "https://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status  # 返回值不是200时会返回错误类型
    r.encoding = r.apparent_encoding
    print(r.text[0:1000])
except:
    print("爬取失败")