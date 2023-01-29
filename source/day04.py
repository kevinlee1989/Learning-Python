"""
    Day03 - control statement
    Version : 1.0
    Created : 2022.05.20
    Updated : 2022.05.20
    Author : J.W.Lee
"""
from colors import *
print(RED + "while" + END)
print('노가다')
print('1번 출력')
print('2번 출력')
print('3번 출력')
print('4번 출력')
print('5번 출력')
print('6번 출력')
print('7번 출력')
print('8번 출력')
print('9번 출력')
print('10번 출력')
print()

print('자동화')
i = 1
while i < 11:
    print('{}번 출력'.format(i))
    i = i + 1

i = 0
# while True:
#     print("막을 수가 업어{}!".format(i))
#     i = i + 1    # i += 1


# while True:
#     num = input("1에서부터 10까지의 숫자 중 하나를 입력해주세요 :")
#     if num.isdecimal() == True and int(num) >= 1 and int(num) <= 10:    #숫자이면 TRUE 문자이면 FALSE
#         print('입력하신 숫자는 {}입니다'.format(num))
#         break
#     else:
#         print('{}는 잘못 입력한 값이잖아'.format(num))


print(GREEN + 'for' + END)
for s in '문자열들':   #문자열
    print(s, end = '-')

print()
for l in ['first','second','third']:  # 리스트
    print(l)

print()
season4 = ['Spring','Summer','Fall','Winter']  # 튜플
for t in season4:
    print(t)

print()
season4 = {'Spring','Summer','Fall','Winter'}  # 세트, 순서 무작위
for t in season4:
    print(t)

print()
for i in range(1,11,1): # 레인지
    print("{}번 출력".format(i))

print()
person = {'name':'py', 'age':[100,200,300]} # 딕트
for d in person:
    print(d,person[d],person.get(d)) # 첫번째는 그냥 key 만 출력, 두번째와 세번째는 둘다 value 를 출력

for item in person.items(): # 딕트인데 key 와 value 를 둘다 동시에 가져오는 방법
    print(item)
