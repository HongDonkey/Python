# demoStr.py

# 파일에 저장
f = open("c:\\work\\customer.txt","wt",encoding="utf-8")
names = ["이순신", "박문수","전우치"]
for name in names:
    f.write("안녕하세요 {0}님 \n".format(name))
    f.write("="*40 + "\n")