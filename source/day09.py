"""
    Day09 -
    Version : 1.0
    Created : 2022.06.03
    Updated : 2022.06.03
    Author : J.W.Lee
"""

from colors import*
from myutils import*



tuple_a = (1,2) # 튜플은 데이터가 변경되는 Method를 혀용하지않는다 ex) remove(), index(), clear() X
print(tuple_a.index(2))

cprintTitle("Set Method")
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
c = a.intersection(b) #교집합
d = a.union(b) #합집합
e = a.difference(b) #차집합
print('교집합' , c)
print('합집합' , d)
print('차집합' , e)


cprintTitle("Dictionary Method")
dic = {1: 'one', 'subject' : ['science', 'korean'], '숫자' : 1234}
print(dic)
# print(dic[1:3]) # dictionary는 순서가 없음
print(list(dic.keys())) # keys()의 결과는 dict_key type 이기때문에 앞에 list로 변환을 꼭해줘야 한다.
print(dic.values())
print(dic.items())

print('dic[1]', dic[1])
print('dic.get(1)', dic.get(1))

#print(dic[8]) # 해당 key가 없으면 오류
print('dic.get(8)', dic.get(8)) # get()을 썻을떄는 오류가 아니라 None 이된다
print(dic.get(8, "그런건 없지롱")) # 뒤에 데이터를 넣어주면 없을떄는 그값으로 대체를 할 수 있게된다

person = {'name' : '이재우', 'age' : 25, 'blood type' : 'O'}

# person에서 꺼내오면 key만 꺼내옴
for item in person:
    # print(item) # key들만 순차적으로 출력한다
    print(item, person.get(item))

for item in person.items():
    print(item[0], item[1])

cprintTitle("String")
a = 'abcdefg'
print(a)
print(a[0], a[1], a[2], a[5])
print(a[1:3])
print(a[3:])
print(a[3::2])

cprintTitle("Array copy")
a = list(range(1, 11)) # 1 부터 10
print(a)
b = a[1:8]
print(b)
c = a[1:8:2]
print(c)


e = (1, 2, 3, 4, 5)
f = e[2:]
print(f) #f 는 튜플 타입

g = {1, 2, 3, 4, 5}
# h = g[1:3] # 세트는 순번이 없기떄문에 선택적으로 복사할수가없다, 즉 set는 index라는것이 존재하지않는다
h = g


cprintTitle("User define Function")
printMessage1()
printMessage2('Happy 재우')
 # printMessage2() # missing argument
printMessage3('unHappy')
printMessage3()
printMessage4('hhh', 3)
printMessage4()
printMessage4(i=4)


val = getRandomDice(10000)
print(val)

vals1, vals2, vals3 = getMultiDice(1000)
print(vals1, vals2, vals3)

v = getMultiDice(1000) # 리턴 값이 여러 개인데 하나로 받는 경우 튜플로 받아짐
print(v)

s = addAll(2,3,4,5,6,7,8,9)
print(s)












user_input = input('전화번호를 입력하세요 ( 숫자와 - 기호만 사용하시오 ) : ')
a,b,c = checkPhoneNumber(user_input)
print(a,b,c, sep = '-')
