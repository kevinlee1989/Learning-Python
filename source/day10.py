"""
    Day10 -  variables
    Version : 1.0
    Created : 2022.06.07
    Updated : 2022.06.07
    Author : J.W.Lee
"""

from myutils import*

cprintTitle("Global, local Variables")

# 1 step
gv = 10

def printVar1():
    print('1 step gv :', gv)

printVar1()

# 2 step
def printVar2():
    lv = 20
    print('2 step gv :', gv)
    print('2 step lv :', lv)

printVar2()

# 3단계
def printVar3():
     # print('3 step gv:', gv)
    gv = 30
    lv = 30
    print('3 step gv :', gv)
    print('3 step lv :', lv)
printVar3()
print('3 step gv: ', gv)

# 4 step
def printVar4(gv):
    print('4 step gv:', gv)
    gv = 40
    lv = 40
    print('4 step gv: ', gv)
    print('4 step lv:', lv)
printVar4('abcd')
print('4 step gv:' , gv)

# 5 step
def printVar5():
    lv = 50
    return lv
gv = printVar5()
print('5 step gv :', gv)

# 6 step
gv1 = 61
gv2 = 62

def printVar6():
    global gv1
    gv1 = 601
    globals()['gv2'] = 602
    gv2 = 702 # no effect

printVar6()
print('6 step gv1:', gv1)
print('6 step gv2 :', gv2)

# 7 step
if gv1 == 601:
    lv1 = 300

print('7step lv1 :', lv1)

# 8 step

import random as r

i = 9375482948
for r in range(5): # for 는 함수랑 달르고 정식멤버라 i의 값이 변경해지는게 인정된다.
    print(r)


print('8 step i :', i)

cprintTitle("Time module")

import time

t1 = time.time()
t2 = time.ctime()
t3 = time.strftime('%Y%m%d %H:%M:%S')

print('time.time() :' , t1)
print('time.ctime() : ', t2)
print('time.strftime() :', t3)

cprintTitle('File In/Out')
s1 = 'We are studying Python'
s2 = '우리는 파이썬을 공부중입니다'

f = open('sample.txt', 'wt', encoding = 'utf-8') # cp949 모드 : 윈도우에서 지원하는 한글 모드임
f.write(s1)
f.write('\n')
f.write(s2)
f.close()

f = open('sample.txt', 'rt', encoding = 'utf-8')
while True: #읽는 방법
    readstr = f.readline()
    if readstr == '':
        break
    print(readstr)

#readlines(10) : 10줄 읽기는 아니다, 10글자가 넘어가는 라인까지 읽음
















