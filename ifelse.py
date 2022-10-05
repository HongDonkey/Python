# ifelse.py
score = int(input("점수입력 : "))

if 90 <= score :
    grade  = "A"
elif score < 90 :
    grade = "B"
elif score < 80 :
    grade = "C"
else :
    grade = "D"

print("this grade : " + grade)
