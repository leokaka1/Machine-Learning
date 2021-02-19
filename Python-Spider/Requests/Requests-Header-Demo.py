import requests

url = "https://www.baidu.com"

response = requests.get(url)

# 打印响应对应的请求头信息
print(response.headers)


headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.68"
}

response = requests.get(url,headers = headers)

print(response.content)

# 再次打印请求头对比
print(response.headers)