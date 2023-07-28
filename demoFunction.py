# demoFunction.py
def setValue(newValue):
    x = newValue
    print("함수내부: " , x)

# 호출
retValue = setValue(5)
print(retValue)

# 함수정의
def swap(x, y):
    return y,x


# 호출
print(swap(3,4))

#LGB(Local, Global, BuiltIn)
x = 10
def func(a):
    return x + a

# 호출
print(func(1))

def func2(a):
    x = 5
    return x + a

# 호출
print(func2(1))

print("--불변형식--")
a = 1.2
print( id(a))
a = 2.3
print( id(a))

print("--가변형식--")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))