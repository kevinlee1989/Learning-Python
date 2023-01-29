"""
    Caluclator
"""
"""
    1. 무한루프로 사용자에게 수식을 입력받는다.
    2. 수식 대신 'X'를 입력하면 종료한다.
    3. 수식을 계산해서 수식과 결과를 출력한다. 총 40칸으로 오른쪽 정렬해서 결과를 출력
    4. 사용자가 수식을 계속해서 입력하면 기존 수식들을 출려고하고
       기존 결과에 추가로 수식을 계산한 결과를 출력한다.
    5. 수식대신 'C'를 입력하면 0을 출력하고 수식들을 다 비운다.
"""
from myutils import*
from colors import*

# 0. 타이틀을 출력한다.
cprintTitle('Calculator for Engineering')

# list_result = []
#
# while True:
#     user_input = input('수식을 입력하세요 :')
#     if user_input == 'X':
#         break
#     list_result.append(user_input)
# print(list_result)

exp_list = []
isFirst = True

# 1. 무한루프로 사용자에게 수식을 입력받는다. X를 입력하면 종료한다
while True :
# 1-1. 입력받은 수식은 exp, 그동안 입력했던 수식들은 exp_list
    exp = input("수식을 입력하십시오(종료는 X, 초기화는 C) : ")

# 1-2. X를 입력하면 종료, C를 입력하면 0을 출력하고 초기화후 루프진행
    if exp == 'X':
        break
    elif exp == 'C':
        print(0)
        isFirst = True
        exp_list.clear()
        continue

# 3. 수식을 계산한다.
    if isFirst == True:
        exp1 = exp
    else:
        exp1 = str(res) + ' ' + exp

    res = eval(exp1)
    isFirst = False

# 4. 수식을 저장한다.
    exp_list.append(exp)

# 5. 수식을 출력한다.
    # print(exp_list)
    for e in enumerate(exp_list): #enumerate함수는 리스트 앞에 순번을 매겨준다 그래서 e에 2개의 데이터가 들어가게돈다 ( 순번, 데이터)
        if e[0] == len(exp_list) - 1: # 맨 마지막 수식이면
            print(RED + format(e[1], '>40') + END)
        else:
            print(GREEN+ format(e[1], '>40') + END)


# 6. 결과를 출력한다
    print(YELLOW + '-'*40 + END)
    print(format(res, '>40'))
