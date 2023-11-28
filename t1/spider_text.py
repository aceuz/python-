import requests
response = requests.get("http://books.toscrape.com/")
if response.status_code >=200 and response.status_code<400:
    print(response.text)
elif response.status_code>=400 and response.status_code<500:
    print("false")
elif response.status_code>=500:
    print("flase")
