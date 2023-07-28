# demoLoop.py

value = 5
while value > 0:
    print(value)
    value -= 1

# 시퀀스형식은 for in을 사용

for i in range (1, 11):
    print(i)

d = {"apple":100, "orange":200, "kiwi":300}

for k,v in d.items():
    print(k,v)

for i in range(2,7):
    print("--{0}단--")
    for j in range(1,10):
        print("{0} * {1} = {2}".format(i,j,i*j))

for i in range(0,10):
    print("*"*i)

print("---break---")
for i in range(1,11):
    if i > 5:
        break
    print("item:{0}".format(i))

print("---continue---")
for i in range(1,11):
    if i % 2 == 1:
        continue
    print("item:{0}".format(i))

lst = list(range(1,11))
print([i**2 for i in lst if i > 5])

tp = ("apple", "orange", "kiwi")
print( [len(i) for i in tp])
d = {100:"apple", 200:"kiwi"}
print( [v.upper() for v in d.values()])

print("--필터링없음--")
def getBiggerThan20(i):
    return i > 20

lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("--필터링--")
lst = [10,25,30]
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

