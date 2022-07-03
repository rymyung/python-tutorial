class SelfTest:

    # 클래스 변수
    name = 'aaa'

    def __init__(self, x):
        self.x = x

    # 클래스 메서드
    @classmethod
    def func1(cls):
        print(f'cls : {cls}')
        print('func1')

    # 인스턴스 메서드
    def func2(self):
        print(f'self : {self}')
        print('class 안의 self 주소: ', id(self))
        print('func2')


test_obj = SelfTest(17)
test_obj.func2()
SelfTest.func1()
print('인스턴스 주소: ', id(test_obj))

'''
[출력 결과]
self : <__main__.SelfTest object at 0x103e26680>
class 안의 self 주소:  4360136320
func2
cls : <class '__main__.SelfTest'>
func1
인스턴스 주소:  4360136320

# [self의 이해]
# ** self는 인스턴스 객체이다!!
# ** 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다! 즉, self는 인스턴스 그 자체이다!
'''
