class House:
    """
    My house Class : valuable
    """
    def welcome(self):
        print('Welcome to my House')

    house_count = 0 # 모든 객체가 갖는 변수, 클래스 변수
    def __init__(self, name):
        print('Instance OK')
        self.name = name # 객체마다 다른 변수, 객체변수
        House.house_count += 1


    def __init__(self, name = 'noname'):
        print('Instance OK')
        self.name = 'noname' # 객체마다 다른 변수, 객체변수
        House.house_count += 1

    def data_process(self, data):
        print(type(data))

class Apart:
    def __init__(self):
        print('새로운 아파트가 생성되었습니다')
        self.room = 3
        self.furniture = []


    def set_room(self, i):
        self.room = i

    def get_room(self):
        return self.room

    def add_furniture(self, str):
        #self.furniture 에 str 추가
        self.furniture.append(str)

    def show_furniture(self):
        print(self.furniture)

class MyException(Exception): # Exception 을 상속받은 것이다.
    # log를 기록한다.
    # 예외시스템으로 전송한다 ....
    pass