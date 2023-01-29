"""
    Day03 - str, condition statement
    Version : 1.0
    Created : 2022.05.19
    Updated : 2022.05.19
    Author : J.W.Lee
"""


print(":Day3 - str.format")
a = 1
print("a의 값은: ", a)  #기존방법

print("{}은 또 하나의 {}함수 {}입니다".format('이것','print','사용법'))
print("숫자도 되는지 해보죠 {}".format(10))
print("괄호보다 입력이 더 많을 때는 {}".format('되네','궁금합니다'))
# print("괄호보다 입력이 더 적을 때는 {} {}".format('되나요'))  #괄호가 입력보다 더 많을때는 오류

print("#" * 40)
print("이름:{name}, 주소:{addr}, 번호:{no}".format(name='파이썬',addr='오금역',no = 103))

print("#" * 40)
print("Day3 - if statement")
a=1
if a > 0:
    print("a는 양수")

if a == 1:
    print("a는 1입니다다")
if not a !=1:
    print("a는 1이 아닌게 아님, 즉 1이냐는 뜻")

a = -100
if a > 0:
    print("a는 양수2")
     # print("a는 양수3") #파이썬은 줄이 안맞아도 에러가 뜬다!(문법 오류)
 #print("a는 양수4") #이것마저 indent가 이상하기때문에 오류가 뜬다!
print("a는 양수5")

#if a < 0: print("a는 양수6") #문제가 되지않는다. 하지만 지극히 예외적일때만 쓴다
#          print("a는 양수7") #그다음 줄이 완벽하게 일치해도 오류가 뜨기떄문이다.

if a < 0: print("a는 양수8"); print("a는 양수9")

#if a = 2: # 파이썬은 이런 것을 허용하지않는다
#    print("a는 2임")
print()

import colors #모둘
print(colors.RED + "if-elif-else" + colors.END)
#다른방법 2
# from colors import*
# print(RED + "if-elif-else" + END)

e = input()
if e>0:
    print("positive")
elif e ==0:
    print("zero")
else:
    print("negative")




































