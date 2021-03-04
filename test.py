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

print(block_1)


# try:
#     for i in range(20):
#         one_team = block_1.find_all('span')[count].text
#         two_team = block_1.find_all('span')[count + 1].text
#         three_team = block_1.find_all('span')[count + 2].text
#         result1 = " " + ' ' + one_team + '-' + two_team +'-'+three_team
#         count += 4
#         print(result1)
# except:
#     print()

# else:
#     print('nice')
