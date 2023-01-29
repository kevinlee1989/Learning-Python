"""
    Day07 -  3 statement
    Version : 1.0
    Created : 2022.05.31
    Updated : 2022.05.31
    Author : J.W.Lee
"""

# 삼항연산자 - 하나의 질문으로 참, 거짓에 따라 값이 달라지는 것
score = 90
text = (score > 99) and "당연한결과" or "그것도 점수냐"
# text = (score > 99) ? " 당연한 결과" : "그것도 점수냐"
print(text)

text = "당연한 결과" if score > 99 else  "그것도 점수냐"
print(text)

# Quiz
# 사용자로부터 숫자 입력을 받습니다.
# 숫자의 개수만큼 "수박수박수...." 를 출력한다.
# user_input, result


# result = ""
# user_input = input("숫자 아무거나 입력하세여 : ")
# i = 1
# while i <= int(user_input):
#     if i % 2 == 1:
#         result += "수"
#     else:
#         result += "박"
#     i = i + 1
#
# print(result)
#
# while True:
#     user_input = input("숫자를 입력하세요 : ")
#     if user_input.isdigit():
#         user_input = int(user_input)
#         break
#
# #General Coding
# result = ''
# for i in range(int(user_input/2)):
#     result += '수박'
# if user_input % 2 == 1:
#     result += '수'
#
# print(result)
#
# # Python only
# result = '수박' * int(user_input/2)
# if user_input % 2 == 1:
#     result += '수'
# print(result)
#
# # Python only, only 1 row
# result = '수박' * int(user_input/2) + "수" * (user_input % 2)

import myutils as mu
mu.cprintTitle("Built-in Functions")
print(eval('134244+12334'))
print("1. eval()")
mu.printExp("200 + 500")

print("2. format()")
mu.printExp("format(34567, ',')")
mu.printExp("format(34567, '_')")

mu.printExp("format('꽥꽥꽥꽥꽥', '비<20')")
mu.printExp("format(1234, '0>10')")
mu.printExp("format(1234, '0>+10')")
mu.printExp("format(1234, '<10')")

print('3. str(), float(), int()')
print('str() : ' + str(47) + '명이 출석 중')
print('float(10)')
mu.printExp('float(10)')
mu.printExp('int(10.9)')

print('4. divmod()')
mu.printExp("divmod(10, 3)")
a = divmod(10, 3)
#a[0] # 몫
#a[1] # 나머지

b = [1, 2, 2]
print(b)
c = tuple(b) # list -> tuple
print(c) #변신성공
d = set(b) #집합
print(d)

print("5. min(), max()")
c = [1,2,3,4,5]
print(min(c), max(c))
d = ["10000000000000", '2', 'A', 'a']
print(max(d))

print("6. abs(), pow(), sum()")
mu.printExp('abs(-50.5)')
mu.printExp('pow(10, 2)')
mu.printExp('sum([100,200,300], 1000)')
g = [[10000,200,300],[10000,500,60000]]
print(max(g))


print("7. round")
mu.printExp("round(234.2)")
mu.printExp("round(234.2, 3)")
mu.printExp("round(2.975, 2)")
mu.printExp("round(2.675, 2)")
mu.printExp("round(2.67500000001, 2)")


print("8. print")
print('010', '1234','5678',sep = '-', end = '|')
print('010','1234','5678',sep ='')


print('9. input()')
# input_str = input('아무거나 쳐보세요')
# a, b, c, d = input_str.split(' ')
# print(a, b, c, d)


print('10. len()')
mu.printExp("len('abcde')")
student = ['A1','B2','C3']
print(len(student))
print(len(student[0]))
