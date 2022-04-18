import requests
from bs4 import BeautifulSoup as bs

url = 'https://dantri.com.vn/the-thao.htm'

res = requests.get(url)

soup = bs(res.content, 'html.parser')

titles = soup.find_all('a', {'title' : True})

for title in titles:
    if(title['title'] == 'Trang tiếp'):
        break
    print(title.text)
    
