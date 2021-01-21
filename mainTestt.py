import requests
import json

url='http://wwww.baidu.com'
data={
    'name':'张三',
    'age':23
}
response=requests.get(url,params=data)
requests.post
print(response.status_code)
print(response.text)
print(response.url)