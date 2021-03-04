import requests
from bs4 import BeautifulSoup
import fake_useragent


user= fake_useragent.UserAgent().random
header ={'user-agent': user}

link = "https://soccer365.ru/online/"
response = requests.get(link,headers=header).text
soup = BeautifulSoup(response, 'lxml')
block_1 = soup.find('div', id='cmp12')

count=1
liga=block_1.find_all('span')[count-1].text
print(liga)
print()
try:
    for i in range(20):
        time = block_1.find_all('span')[count].text
        one_team = block_1.find_all('span')[count + 1].text
        two_team = block_1.find_all('span')[count + 2].text
        result1 = time + ' ' + one_team + '-' + two_team
        count += 5
        print(result1)
except:
    print()


count=1
block_2 = soup.find('div', id='cmp15')
liga2=block_2.find_all('span')[count - 1].text
print(liga2)
print()
try:
    for i in range(20):
        time = block_2.find_all('span')[count].text
        one_team = block_2.find_all('span')[count + 1].text
        two_team = block_2.find_all('span')[count + 2].text
        result1 = time + ' ' + one_team + '-' + two_team
        count += 5
        print(result1)
except:
    print()


count=1
block_3 = soup.find('div', id='cmp723')
liga3=block_3.find_all('span')[count - 1].text
print(liga3)
print()
try:
    for i in range(20):
        time = block_3.find_all('span')[count].text
        one_team = block_3.find_all('span')[count + 1].text
        two_team = block_3.find_all('span')[count + 2].text
        result1 = time + ' ' + one_team + '-' + two_team
        count += 5
        print(result1)
except:
    print()


count=1
block_4 = soup.find('div', id='gm1521614')
liga4=block_4.find_all('span')[count - 1].text
print(liga4)
print()
try:
    for i in range(20):
        time = block_4.find_all('span')[count].text
        one_team = block_4.find_all('span')[count + 1].text
        two_team = block_4.find_all('span')[count + 2].text
        result1 = time + ' ' + one_team + '-' + two_team
        count += 5
        print(result1)
except:
    print()

