"""
    Day19 -  DATAFRAM(2)
    Version : 1.0
    Created : 2022.07.01
    Updated : 2022.07.01
    Author : J.W.Lee
"""



import makedata as md
import pandas as pd

print('10. append')
df1 = pd.DataFrame(md.make_data(5))
print(df1)
print()

df2 = pd.DataFrame(md.make_data(5))
print(df2)
print()

df3 = df1.append(df2)
print(df3)
print()

#print(df3[3:4])
# index를 새로 구성하여 추가
print(df3.reset_index(drop=True))     # df3 = df1.append(df2).reset_index(drop=True)
# append시에 바로 처리 가능
df3 = df1.append(df2, ignore_index=True)

print('11. concat')
df1 = pd.DataFrame(md.make_data(5))
print(df1)
df2 = pd.DataFrame(md.make_data(5))
print(df2)

# axis 설정을 따로 하지 않으면 row 기준으로 붙는다
df3 = pd.concat([df1,df2]).reset_index(drop=True)    #append 랑 똑같이 동작한다
print(df3)
# axis =1 설정으로 column 단위로 붙일 수 있다
# 기본적으로 데이터가 많은 쪽 기준으로 생성된다(부족한 쪽은 NaN)
df4 = pd.concat([df3, df1], axis=1).reset_index(drop=True)
print(df4)
print()

df5 = pd.concat([df3, df1], axis=1, join='inner').reset_index(drop=True)
print(df5)
print()

print('12. groupby')
g_df = pd.DataFrame(md.make_data())
print(g_df); print()
print('size()')
result_df = g_df.groupby('Name').size().reset_index(name='Counts')
print(result_df)

min_df = g_df.groupby('Name').agg('min').reset_index()
print(min_df); print()
max_df = g_df.groupby('Name').agg('max').reset_index()
print(max_df); print()
mean_df = g_df.groupby('Name').agg('mean').reset_index()
print(mean_df); print()
median_df = g_df.groupby('Name').agg('median').reset_index()
print(median_df); print()
sum_df = g_df.groupby('Name').agg('sum').reset_index()
print(sum_df); print()

# 한 방에 해결
print('한방에 해결')
df_end = g_df.groupby('Name').agg(['min','max','median','mean','sum']).reset_index()
print(df_end)
print()

print('13.select')

print(df_end[2:4]['나이']['mean'], end='\n\n')
print(df_end.loc[1]['Name'][''])

# column을 새롭게 지정
col_data = {
    'Name':df_end['Name'],
    'Min':df_end['나이']['min'],
    'Max':df_end['나이']['max'],
    'Sum':df_end['나이']['sum']
}
n_df = pd.DataFrame(col_data)
print(n_df);print()

print('rename column')
n_df2 = n_df.rename(columns={'Name': 'Author Name', 'Min': '최소'})
print(n_df2)

print('13. csv, excel')
# Excel Writing
n_df2.to_excel('day19.xlsx', sheet_name='19일차', engine='xlsxwriter', encoding='uft-8-sig')

# Excel Reading
e_df = pd.read_excel('day19.xlsx','19일차')
print(e_df); print()

# CSV Writing
n_df2.to_csv('day19.csv', index=False)

# CSV Reading
c_df = pd.read_csv('day19.csv')
print(c_df)


















