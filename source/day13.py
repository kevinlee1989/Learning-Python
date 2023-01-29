"""
    Day13 -  web Crawling
    Version : 1.0
    Created : 2022.06.16
    Updated : 2022.06.16
    Author : J.W.Lee
"""
import requests
from bs4 import BeautifulSoup

url = 'http://www.naver.com'
response = requests.get(url)
print('웹서버의 응답시간 : ', response.elapsed)
print('웹서버의 상태 :', response.status_code)
print(response.text)

url = 'https://search.naver.com/search.naver'
param = {'where' : 'nexearch', 'sm' : 'top_hty', 'fbm' : '1', 'ie' : 'utf8', 'query' : '2022worldcup'}
response = requests.get(url, params = param)
print(response.text)

url = 'http://www.samsungfire.com'
response = requests.get(url)
response.encoding = None # 한글이 깨질 경우 사용
print(response.text)

url = 'http://www.google.com'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

#find method
list1 = soup.find('div')
print(list1)
list2 = soup.find('div').text
print(list2)
list3 = soup.find('div').get('id')
print(list3)

print()

#find_all method
list4 = soup.find_all('div')
print(list4) # 구글 크롬의 div 갯수

# naver 영화 사이트 '범죄도시2'
url = 'https://movie.naver.com/movie/bi/mi/basic.naver'
param = {'code' : '192608'}
response = requests.get(url, params = param)
html = response.text
soup = BeautifulSoup(html, 'html.parser')


# using find_all to get one-line review
list = soup.find_all('div', class_= 'score_reple')
for div in list:
    print(div.find('p').text.strip())

print()

# using select to get one-line review
list1 = soup.select('div.score_reple > p')
for div in list1:
    print(div.text.strip())

# 명대사 가져오기(homework)
print('명대사 가져오기')
list2 = soup.select('div.tx_tob > strong')
for div in list2:
    print(div.text.strip())

# print('API 방식으로 데이터 취득')
# for i in range(1,11):
#     url =

