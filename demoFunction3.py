# demoFunction3.py
# 가변인자(내부에서 tuple로 받기)
def union(*ar):
    # 지역변수에 글자 모아두기
    result = []
    # HAM(0) | EGG(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            if x not in result:
                result.append(x)
    return result
# 호출
print( union("HAM", "EGG"))
print( union("HAM", "EGG", "SPAM"))

# 정의되지 않은 인자처리
def userUriBuilder(server, port, **user):
    strUrl = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strUrl += key + "=" + user[key] + "&"
    return strUrl

print(userUriBuilder("localhost", "8080", id="kim"))
print(userUriBuilder("localhost", "8080", id="kim", name = "python"))

#람다 함수
g = lambda x,y:x*y
print (g(3,4))
print (g(5,6))
print ((lambda x:x*x)(3))
print( globals())

print("--필터링--")
lst = [10,25,30]
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)