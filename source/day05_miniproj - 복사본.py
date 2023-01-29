"""
    Mini Project
    Version : 1.0
    Created : 2022.05.24
    Updated : 2022.05.24
    Author : Kevin Lee
"""
"""
    1. 보물상자에서 무기를 5종류 중 랜덤으로 하나를 획득한다.
    2. 길을 가다가 늑대, 산적, 드래곤 중 랜덤으로 하나를 만난다. 
    3. 무기를 가지고 둘 중 하나의 에너지가 0이 될 때까지 싸운다.
        사용자는 공격, 회복 중 하나늘 선택하며 상대는 공격만 한다.
    4. 승리 또는 패배에 따라 메시지를 출력한다.
"""
# 1. Opening => Pseudo Code
import time
from colors import *
#0
print("*" * 40)
print("게임이 시작되었다 준비해라!!!!!!!!!!")
print("*" * 40)


print(YELLOW + "[보물상자]" + END + "를 발견하였다.")
input( "보물상자를 열기위해서 아무키와 엔터키를 누르도록하여라.")


# 1-2. 보물상자에서 랜덤으로 1개의 무기를 획득한다
# 각 무기는 [무기이름, 최소공격력, 최대공격력]의 데이터를 가진다
# random, list 익히기

weapon_list = [['휴지',1,3],['목검',3,5],['대검',5,10],['대포',1,50],['에픽밸붕검',50,100]]
import random
sel = random.randint(0,4)
print(sel) # only for debugging
weapon = weapon_list[sel]
print(weapon)


if sel == 0:
    print("당신은 [{}]({} ~ {})을/를 획득했다!!!".format(weapon[0],weapon[1],weapon[2]))
elif sel == 1:
    print("당신은 " + GREEN + "[{}]({} ~ {})".format(weapon[0],weapon[1],weapon[2]) + END + "을/를 획득했다!!!")
elif sel == 2:
    print("당신은 " + BLUE + "[{}]({} ~ {})".format(weapon[0], weapon[1], weapon[2]) + END + "을/를 획득했다!!!")
elif sel == 3:
    print("당신은 " + YELLOW + "[{}]({} ~ {})".format(weapon[0],weapon[1],weapon[2]) + END + "을/를 획득했다!!!")
else:
    print("당신은 " + MAGENTA + "[{}]({} ~ {})".format(weapon[0],weapon[1],weapon[2]) + END + "을/를 획득했다!!!")

time.sleep(1) #1초를 쉬게한다

# 2. 길을 가다가 늑대, 산적, 드래곤 중 랜덤으로 하나를 만난다.
mon_list = [['늑대',1,3],["산적",5,10],["드래곤",1,100]]
sel2 = random.randint(0,2)
mon = mon_list[sel2]
if sel2 == 0:
    print("길을 가다가 당신은 몬스터[{}({}-{})]을/를 만났습니다".format(mon[0],mon[1],mon[2]))
elif sel2 == 1:
    print("길을 가다가 당신은 " + GREEN + "[{}]({} - {})".format(mon[0],mon[1],mon[2]) + END + "을/를 만났습니다")
else:
    print("길을 가다가 당신은 재수없게도 " + RED + "[{}]({} - {})".format(mon[0], mon[1], mon[2]) + END + "을/를 만났습니다")

# 3-1. 초기 양쪽의 에너지는 100이다. my_energy, mon_energy에 저장한다.
my_energy = 100
mon_energy = 100

# 3-2 무한루프로 전투를 한다. 무한루프는 둘 중 하나의 에너지가 0이하가 되면 탈출한다.
while True:
    # 3-3 사용자는 공격 또는 회복을 한다.
    while True:
        user_input = input("행동을 선택하라!(1.공격, 2.회복 : )")
        if user_input == "1" or user_input == "2":
            if user_input in "12":
                break
    # 3-4. 공격을 선택했다면 최소와 최대 공격력 사이로 공격을 한다
    if user_input == "1":
        print("공격선택을 선택하셨습니다")
        mydamage = random.randint(weapon[1],weapon[2])
        mon_energy = mon_energy - mydamage
        print("당신은 공격으로 {}의 데미지를 입혔다!! {}의 현재 체력 : {}".format(mydamage,mon[0],mon_energy))

        if mon_energy <=0:
            break
            time.sleep(1)  # 1초를 쉬게한다

    # 3-5 회복을 선택했다면 0 부터 30 까지의 에너지를 회복한다
    elif user_input == "2":
        print("회복을 선택하셨습니다")
        heal = random.randint(0,30)
        my_energy = my_energy + heal
        if my_energy > 100:
            my_energy = 100
        # my_energy = (my_energy > 100) ? 100 : my_energy
        print("당신은 회복으로 {}의 에너지가 회복되었습니다. 현재 나의 체력 : {}".format(heal,my_energy))

    # 3.6 몬스터가 최소와 최대 공격력 사이로 공격을 한다.
    mondamage = random.randint(mon[1],mon[2])
    my_energy = my_energy - mondamage
    print("당신은 {}의 공격으로 {}의 피해를 입었습니다. 당신의 체력 {}".format(mon[0],mondamage,my_energy))
    if my_energy <= 0 :
        break
        time.sleep(1)  # 1초를 쉬게한다



#4. 승리 또는 패배에 따라 메시지를 출력한다
if my_energy >0:  #승리
    print("당신이 승리하였습니다!!!!!!")
else :
    print("당신은 죽었습니다.....")
# 5. 프로그램 종료 선언
print()
print("운명의 게임 끄읕!!!!!!!!!!!")