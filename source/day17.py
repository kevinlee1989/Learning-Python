"""
    Day17 -  Numpy(2)
    Version : 1.0
    Created : 2022.06.28
    Updated : 2022.06.28
    Author : J.W.Lee
"""
import numpy as np
from myutils import*

cprintTitle('7) unique')
rd = np.random.randint(1, 10, (3, 4))
print(rd)
number, count = np.unique(rd, return_counts = True)
print('unique한 값은 ', number)
print('unique한 값의 개수는 ', count)
number = np.unique(rd)
print('unique한 값은', number)

print()

cprintTitle('8) concatenate')
na1 = np.random.randint(10, size=(2,3))
na2 = np.random.randint(10, size=(3,2))
na3 = np.random.randint(10, size=(3,3))
print(na1)
print(na2)
print(na3)

print('8-1) 세로 결합')
c_con = np.concatenate((na1, na3))
print(c_con)

print('8-2) 가로 결합')
r_con = np.concatenate((na2, na3), axis=1)
print(r_con)

print()
cprintTitle('9) split')
r = np.arange(11,20)
print(r)

array1= np.split(r, [5])
print(array1)
array2 = np.split(r, [2,4,6,8])
print(array2)

print()
cprintTitle('10) sort')
r1 = np.random.randint(10, size=(3,3))
print(r1)
print('가로정렬')
r1.sort()
print(r1)
print('세로정렬')
r1.sort(axis = 0)
print(r1)
print()
"""
Quiz 5
1 부터 20까지의 랜덤숫자를 갖는 5 * 5의 행렬을 만드시고
최소값과 최대값을 sort를 사용하여 구하시오.
"""
cprintTitle('Quiz 5')
na = np.random.randint(1, 21, size=(5,5))
print(na)
na.sort()
na.sort(axis=0)
print('min : ', na[0,0])
print('max : ', na[4,4])

print('\n\n')
cprintTitle('NUMPY 연산')
print('1) basic')
# list 연산
ls = []
print('[1,2,3] * 3 => ', [1, 2, 3]*3)
# ndarray 연산
na = np.array([1,2,3])
print('na * 3 =>', na * 3)
nb = np.array([4,5,6])
print('na * nb => ', na*nb)
print()

print('2) compare')
print('na : ', na)
print('nb : ', nb)
print('na == 2 : ', na == 2)
print()

print('3) filter')
print('na[na==2] : ', na[na==2])
na3 = np.array([1,2,3,2,2])
print('na3[na3==2] : ', na3[na3 ==2])
print('nb[nb>4] :', nb[nb>4] )
nf = [True, False, True, False, True]
print('na3[nf] : ', na3[nf])

na4 = np.arange(10)
print(na4)
# 3의 배수만 출력
print(na4[na4 % 3 == 0])

# 2개의 ndarray에서 같은 데이터만 남김
ls1 = [1,2,3,4,5]
ls2 = [1,0,3,0,5]
print('ls1 == ls2 :', ls1 == ls2)
na1 = np.array(ls1)
na2 = np.array(ls2)
print('na1 == na2 : ', na1 == na2)
print()

print('4) bradcasting')
na = np.array(range(12)).reshape(3, 4)
print(na)

# 모든데이터에 1 더하기
print('모든 데이터에 1을 더하는 방법은 na + 1 :', na + 1)

# 모든 행에 na1 더하기
na1 = np.array(range(4))
print(na1)
print(na + na1)


#모든 열에 na2 더하기
na2 = np.array([[1000],[2000],[3000]])
print(na2)
print(na + na2)
print()


print('5) NUMPY functions')
na = np.random.randint(10, size=(2,3))
print(na)

#min, max, argmin, argmax
print('min, max : ', na.min(), na.max())
print('argmin, argmax : ', na.argmin(), na.argmax())

# sum
print('np.sum(na) :', np.sum(na)) # 전체를 합해준다
print('np.sum(na, axis=0) :', np.sum(na, axis=0)) # 세로 값들을 더해준다
print('np.sum(na, axis=1) :', np.sum(na, axis=1)) # 가로 값들을 더해준다

# mean, median
print('mean(na) :', np.mean(na))
print('median(na) :', np.median(na))
print()

'''
Quiz 6
1부터 20까지 랜덤숫자를 가지는 5*5 행렬을 만드시고
최소값과 최대값은 숫자(min), 숫자(max)로 출력하시오
'''

cprintTitle('대망의 퀴즈!!!!!!!!!!')

# Making a random ndarray
na = np.random.randint(1, 21, size=(5,5))
print(na)

# Defining Max And Min
minv = na.min()
maxv = na.max()

# Changing ndarray type to string type(<U8)
na_r = na.astype(dtype = '<U8')
na_r = na_r.reshape(25)
print(na_r)

# adding 최소, 최대값 to the string type
for i in range(len(na_r)):
    if na_r[i] == str(minv):
        na_r[i] += '(min)'
    if na_r[i] == str(maxv):
        na_r[i] += '(max)'

print(na_r)

# Returning to original shape of ndarray

result = na_r.reshape(na.shape)
print(result)





































