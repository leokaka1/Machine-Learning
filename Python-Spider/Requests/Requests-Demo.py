import requests

URL = "http://www.baidu.com"

# 用一个response来承接返回的数据
response = requests.get(URL)

# response.content返回内容

'''
 - response.text
   - 类型：str
   - 解码类型： requests模块自动根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
 - response.content
   - 类型：bytes
   - 解码类型： 没有指定
'''
# print(response.content)
# print(response.text)

# 设置编码
# print(response.content.decode())


# 打印响应内容
# print(response.text)
# print(response.content.decode())       # 注意这里！
# print(response.url)              # 打印响应的url
# print(response.status_code)          # 打印响应的状态码
# print(response.request.headers)        # 打印响应对象的请求头
# print(response.headers)            # 打印响应头
# print(response.request._cookies)      # 打印请求携带的cookies
# print(response.cookies)            # 打印响应中携带的cookies