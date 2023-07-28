# demoFile.py
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close()

# 파일 읽기
f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
print(f.read()) # 전체 파일 내용 읽어오기
print(f.tell()) # 파일 포인터의 값 리턴
f.seek(0) # 파일 포인터를 0으로 이동
print(f.readline(),end="")
print(f.readline(),end="") # print는 기본적으로 줄바꿈이 되어있으므로 end에 ""값을 줌으로써 줄이 바뀌지 않게 설정
f.seek(0)
result = f.readlines() # 줄을 나누어서 리스트로 반환
print(result)

for item in result:
    # print(item, end="")
    print(item.replace("\n", ""))
f.close()

# 기존 파일에 첨부하는 경우
f = open("c:\\work\\test.txt", "wt", encoding="utf-8")
f.write("다른 데이터\n")

f = open("c:\\work\\test.txt", "rt", encoding="utf-8")
print(f.read())
f.close() 

