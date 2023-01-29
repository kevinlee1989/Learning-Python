"""
    Day16 -  Numpy
    Version : 1.0
    Created : 2022.06.23
    Updated : 2022.06.23
    Author : J.W.Lee
"""
import numpy as np

#1. 행렬의 생성 1
print('1-1 ) 1차원 행렬')
a1 = np.array([1,2,3])
print(a1, type(a1))

print()
print('1-2) 2차원 행렬')
a2 = np.array([[1,2,3],[4,5,np.NaN]])
print(a2)

print('1-3 ) ')
print('차원 :', a1.ndim,a1.ndim)
print(' 모양 : ', a1.shape, a2.shape) # shape 현재의 모양을 알려준다

print()
print('1-4) 행렬의 모양 변경')
na = np.array(range(10))
print(na, '길이 :', len(na))
nb = na.reshape(2, 5) # reshape 현재의 모양을 내가원하는 모양으로 알려준다, 원래의 모양을 변형시키지 않는다
print('reshape적용완료!!')
print(nb)

# 2. 행렬 데이터의 선택
a3 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,np.NaN]]])
print('2) 행렬 데이터의 선택')
print(a3)

# 1) 데이터의 선택
print()
print('a3[1] :\n', a3[1])
print('\na3[1][0] :\n ', a3[1][0])
print('\na3[1][0][2] : \n', a3[1][0][2]) # 9.0

# 2) []의 생략이 가능
print('a3[1,0,2] : \n', a3[1,0,2])

# 3) 범위로 선택 가능
print('\na3[1:,:,:2] :\n', a3[1:,:,:2])
print('\na3[1:,:,1:] :\n', a3[1:,:,1:])

# 4) 데이터 수정
print()
print('데이터 수정')
a1 = np.array(range(5))
a1[2] = 0
print(a1)

# 5) 브로드캐스팅 수정
print()
print('브로드캐스팅 수정')
a1 = np.array(range(5))
# a1[1::2] = 0
a1[3:] = 0
print(a1)

# 3. 행렬의 생성 2
print()
print('3. 행렬의 생성 2')
print('3-1) zeros')
zero = np.zeros((2,3))
print('np.zeros((2,3)) : \n', zero)

print()
print('3-2) ones')
ones = np.ones((4,3), dtype=int)
print('np.ones((4,3), dtype=int) : \n', ones)

"""
Quiz 1
numpy를 사용하여 5개의 1로 이루어진 정수타입의 1차원 행렬(벡터)를 만드시오.
q1이라는 변수에 [1 1 1 1 1]을 넣으시오
"""

print()
print("-----Quiz1-----")
q1 = np.ones(5, dtype = int)
# q1 = np.ones((1,5), dtype = int)[0]
print(q1)

"""
Quize 2 
10개의 1로 만들어진 정수 데이터 타입의 벡터에서 마지막 5개는 5로 바꾸시오
q2 = [1 1 1 1 1 5 5 5 5 5]
"""
print()
print('-----Quiz 2-----')
q2 = np.ones(10, dtype=int)
q2[5:] = 5
print(q2)

# 4. arange 만들기
print()
print('4. arange')
ar1 = np.arange(10)
ar2 = np.array(range(10)) # 위와 아래가 다를바가 없다
print(ar1, ar2)
ar3 = np.arange(5, 10, 2)
print(ar3)

# 5. linspace, logspace
print()
e51 = np.linspace(0, 100, 5, dtype= int)
print(e51)
e52 = np.logspace(1, 2, 5)
print(e52)

"""
Quiz 3
numpy를 사용하여 1에서 10까지의 홀수 데이터를 갖는 벡터를 만드시오
"""
print()
print('-----Quiz 3-----')
q3 = np.arange(1, 10, 2)
print(q3)

"""
Quiz 4
0 부터 8까지의 값을 갖는 3x3 행렬을 만드시오.
"""
print()
print('-----Quiz 4-----')
q4 = np.arange(9)
q4= q4.reshape(3,3)
print(q4)

# 6. Random
print()
print('4. Random')
print('1) seed')
np.random.seed(1)
result1 = np.random.randint(low=10, high = 100, size = 10)
print(result1)
np.random.seed(1)
result2 = np.random.randint(low=10, high = 100, size = 10)
result3 = np.random.randint(low=10, high = 100, size = 10)
np.random.seed(1)
result4 = np.random.randint(low=10, high = 100, size = 10)
print(result2)
print(result3)
print(result4)

print()
print('2) rand')
rd = np.random.rand(10)
print(rd)
print()

print('3) rnadn')

rd = np.random.randn(100)
print(rd)
print()

print('4) randint')
rd = np.random.randint(5, 10, (2,3))
print(rd)
rd = np.random.randint(5, size=(4,3)) # 두번쨰 들어갈 자리에 이상한것이 들어가기 때문에 size 라는것을 명시 해주어야 한다.
print(rd)
print()

print('5) shuffle')
np.random.seed(0) # seed 무효화
rd = np.random.randint(1, 10, (3,4))
print(rd)
np.random.shuffle(rd)
print(rd)
print()

# 전체를 섞는 방법
print('전체를 섞는 방법')
rd = np.random.randint(1, 10, (3,4))
print(rd)
print()
# 모든 차원의 데이터를 섞을 때에는 1차원으로 변경 후 shuffle, 원 모습으로 복귀

# 1차원으로 변경
rd_1 = rd.reshape(rd.size)
print('1차원으로 변경 :', rd_1)
print()

# shuffle
np.random.shuffle(rd_1)
print('Shuffle : ', rd_1 )
print()

# 원래 차원으로 복귀
result = rd_1.reshape(rd.shape)
print('원 모습으로 복귀 : \n', result)
print()
# choice
print('6) choice')
c = np.random.choice(5, 10, p = [0, 0.4, 0.4, 0.2, 0])
print(c)





