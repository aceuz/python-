import requests
headers = {
    "user-Agent":
    #伪装成浏览器
}
response = requests.get("https://movie.douban.com/top250")
print(response.status_code)