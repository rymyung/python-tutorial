

class Robot:

    '''
    [Robot Class]
    Author : xx
    Role : xx
    '''

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        print(f'Greetings, my masters call me {self.name}')

    def cal_add(self, a, b):
        return a + b

    def die(self):
        print(f'{self.name} is being destoryed!')
        Robot.population -= 1
        if Robot.population == 0:
            print(f'{self.name} is the last one.')
        else:
            print(f'There are still {Robot.population} robots working.')

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f'We have {cls.population} robot.')

    @staticmethod
    def is_robot_class():
        print('yes!!')

    # magic method
    def __str__(self):
        return f'{self.name} robot!!'

    def __call__(self):
        print('call!!')
        return f'{self.name} call!!'


# print(Robot.population)  # 0
siri = Robot('siri', 29184853)
# print(Robot.population)  # 1
jarvis = Robot('jarvis', 20948455)
# print(Robot.population)  # 2
bixby = Robot('bixby', 49583732)
# print(Robot.population)  # 3

# Robot.how_many()

"""
#* namespace : 개체를 구분할 수 있는 범위
#* __dict__ : 네임스페이스를 확인할 수 있다.
#* dir() : 네임스페이스의 key 값을 확인할 수 있다.
#* __doc__ : class의 주석을 확인한다.
#* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
"""
'''
print(Robot.__dict__)
print(siri.__dict__)  # name, code만 존재

# 인스턴스의 namespace에 없어서 클래스에서 찾음
print(siri.population)
print(siri.how_many())

# Robot.say_hi() -> 에러 발생
Robot.say_hi(siri)

# 사용할 수 있는 목록 확인
print(dir(Robot))
print(dir(siri))

# magic method
print(Robot.__doc__)
print(siri.__class__)

# @staticmethod 미사용 시 인스턴스로 호출하면 에러 발생 (Robot.is_robot_class() 사용)
print(siri.is_robot_class())
'''

# __str__
print(siri)
print(siri.__str__())

# __call__
call_returned = siri()
print(call_returned)
