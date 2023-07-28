# demoClass.py
class Person:
    # 초기화 메서드
    def __init__(self):
        self.name = "default name"
    # 인스턴스 메서드
    def printout(self):
        print("My name us {0}".format(self.name))
# 인스턴스 생성    
p1 = Person()
p2 = Person()
p1.name = "전우치"

p1.printout()
p2.printout()