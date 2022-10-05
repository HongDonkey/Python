# demoFunction2.py

# 교집합 글자 리턴
from ssl import OP_NO_RENEGOTIATION


def intersect(prelist, postlist):
    # 지역변수
    result = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

# 호출
print( intersect("HAM", "SPAM"))

# 가변형식
def change(x):
    x[0] = "H"

wordlist = ["J", "A", "M"]
change(wordlist)
print("함수 호출 후 : " , wordlist)


print("--코드 수정--")
orignal = []
def change(x):
# 복사본 생성
    global orignal
    orignal = x[:]
    x[0] = "H"
    print("함수 내부 : ", orignal)
    
# 호출    
wordlist = ["J", "A", "M"]
change(wordlist)
print("함수 호출 후 : " , wordlist)
print(orignal)


g = 1
def testScope(a):
    global g
    g = 3 
    return a+g

print(testScope(1))
print("전역변수 g : ", g)

def times(a=10, b=20):
    return a+b

# 호출
print(times())
print(times(5))
print(times(5,6))
print(times(b=6))

def connectUri(server, port):
    strUrl = "http://" + server + ":" + port
    return strUrl

print(connectUri("localhost", "8080"))
print(connectUri(port = "5432", server = "postresql.com"))

