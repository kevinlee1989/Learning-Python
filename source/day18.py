"""
    Day18 -  Pandas
    Version : 1.0
    Created : 2022.06.30
    Updated : 2022.06.30
    Author : J.W.Lee
"""
import pandas as pd
from myutils import*
import numpy as np

cprintTitle('1. Series')
# 1.스칼라(Scalar) 데이터
s = pd.Series([1.0, 3.0, 5.0, 7.0, 9.0]) # enumerate 함수와 동일하게 숫자를 붙혀준다.
print(s)
print(type(s))
print()
s1 = pd.Series(7, index=['이','재','우'])
print(s1)
print()

# 2. 1차원 배열 데이터
s2 = pd.Series(np.random.randn(5))
print(s2)
print()
s3 = pd.Series(np.random.randn(5), index=['jan','feb','mar','apr','may']) # 인덱스랑 갯수와 match를 해야한다.
print(s3)
print()

# 3. 리스트 데이터
s4 = pd.Series([1,2,3,4,5], index=['이','재','우','천','재'])
print(s4)
print()

# 4. 딕셔너리 데이터
s5 = pd.Series({'a':0,'subject':2345,'score':6789})
print(s5)
print()

#5. range 데이터
s6 = pd.Series(range(10), index=range(9,19,1))
print(s6)

cprintTitle('2.date_range')
# 1. start와 end를 지정해서 날짜 생성
date1 = pd.date_range(start='2022-06-30', end='2022-7-10')
print('2-1)', date1); print(); print()

# 2. start와 periods를 지정해서 날짜 생성
date2 = pd.date_range(start='2022-06-30', periods=7)
print('2-2)', date2); print(); print()

# 3. 2일씩 증가하는 날짜 데이터 생성
date3 = pd.date_range(start='2023-01-01', periods=10, freq = '2D')
print(date3, end = '\n\n\n')

# 4. 1시간 주기로 10시간 생성
date4 = pd.date_range(start='2022-06-30 08:00', periods=10, freq='1H')
print(date4, end='\n\n\n')

# 5. 30분 단위로 4개 시간을 생성
date5 = pd.date_range(start='2022-06-30 10:00', periods=4 , freq='30MIN')
print(date5,end='\n\n\n')

# 6. 10초 단위로 4개 시간을 생성
date6 = pd.date_range(start='2022-06-30 10:00:00', periods=4, freq = '10S')
print(date6, end='\n\n\n')

cprintTitle('3. DataFrame')
#1. numpy의 2차원 배열 데이터 사용
data1 = np.array([[10,20,30],[40,50,60]])
print('데이터의 행과 열은 : ' , data1.shape)
df1 = pd.DataFrame(data1)
print('3-1) \n ',df1, end = '\n\n\n')

# 2. index와 column을 지정된 날짜와 문자로 출력 **
data2 = np.array([[10,20,20],[0,0,5],[5,10,15]])
index_date = pd.date_range('2022-06-01', periods=3)
col_list = ['python', 'C', 'Java']
df2 = pd.DataFrame(data2, index=index_date, columns=col_list)
print('3-2) \n', df2, end = '\n\n\n')

# 3. 어느 회사의 연도 및 지사별 고객수 데이터
# 데이터를 딕셔너리로 만들어보자
table_data = {'연도':[2020, 2021, 2021, 2022, 2022],
              '지사':['kor','kor','usa','jap','aus'],
              '고객수':[200, 250, 450, 300, 500]
              }
df3 = pd.DataFrame(table_data)
print(df3); print()
print(df3.index)
print(df3.values) # 데이터 값 가져오기
print()

cprintTitle('4. Key')
# 데이터 프레임 생성
table_data = {'weight':[80, 70, 65, 46, 51],
              'height':[50, 30, 80, 45 ,50],
              'type':['f','s','f','o','o']
              }
df4 = pd.DataFrame(table_data)
print(df4); print()
print(df4[['weight']], end = '\n\n') # weight 데이터 목록만 추출.
print(df4[['weight','height']]) # weight 와 height 데이터 목록 추출


cprintTitle('5. Slice')
table_data = {'weight':[80, 70, 65, 46, 51],
              'height':[50, 30, 80, 45 ,50],
              'type':['f','s','f','o','o']
              }
df5 = pd.DataFrame(table_data)
print(df5); print()
# Printing only 2,3 data
print(df5[2:4]) # 값이 하나만 들어가면 무조건 column에서 찾고 값이 범위로 들어가면 index에서 찾는다
# Printing after third data
print(df5[3:])

cprintTitle('6. Filter')
table_data = {'weight':[80, 70, 65, 46, 51],
              'height':[50, 30, 80, 45 ,50],
              'type':['f','s','f','o','o']
              }
df6 = pd.DataFrame(table_data)
print(df6); print()
# Extract height only above 50
print(df6[df6.height >= 50])
print()
# Extract type only equal to o
print(df6[df6.type == 'o'])
print()
# height가 50이상이면서 type이 o인것만 추출
# 여러 개의 조건이 걸렸을 때는 하나씩 처리
df7 = df6[df6.height >= 50]
print(df7[df7.type == 'o'])
print()

cprintTitle('7. Sort')
table_data = {'weight':[80, 70, 65, 46, 51],
              'height':[50, 30, 80, 45 ,50],
              'type':['f','s','f','o','o']
              }
df7 = pd.DataFrame(table_data)
print(df7); print()

# height로 오름차순
print(df7.sort_values(by='height'))
# weight로 내림차순
print(df7.sort_values(by='weight', ascending=False))
print()

cprintTitle('8. Rot')
table_data = [['A','B','C'],['D','E','F'],['G','H','I']]
df8 = pd.DataFrame(table_data)
print(df8)
print('행렬이 뒤집혔네?? :')
print(df8.T)





































