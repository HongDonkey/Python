# demoCopy.py
# 얕은 복사
from re import A


a = [1,2,3]
b = a
a[0] = 38
print(a)
print(b)
print(id(a) == id(b))

# 깊은 복사
a = [1,2,3]
b = a[:]
a[0] = 38
print(a)
print(b)
print(id(a) == id(b))

import copy
a = [100,200,300]
b = copy.deepcopy(a)
a[0] = 101
print(a)
print(b)
print(id(a) == id(b))


lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))


print(type('c'))