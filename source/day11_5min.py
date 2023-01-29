"""
    Day11 5min challenge
    Kevin Lee
    2022.06.09
"""
"""
    1. 문자열을 2개 입력받는다.
    2. 공통으로 존재하는 문자를 찾는다.
    3. '첫 번째 문자열의 길이 : ***, 두 번째 문자열의 길이 : ***'
       '공통으로 존재하는 문자 개수 : ***'를 출력한다.
    4. 첫 번째 문자열과 두 번째 문자열을 출력하되
       공통된 문자만 색을 입혀 출력한다.
"""
from colors import*

# 1. 문자열을 2개 입력받는다.

str1 = input('첫번째 문자열을 입력하세요 : ')
str2 = input('두번째 문자열을 입력하세요 : ')


str1_list = []
str2_list = []

for c in str1:
    str1_list.append(c)
for c in str2:
    str2_list.append(c)

# Set의 성질을 이용하여 중복된 글자를 찾아낸다.

str1_set = set(str1_list) # set은 중복을 허락하지않기때문에 중복은 이미 날라갔다
str2_set = set(str2_list)
str3_set = str1_set.intersection(str2_set)
str3_list = list(str3_set)
if ' ' in str3_list:
    str3_list.remove(' ')

# 3. 출력
print('첫 번째 문자열의 길이 : {}, 두 번째 문자열의 길이 : {}'.format(len(str1),len(str2)))
print('공통으로 존재하는 문자 개수 : {} '.format(len(str3_list)))


for c in str1:
    if c in str3_list:
        print(RED + c + END, end = '')
    else:
        print(c, end='')
print()
for c in str2:
    if c in str3_list:
        print(RED + c + END, end = '')
    else:
        print(c, end='')

