# demoSet.py
a = {1,2,3,3}
b = {3,4,5,5}
print(a, b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# 리스트
colors = ["red","blue","green"]
for i in colors:
    print(i)

print (dir())

# 튜플
tp = (1,2,3)
print(len(tp))
print(tp[0])
print(tp.count(2))

# 함수에서 한 개 이상 리턴
def times(a,b):
    return a+b, a-b


print(times(3,5))
print(type(times(3,5)))



args = (3,4)
print(times(*args))

color_fruits = {"apple" : "red", "banana" : "yellow"}
for k,v in color_fruits.items():
    print(k,v)


