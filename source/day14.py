"""
    Day13 -  Linked List
    Version : 1.0
    Created : 2022.06.17
    Updated : 2022.06.17
    Author : J.W.Lee
"""
# list example
alist = [1,2,3,4,5]
print(alist)
print(len(alist))

blist = [1,2,[3,4],5]
print(len(blist))

blist.append(6) # 맨 뒤에 6을 추가
print('#1', blist)

# append 7 to the frist place
blist.insert(1, 7)
print('#2' ,blist)
# delete the last data
ppp = blist.pop()
print('#3', ppp,  blist)
# 맨 앞의 값을 qqq에 저장하고 삭제
qqq = blist.pop(0)
print('#4', qqq, blist)

#list Challenge 1
clist = [100, 200, 300, 400, 500]
# dlist = [500, 400, 300, 200, 100]

# result = []
# for i in range(len(clist)):
#     result.append(clist[4-i])
# print(result)

result = clist[::-1] # 배열을 역순으로 복제
print('Q1:', result)

# list Challenge 2
list1 = ['M','na','i','Ke']
list2 = ['y','me','s','lly']
#result = ['My','name','is','Kelly']

# solution 1
list3 = []
for i in range(0, len(list1)):
    list3.append(list1[i]+list2[i])
print('Solution 1. ', list3)

# solution 2
list3 = []
for i in zip(list1, list2):
    list3.append(i[0]+i[1])
print('Solution 2. ', list3)

# solution 3
list3 = [i+j for i, j in zip(list1, list2)]
print('Solution 3. ', list3)

# list challenge 3
list3 = [1,2,3,4,5]
#result = [1,4,9,16,25]
result = [i*i for i in list3]
print('Challenge 3 solution. ', result)

# list challenge 4
list4 = ['Hello', 'Make']
list5 = ['Bye', 'Sleep']
# result = ['Hello Bye' , 'Hello Sleep', 'Make Bye', 'Make Sleep']
result = [i + ' ' + j  for i in list4 for j in list5]
print('Challenge 4 ' ,result)

# list challenge 5
list6 = [10,20,30,40]
list7 = [100,200,300,400]
"""
result
10 400
20 300
30 200
40 100
"""
print()
print('result')
for i,j in zip(list6,list7[::-1]):
    print(i, j)

# list challenge 6
list8 = [5,10,15,20,25,30,35]
# 20을 200으로 변경
# for i in range(len(list8)):
#     if list8[i] == 20:
#         list8[i] = 200
# print(list8)
list8[list8.index(20)] = 200 # index() 는 괄호안의 있는 수를 처음으로 찾는 인덱스를 가져온다.
print(list8)

# stack
print()
print('**** Stack ****')
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop()
stack.pop()
print(stack)
stack.pop()
print(stack)

# queue
print()
print(' **** Queue ****')
# 1. list로 구현
queue1 = []
queue1.append(1)
queue1.append(2)
queue1.append(3)
print(queue1)
queue1.pop(0)
queue1.pop(0)
print(queue1)
queue1.pop(0)
print(queue1)

# 2. Queue 클래스로 구현
import queue
import time
q1 = queue.Queue()
time1 = time.time()
for i in range(10000):
    q1.put(i)
for i in range(10000):
    q1.get(i)
time2 = time.time()

q2 = []
time3 = time.time()
for i in range(10000):
    q2.append(i)
for i in range(10000):
    q2.pop(0)
time4 = time.time()

print(time.ctime())
print('Queue(class) : ', time2 - time1)
print('Stack(mine) : ', time4 - time3)

