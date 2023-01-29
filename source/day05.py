"""
    Day03 - control statement
    Version : 1.0
    Created : 2022.05.24
    Updated : 2022.05.24
    Author : J.W.Lee
"""
# 1. while
i = 1
while i < 10:
    print(i)
    i += 1

# 2. for
for i in range(1,10):
    print(i)
    i = 9 #for문으로 돌아가는 순간 i는 다시 설정되어 이 문장은 무의미

#3. break
n = 1
while True:
    if n == 10:
        break
    print(n)
    n += 1

# 4. continue
print('#' * 40)
print('continue : 1부터 9까지 중에 3의 배수만 빼고 출력')
n = 1
while True:
    if n == 10:
        break
    elif n % 3 == 0:
        n = n + 1
        continue
    print(n)
    n += 1

print("#" * 40)
print("list")
print("#" * 40)

list_simple = [1, 2, 3]
list_bokjap = [[1, 2, 3], [4, 5, 6]]
print(list_simple)
print(list_simple[0])
print(list_bokjap[1][1])

aaa = list_bokjap[0] # aaa는 list가되게된다.

print(list_simple[1:3])

# colors
# 1. 기본 8색
from colors import *

print('8 colors')
str = ['', '', '', '']
str[0] = YELLOW + '노란색' + END
str[1] = CYAN + '하늘색' + END
str[2] = RED_BG + '빨간색바탕' + END
str[3] = BLACK + GREEN_BG + '녹색바탕에 검정색' + END


for s in str:
    print(s)

for i in range(0,4,1):
    print(str[i])

str8 = ' '
for i in range(100,108):
    str8 = str8 + '\033[{}m'.format(i) + '   ' + END
print(str8)

print('256 colors')
str256 = ' '
for i in range(256):
    str256 = str256 + '\033[48;5;{}m'.format(i) + ' ' + END
print(str256)

print('true colors')
str_tc = ['', '', '', '']
for i in range(128,256):
    str_tc[0] = str_tc[0] + '\033[48;2;{};0;0m'.format(i) + "  " + END
    str_tc[1] = str_tc[1] + '\033[48;2;0;{};0m'.format(i) + "  " + END
    str_tc[2] = str_tc[2] + '\033[48;2;0;0;{}m'.format(i) + "  " + END
    str_tc[3] = str_tc[3] + '\033[48;2;{};{};{}m'.format(i,i,i) + "  " + END

for i in range(4):
    print(str_tc[i])