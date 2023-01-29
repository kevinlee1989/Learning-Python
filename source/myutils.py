import random


def cprintTitle(str):
    col = random.randint(0,255)
    print("\033[38;5;{}m".format(col))
    print("*" * 40)
    print(str)
    print("*" * 40)
    print('\033[0m')

def printExp(str):
    print(str + "=> {}".format(eval(str)))


def printMessage1():
    print('인수도 없고 결과값도 없는 사용자 함수랍니다 호호호!')

def printMessage2(message):
    print(message)

def printMessage3(message = '입력을 하지않으셨는데영~'): # printMessage2 보다는 printMessage3 을 더 사용하는 편이다.
    print(message)

def printMessage4(message=' you input nothing', i = 5):
    for j in range(i):
        print(message)

def getRandomDice(i=6):
    r = random.randint(1, i)
    print('당시은 ', r ,'을 얻었습니다!')
    return r


def getMultiDice(i=6):
    r1 = random.randint(1, i)
    r2 = random.randint(1, i)
    r3 = random.randint(1, i)
    return r1, r2, r3

def addAll(*i):
    res = 0
    for j in i:
        res = res + j
    return res

"""
    1. str이 숫자와 '-' 로만 구성이 되어 있는지 체크
    2. 숫자가 10자리 또는 11자리인지 체크
    3. 10자리이면 XXX, XXX, XXXX return
       11자리이면 XXX, XXXX, XXXX return
    4. 비정상이면 999, 9999, 9999 return
"""
# def checkPhoneNumber(user):   # 내가한것
#     error = True
#
#     for i in user:
#         if not(i.isdigit()) and i != '-':
#             error = False
#
#     if error == True and len(user) == 10:
#         print('10자리입니다')
#     elif error == True and len(user) == 11:
#         print('11자리입니다')
#     else:
#         print('비졍상입니다')

def checkPhoneNumber(str):
    ndigit = 0
    nstring = ''

    # 1. 숫자와 '-'로만 구성되어 있는지 check
    for c in str:
        if c in '0123456789-':
            if c == '-':
                ndigit = ndigit + 0 #pass
            else: # 숫자이면
                ndigit = ndigit + 1
                nstring = nstring + c
        else:
            return '999', '9999', '9999'

    # 2. 숫자가 10자리인지 11자리인지 check
    if ndigit == 10:
        return nstring[0:3], nstring[3:6], nstring[6:10]
    elif ndigit == 11:
        return nstring[0:3], nstring[3:7], nstring[7:11]
    else:
        return '999', '9999', '9999'







