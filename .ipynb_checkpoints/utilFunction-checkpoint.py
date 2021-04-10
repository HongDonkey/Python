def utilFunction(inValue):

    # step1 : 입력받은 데이터를 반올림 자리수만큼 곱해준다
    # 함수를 개발하기 위한 디버깅코드
    step1 = inValue * 100

    step2= int(step1 + 0.5)

    outValue=step2/100
    
    return outValue