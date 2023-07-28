# demoClass.py
class Person:
    # 클래스 멤버 변수
    num_person = 0
    # 초기화 메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    # 인스턴스 메서드
    def printout(self):
        print("My name us {0}".format(self.name))
# 인스턴스 생성    
p1 = Person()
p2 = Person()

print("인스턴스 갯수 : {0}".format(Person.num_person))

# 런타임 시 변수 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)