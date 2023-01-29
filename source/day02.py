"""
    Day02 - pring, input, operator
    Version : 1.0
    Created : 2022.05.17
    Updated : 2022.05.17
    Author : J.W.Lee
"""
RED = '\033[91m'
GREEN = '\033[92m'
END = '\033[0m'

print(GREEN + '1.print' + END)

# 1. 화면에 Hello + 본인이름 을 출력하시오.

print('Hello 저는 이재우라고 합니다')
print('Hello ' + 'jwlee', end='|')
print()

# 2. Mary's consmetics

#첫번째 방법 :
print('Mary\'s cosmetics')
#두번째 방법 :
print("Mary's cosmetics")

# 3. 신씨가 "도둑이야"라고 소리쳤다.
print('신씨가 "도둑이야"라고 소리쳤다.')
print("신씨가 \"도둑이야\"라고 소리쳤다.")

# 4. a = 'first', b = 'second' 일때 first second를 출력하시오.

a = 'first'
b = 'second'
print(a + ' ' + b)
print(a, b)
# a 와 b 사이에 컴마를 넣어주게 되면 띄어쓰기가 되게된다.

print(RED + "2.input" + END)
# a = input()
# print(a)
# b = input("값을 입력하세요 : ")
# print(b)
# a, b = input("두 개의 값을 입력하세요 : ").split(" ")
# c = a + b
#c= int(a) + int(b)
# a1 = float(a)
# b1 = float(b)
# c = int(a1) + int(b1)
# d = float(a1) + float(b1)
# print(a, b, "연산결과: " ,c, d)

print( GREEN + '3.operator' + END)
print('(1)산술연산자')
a = 'My name'
b = 'is None'
print(a + ' ' + b)
c = 'I \'ll be'
d = 100
print(c + ' ' + str(d))
# str() : 숫자를 문자열로 바꾸어준다
print('10 - 10.9 =', 10 - 10.9)
#print('my name' - 'my') 오류, 문자열의 뺄셈은 불가

print('안녕' * 5)
# print('ddd' /3) 오류, 문자열의 나누기는 불가

print('10 // 3 =', 10 // 3)
print('10 % 3 =', 10 % 3)
print('5 ** 1.25 =', 5 ** 1.25)

print('(2)비교연산자')
a = 30
b = 20
c = a > b
print(c)
print(type(c))
print('10 > 10 :', 10 > 10)
print(' 10 >= 10 :', 10 >= 10)
print('10 == 20 :', 10 == 20)
print('a != b :', a != b)

print('(3)논리연산자')
a = -30   # 온도를 의미
b = 0    # 내복 착용 여부

c = a < - 10 and b == 0
d = a < -10 or b == 0
print(c)
print(d)

e = True ^ False ^ False
print(e)
