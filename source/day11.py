"""
    Day11 -  string
    Version : 1.0
    Created : 2022.06.09
    Updated : 2022.06.09
    Author : J.W.Lee
"""

from myutils import*
cprintTitle('Day11 - String')

s1 = 'my name is Kevin'
print(s1.find('name')) # index 3에 위치 하기 때문에 3을 출력 한다
print(s1.find('Name')) # 없는 문자를 넣으면 -1을 출력 한다 # -1 : not found
print('name' in s1) # s1 에 'name'이 있는지 없는지를 bool 타입으로 반환한다.

c = '1'
if c in '0123456789': # c 가 0부터9사이에 숫자라면 참이된다.
    print('true')

print('Name'.lower() in s1.lower()) # 대문자 소문자 상관없이 판단하기 위해 서는 두개의 비교대상을 한쪽으로 몰아준다.


s2 = s1.title() # 각 단어의 첫글자만 대문자로 변환해준다
print(s2)
s3 = s1.capitalize() # 첫글자만 대문자로 변환해준다.
print(s3)

s4 = '                I will be the best programmer@@@@@@@@@@@1'
s5 = s4.lstrip(' ') # 왼쪽부터 공백을 전부 날려준다
s6 = s5.rstrip('@1') # 배열로 생각하기때문에 문자들이 안나올때까지 지운다.
s7 = s5.rstrip('1@') # s6 과 똑같은 결과를 출력한다.
print(s5)
print(s6)
print(s7)



























