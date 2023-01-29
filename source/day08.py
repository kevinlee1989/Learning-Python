"""
    Day08 -  built in function
    Version : 1.0
    Created : 2022.06.02
    Updated : 2022.06.02
    Author : J.W.Lee
"""

from myutils import *

cprintTitle("11.range()")
printExp("range(10)")
print(type(range(10)))

a = list(range(10))
print(a)
a = list(range(1,100,2)) # 1,3,5,....99
print(a)
a = list(range(10,0,-1)) # 10,9,8,7,6,5,4,3,2,1
print(a)
a = list(range(0,15,-5)) # 도달할 수 없는 조건이라면 []
print(a)

cprintTitle("12. sorted() ")
student = ['A학생11111', 'a학생', 'B학생', '12345']
# ASCII 아스키코드 0x30(16*3 + 1*0 = 48) <- 0x2F  (16진수)
# 0x30 부터가 숫자, 0x41(16*4 + 1*1 = 65)부터 영대문자, 0x61(97)부터 영소문자
student_a = sorted(student, reverse = False) #오름차순
print(student_a)
student_d = sorted(student, reverse = True) #내림차순
print(student_d)

# ttt = [1, 'AAA']
# ttt_a = sorted(ttt, reverse = False) # 문자열과 숫자는 비교할수 없음
# print(ttt_a)

cprintTitle("13. enumerate(), zip()")
print(enumerate(student))
student_e = list(enumerate(student))
print(student_e)

for s in enumerate(student):
    print(s[0], s[1])

student_i = ['30444','30122','20312','11111']
print(zip(student_i))
print(zip(student, student_i))
print(list(zip(student, student_i)))

for s in zip(student, student_i):
    print(s[0], s[1])

#Method
cprintTitle("Method of List")
list_a = [1,2,3]
print(list_a)
#list_a[3] = 4 # index out of range    cf) Java : ArrayOutOfBoundsException
list_a.append(4)
print(list_a)
# list_aaaaa = [4,5,6,7,8,9]
# list_a.append(list_aaaaa)
print(list_a)
list_a.append('abcde')
print(list_a)

list_a.insert(2, 65555)
print(list_a)
list_a.insert(6, 888)
print(list_a)

#list_a.append(1234545)
#list_a.insert(len(list_a), 1234545)

# list 와 list의 합작품
list_b = [4,5,6,7,8]
list_a.extend(list_b)
print(list_a)
print('extend01', list_a)
# tuple 과 list의 합작품
tuple_a = (4444, 5555)
list_a.extend(tuple_a)
print('extend02', list_a)
# set 과 list의 합작품
set_a = {1233, 4566}
list_a.extend(set_a)
print('extend03', list_a)

b = list_a.pop()
print('pop01', list_a)
c = list_a.pop(0)
print('pop02', list_a)
f = list_a.remove('abcde')
print('remove01', f, list_a)
list_a.remove(4) # 중복된 값이 있으면 앞에 값만 삭제
print('remove02', list_a)

g = list_a.index(4)
print('index01', g, list_a)
# h = list_a.index(4, 5) # 못찾으면 오류, 오류 안내려면 추후 학습할 except

list_a.clear()
print(list_a)
