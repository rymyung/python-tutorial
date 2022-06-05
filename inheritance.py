"""
[클래스 상속]

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩
4. super()
5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다.
6. class.mro() : 상속 관계를 보여준다.
"""


class Robot:

    '''
    [Robot Class]
    Author : xx
    Role : xx
    '''

    # 클래스 변수 : 인스턴스들이 공유하는 변수
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
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
    def how_many(cls):  # cls -> Robot
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


class Siri(Robot):

    # method overriding
    def __init__(self, name, age):
        super().__init__(name)  # 부모 클래스의 __init__() 실행
        self.age = age

    def call_me(self):
        print('Yes?')

    def cal_mul(self, a, b):
        return a * b

    def cal_new(self, a, b):
        super().say_hi()
        return self.cal_mul(a, b) + self.cal_add(a, b) + super().cal_add(a, b)

    @classmethod
    def hello_apple(cls):  # cls -> Siri
        print(f'{cls} hello apple!!')

    # method overriding
    def say_hi(self):
        print(f'Greetings, my masters call me {self.name}, by apple.')

    # method overriding
    @classmethod
    def how_many(cls):  # cls -> Robot
        print(f'We have {cls.population} robot by apple.')


siri = Siri('iphone8', 17)
print(siri.age)
print(siri.name)
siri.say_hi()
Siri.how_many()

print(siri.cal_new(5, 3))
