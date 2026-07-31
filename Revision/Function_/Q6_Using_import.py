import requests

a=requests.get("https://api.github.com/")
print(a.json())