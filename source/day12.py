"""
    Day12 -  class
    Version : 1.0
    Created : 2022.06.14
    Updated : 2022.06.14
    Author : J.W.Lee
"""
import myclasses as mc
from myutils import*

# class variable, instance variable
myhouse = mc.House('My House')
myhouse.welcome()
print(myhouse.house_count)
print(myhouse.name)
# myhouse.house_count = 500 # 클래스 변수를없애고 새로운 객체변수를 그냥 만든것이다.
print(myhouse.house_count)

yourhouse = mc.House('Your House')
print(myhouse.house_count)
print(yourhouse.house_count)

hishouse = mc.House()
print(hishouse.name)
# instance variable

print(yourhouse.__dict__) # 가지고 있는 local 함수를 나타내준다

# docstring test
print(mc.House.__doc__) # class 밑에의 주석을 출력해준다


# special type test
hishouse.data_process('pppp')
hishouse.data_process(1000)
hishouse.data_process([1,2,3,4])

# class test
apart1 = mc.Apart()
apart2 = mc.Apart()
print(apart1.get_room()) #아무것도 안하고 그냥 room의 갯수(default) 값은 3
apart1.set_room(99) # set_room 함수를 사용함으로써 99개의 방을 apart1 객체 변수에 99를 할당한다.
print(apart1.get_room())
apart1.add_furniture('Sofa')
apart1.add_furniture('TV')
apart1.add_furniture('Bed')
apart1.show_furniture()
apart2.show_furniture()

list_a = [apart1, apart2]
print(list_a)


# Exception
cprintTitle('Exception')
try:
    a = int(input('please input the number that is divided : '))
    if a > 10000:
        raise Exception('kidding me? ')
    b = int(input('Please input the number to divide : '))
    c = a/b
    print('{}/{} = {}'.format(a,b,c))
except ZeroDivisionError as e:
    print('are you trying to divde by 0?')
    print(e)
except ValueError as e:
    print('only the integer can be the result')
    print(e)
except Exception as e:
    print(' I don\'t know what exactly error is.... but there should be an error somewhere ')
    print(e)
else:
    print('there are no errors and you have coded well! ')
finally:
    print('this sentence will appear either there is any error or not') # 이거는 그냥 무조건 수행하고 끝낸다

print()
print()

# 사용자가 exeption 발생
def alwaysAngry():
    raise mc.MyException('you dare call me ')

try:
    alwaysAngry()
except Exception as e:
    print('there is an exception')
    print(e)





