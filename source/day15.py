"""
    Day13 -  Data Visualization
    Version : 1.0
    Created : 2022.06.21
    Updated : 2022.06.21
    Author : J.W.Lee
"""
import matplotlib.pyplot as plt
from myutils import*

cprintTitle("MatPlotLib")

# figure = plt.figure()
# axis = figure.add_subplot(1,1,1)
# # plt.show()
#
# figure2 = plt.figure()
# axis11 = figure2.add_subplot(121) #add_subplot 는 단지 피규어를 몇등분을 해서 몇번째 자리인지를 결정해주는것이다.
# axis12 = figure2.add_subplot(122)
# axis13 = figure2.add_subplot(339)
# # axis14 = figure2.add_subplot(10101) # 오류 # 쉼표를 생략하는 문법을 사용하기 위해서는 행, 열, 번호가 다 한자리 수 여야만 가능하다.
# # plt.show()
#
# figure3 = plt.figure()
# axis31 = figure3.add_subplot(331)
# axis35 = figure3.add_subplot(335)
# axis39 = figure3.add_subplot(339)
# plt.show()
#

plt.rcParams['figure.figsize'] = (15,5) # 창의 크기 조절

# plot
figure = plt.figure()
axis = figure.add_subplot(1,6,1)
x = [0, 1, 2, 3, 4]
y = [4, 1, 3, 5, 2]
axis.plot(x,y, linestyle = 'dotted', linewidth = '10')
y2 = [0, 8, 5, 3, 1]
axis.plot(x, y2, color='y', marker = 'o')
# plt.show()

# 한글이 깨질 때 조치 방법
import matplotlib as mpl
path = 'C:/Windows/Fonts/HMFMPYUN.TTF'
name = mpl.font_manager.FontProperties(fname = path).get_name()
print(name)
mpl.rc('font', family = name)

axis = figure.add_subplot(1,6,2)
x = ['봄', '여름', '가을', '겨울']
y = [4, 1, 3, 5]
axis.plot(x,y)
# plt.show()

# bar
axis = figure.add_subplot(1,6,3)
axis.bar(x, y)
plt.title('계절별분포')
plt.xlabel('계절')
plt.ylabel('분포')
# plt.show()

# scatter (산포도)
axis = figure.add_subplot(1,6,4)
x = [range(1,7)]
y = [6, 4, 1, 2, 7, 5]
size = [50, 100, 150, 600, 250, 300]
color = ['red', 'yellow', 'green', 'blue', 'orange', 'aqua']
axis.scatter(x, y, s= size, c = color) # s 는 size, c 는 color
# plt.show()

# pie
axis = figure.add_subplot(1,3,3)
data = [1, 2, 3, 4, 5, 6]
label = ['사과','귤','바나나','수박','참외','사발면']

axis.pie(data, labels = label, autopct = '% 0.1f%%') # autopct 데이터를 어떻게 표현할것인지 해준다
plt.axis('equal') # 가로세로축이 맞춰진다.
plt.legend(label, loc = 'center right')
# plt.show()


# seaborn
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="dark")

# Simulate data from a bivariate Gaussian
n = 10000
mean = [0, 0]
cov = [(2, .4), (.4, .2)]
rng = np.random.RandomState(0)
x, y = rng.multivariate_normal(mean, cov, n).T

# Draw a combo histogram and scatterplot with density contours
f, ax = plt.subplots(figsize=(6, 6))
sns.scatterplot(x=x, y=y, s=5, color=".15")
sns.histplot(x=x, y=y, bins=50, pthresh=.1, cmap="mako")
sns.kdeplot(x=x, y=y, levels=5, color="w", linewidths=1)

plt.show()

# Plotly
import plotly.express as px
df = px.data.tips()
fig = px.histogram(df, x="total_bill", y="tip", color="sex", marginal="rug",
                   hover_data=df.columns)
fig.show()


# pydeck
import pydeck as pdk

# 2014 locations of car accidents in the UK
UK_ACCIDENTS_DATA = ('https://raw.githubusercontent.com/uber-common/'
                     'deck.gl-data/master/examples/3d-heatmap/heatmap-data.csv')

# Define a layer to display on a map
layer = pdk.Layer(
    'HexagonLayer',
    UK_ACCIDENTS_DATA,
    get_position=['lng', 'lat'],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
    coverage=1)

# Set the viewport location
view_state = pdk.ViewState(
    # longitude=-1.415,
    # latitude=52.2323,
    longitude=126.5841,
    latitude=37.3359,
    zoom=6,
    min_zoom=5,
    max_zoom=15,
    pitch=40.5,
    bearing=-27.36)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html('demo.html')