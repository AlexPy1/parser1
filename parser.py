import requests
from bs4 import BeautifulSoup
import fake_useragent


user= fake_useragent.UserAgent().random
header ={'user-agent': user}

link = "https://soccer365.ru/online/"
response = requests.get(link,headers=header).text
soup = BeautifulSoup(response, 'lxml')
block_1 = soup.find('div', id='cmp16')
def today(block):
    count=1
    liga=block.find_all('span')[count-1].text
    print(liga)
    print()
    try:
        for i in range(20):
            time = block.find_all('span')[count].text
            one_team = block.find_all('span')[count + 1].text
            two_team = block.find_all('span')[count + 2].text
            result1 = time + ' ' + one_team + '-' + two_team
            count += 5
            print(result1)
    except:
        print()
today(block=block_1)


# count=1
block_2 = soup.find('div', id='cmp17')
today(block=block_2)
block_3 = soup.find('div', id='cmp723')
today(block=block_3)
# liga3=block_3.find_all('span')[count - 1].text
# print(liga3)
# print()
# try:
#     for i in range(20):
#         time = block_3.find_all('span')[count].text
#         one_team = block_3.find_all('span')[count + 1].text
#         two_team = block_3.find_all('span')[count + 2].text
#         result1 = time + ' ' + one_team + '-' + two_team
#         count += 5
#         print(result1)
# except:
#     print()
#
#
# count=1
# block_4 = soup.find('div', id='gm1521614')
# liga4=block_4.find_all('span')[count - 1].text
# print(liga4)
# print()
# try:
#     for i in range(20):
#         time = block_4.find_all('span')[count].text
#         one_team = block_4.find_all('span')[count + 1].text
#         two_team = block_4.find_all('span')[count + 2].text
#         result1 = time + ' ' + one_team + '-' + two_team
#         count += 5
#         print(result1)
# except:
#     print()

