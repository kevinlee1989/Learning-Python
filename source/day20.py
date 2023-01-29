# """
#     Day20 -  tkinter
#     Version : 1.0
#     Created : 2022.07.01
#     Updated : 2022.07.01
#     Author : J.W.Lee
# """
#
# from tkinter import*
# from maps import*
# def search_hospital(arg=None):
#     print('Search Hospital Begin')
#     sido_cd = entry1.get()
#     list_cd = listbox.curselection()[0]
#     label2.config(text=sido_cd + ':' + str(list_cd))
#     if sido_cd == '':
#         label2.config(text='입력할 건 하셔야죠')
#     else:
#         if list_cd == 0:
#             find_hospital(sido_cd, '상급종합')
#         elif list_cd == 1:
#             find_hospital(sido_cd, '종합병원')
#         elif list_cd ==2:
#             find_hospital(sido_cd, "병원")
#
#
#
#
#
#
# root = Tk()
#
# label1 = Label(root, text='Find Hospital')
# label1.pack()
#
# entry1 = Entry(root, width=20)
# entry2 = Entry(root, width=20)
# entry1.pack()
# entry2.pack()
#
# listbox = Listbox(root, selectmode='single',height=0) #selectmode extended는 여러 개 선택가능
# listbox.insert(0, "상급종합")
# listbox.insert(1, "종합병원")
# listbox.insert(2, "병원")
# listbox.pack()
#
# label2 = Label(root, text='log area')
# label2.pack()
#
# # inserting button
# button1 = Button(root, text='Search', fg='#000000', bg='#FF00FF', command=search_hospital) #fg는 글자의 색깔, #000000 은 검은색
# button1.pack()
#
#
# root.title('병원찾') # titling
# root.geometry('300x150') # scaling the window기
# root.mainloop()
import random

print('안녕하세여')

for x in range(0,3):
    lunch = random.choice(["된장","김치","제육"])
    print(lunch)

