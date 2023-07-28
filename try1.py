# try1.py
# 함수 정의
def divide(a,b):
    return a/b
#에러 처리
try:
    # 호출
    result = divide(5,2)
    
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except TypeError:
    print("정수끼리만 연산 가능합니다.")
else:
    print("결과 : {0}".format(result))
finally:
    print("코드 종료")