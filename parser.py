import requests
from bs4 import BeautifulSoup



link = "https://soccer365.ru/online/"
response = requests.get(link).text
soup = BeautifulSoup(response,'lxml')
block = soup.find('div', id = 'cmp12')

one_team= block.find_all('span')[1].text
two_team= block.find_all('span')[2].text
three_team= block.find('title')
test = block.text
test2=test.split()
print(test2[3])
