# demoDict.py
from gettext import install
from tarfile import PAX_NAME_FIELDS


print("id : %s, name : %s" % ("kim", "김유신"))


def times(a,b):
    return a+b, a-b

args = (3,4)
print(times(*args))

# 딕셔너리 초기화
device = {"아이폰" : 5, "아이패드" : 10, "윈도우타블렛" : 20}
print(device["아이폰"])

# 추가
device["맥북"] = 30
print(device)

# 삭제
del device["아이폰"]
# 수정
device["아이패드"] = 12
print (device)

for item in device.items():
    print(item)

print("--- 각각 받기 ---")
for k,v in device.items():
    print(k,v)


tp = (1,2,3)
lst = list(tp)
lst.append(4)
print(lst, tp)

phone = {"kim" : 111, "lee" : 222, "park" : 333}
print("kim" in phone)
print("monn" not in phone)

p = phone
p["moon"] = 1234
print(p)
print(phone)
print(id(phone))
print(id(p))
print("\n\n")
print("------논리식--------")
print(1 < 2)
print(1 == 2)
print(1 != 2)
print(True and True and True)
print(True and True and False)
print(True or False or False)
print(id(phone) == id(p))
print(bool(0))