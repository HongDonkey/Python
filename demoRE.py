# demoRE.py
import re

result = re.search("[0-9]*th", "35th") #정수가 반복되고 뒤에 문자열'th'가 옴
print(result)
print(result.group())

result = re.match("[0-9]*th", "35th")
print(result)
print(result.group())

print(bool(re.search("ap","this is apple"))) # 'ap'가 포함되어 있다면 true
print(bool(re.match("ap","this is apple"))) # 'ap'와 일치한다면 true

result = re.search("\d{4}", "올해는 2022년입니다.") # 정수 4개를 search
print(result.group())


result = re.search("\d{5}", "우편번호는 93322년입니다.") # 정수 5개를 search
print(result.group())

