import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
import wget
# for i in range(10):
#     url = f'https://weakpass.com/wordlist/medium?page={i}'
#     response = requests.get(url)
#     bs = BeautifulSoup(response.text, 'html.parser')
#     data = bs.find_all('footer', class_='card-footer')
#     for i in data:
#         print(i.get('href'))

c = 1
d = ''

for i in range(c):
    url = f'https://weakpass.com/wordlist/tiny?page={i+1}'
    print(f'Прогресс: {i+1} страниц', end='\r')
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    data = bs.find_all('a', class_="card-footer-item is-primary is-light")
    # print(data)
    for i in data:
        s = i.get('href')
        if "torrent" not in s: 
            # print(i.get('href'))
            d += i.get('href')+'\n'
    
with open('Lists.txt', 'w') as file:
    file.write(d)
print("Процесс завершен !!!")

with open('Lists.txt', 'r') as file:
    s2 = file.readlines()
print(s2[0])


url = 'https://download.weakpass.com/wordlists/1859/Top304Thousand-probable-v2.txt.gz'
response = requests.get(url)
 
with open('Top304Thousand-probable-v2.txt.gz', 'wb') as file:
    file.write(response.content)
