import requests
from settings import LiveUrl, BaseUrl


print(requests.get(BaseUrl, verify=False).content)