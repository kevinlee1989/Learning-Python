"""
    1. '이름을 입력하세요 :'를 출력하고 입력을 받는다
    2. '최대 숫자를 입력하세요 :'를 출력하고 입력을 받는다
    3. 1부터 입력한 수 사이의 임의의 수를 만든다.
    4. 숫자 입력을 받아 임의의 수와 같은지 맞추는 게임을 만든다.
       정답은 몇일까요? 를 출력하고 입력을 받는다.
       임의의 수와 입력한 수가 동일할 때까지 계속한다.
       5번까지 못맞추면 종료한다.
    5. 한 번에 정답을 맞추면 '***님 대단하다'
       세 번 이내에 맞추면 '***님 우수한 성적이다'
       다섯 번 이내에 맞추면 '***님 좀 심하십니다'
       다섯 번까지 못맞추면 '정답은 *입니다. ***님 사람 맞나요?'
"""

#1
name = input('이름을 입력하세요 :')
print(name)

#2
max = input('최대 숫자를 입력하세요 :')
while True:
    if max.isdecimal() == True:
        print(max)
        break
    max = input('최대 숫자를 입력하세요 :')

#3
import random
rand_int = random.randint(1,int(max))
print(rand_int)

#4

count = 1
while True:
    ans = input('정답은 몇일까요? :')
    if int(ans) == rand_int:
        break
    count = count + 1
    if count > 5:
        print('기회다날라감 ㅅㄱ')
        break

# correct = False
# for count in range(0,5):
#     ans = input('정답은 몇일까요? :')
#     if ans.isdecimal():
#         if rand_int == int(ans):
#             correct = True
#             break


if count == 1:
    print('{}님 대단하다'.format(name))
elif count <= 3:
    print('{}님 준수하다'.format(name))
elif count <= 5:
    print('{}님 심하다'.format(name))
else:
    print('정답은 {}입니다. {}님 사람 맞나요?'.format(rand_int, name))
