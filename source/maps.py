import folium
import pandas as pd
import webbrowser

def find_hospital(sido_cd ='서울',type_cd='상급종합'):
    df_init = pd.read_csv('1. 병원정보서비스 2022.3.csv', encoding='cp949')
    print(df_init.head(30))

    # 필요한 데이터만 별도 저장
    df_data = df_init[['요양기관명', '종별코드명', '시도코드명', '주소', '총의사수','x좌표','y좌표']]
    print(df_data.head(30))
    """
    df_data2 = df_data[df_data.시도코드명 == '서울']
    print(df_data2.head())
    df_data3 = df_data2[df_data2.종별코드명 == '상급종합']
    print(df_data3.head())
    """
    df_data2 = df_data[df_data.시도코드명 == sido_cd]
    df_data3 = df_data2[df_data2.종별코드명 == type_cd]

    # 지도 세팅
    default_location = df_data3.head(1)[['y좌표','x좌표']]
    #default_location = [37.5667, 126.9784] # 서울 대표 좌표
    default_zoom = 12
    hmap = folium.Map(location=default_location,
                      control_scale = True,
                      zoom_start=default_zoom)
    # 지도에 좌표찍기
    for ntp in df_data3.itertuples():
        hptl_name, typ_cd, sido_cd, addr, docnum, lng, lat = ntp[1:]

        iframe = hptl_name + '(' + str(docnum) + ')' + '<br>' + addr
        popup = folium.Popup(iframe, min_width=100, max_width=300)

        folium.Marker(location=[lat, lng],
                      tooltip=hptl_name,
                      popup=popup).add_to(hmap)




    # html에 저장
    hmap.save('hospital_info.html')

    #자동으로 web browser에 띄우기
    webbrowser.open('hospital_info.html')

"""
for macos
file_location = "file:///" + file_location
webbrowser.get().open(file_location, new=new)
"""





