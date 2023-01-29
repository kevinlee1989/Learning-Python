import pandas as pd
import numpy as np

print('Pandas Basic Challenge')

KTX_data = {'경부선':[12345,34536,45636,54534,534523,67876,23678],
            '호남선':[1256,3765,3875,7453,8567,3476,9654],
            '경전선':[4536,4734,7535,2856,2486,2475,8434],
            '동해선':[np.nan,np.nan,np.nan,np.nan,4634,2352,6789]
            }
col_list = ['경부선','호남선','경전선','동해선']
index_list = ['2011','2012','2013','2014','2015','2016','2017']
df_KTX = pd.DataFrame(KTX_data, index = index_list, columns= col_list)
# 1. df_KTX 출력
print(df_KTX)
print()
# 2. df_KTX의 인덱스 출력
print(df_KTX.index)
print()
# 3. df_KTX의 컬럼 출력
print(df_KTX.columns)
print()
# 4. df_KTX의 데이터 출력
print(df_KTX.values)
print()

# 5. 첫 n개행 출력
print(df_KTX.head()) # head에 아무것도 안주게되면 첫 5줄을 출력하게된다
print(df_KTX.head(3)) # head안에 숫자 줄 만큼 출력하게 된다.
print()

# 6. 마지막 n개행 출력
print(df_KTX.tail()) # tail안에 아무것도 안주게되면 마지막 5줄을 출력하게된다.
print()

# 7. 1번행 데이터 출력
print(df_KTX[0:1])
print()

# 8. 2~4번행 데이터 출력
print(df_KTX[1:4])
print()

# 9. 2011년 데이터 출력
print(df_KTX.loc['2011'])
print()

# 10. 2013년부터 2016년 까지의 데이터 출력
print(df_KTX.loc['2013':'2016']) # loc 함수일경우 뒤에 index까지 나오게된다
print()

# 11. 경전선 데이터 출력
print(df_KTX[['경전선']])
print()

# 12. 경부선 and 동해선 데이터 출력
print(df_KTX[['경부선','동해선']])
print()








