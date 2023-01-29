import random as rd
import numpy as np

def get_name():
    names = ['이재우', '황연준', '김준호', '박지훈', '임정현', '홍기준', '김석현',
            '이재현','김용원','강세빈','정영환']
    return rd.choice(names)

def get_age(start = 20, end = 40):
    return np.random.randint(start, end)

def make_data(rows = 10):
    datas = []
    for i in range(rows):
        data = {'나이': get_age(), 'Name':get_name()}
        datas.append(data)
    return datas

# for test

