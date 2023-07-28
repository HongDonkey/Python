# demoStr2.py
strA = "python is very powerful"
print(len(strA))
print(strA.capitalize())
print(strA.startswith("python"))
print(strA.endswith("ful"))
print(strA.upper())
print("MBC2580".isalnum())
print("MBC2580".isdecimal())
print("2580".isdecimal())

u = "<<<spam and ham"
result = u.strip("<<<")
print(u)
print(result)

result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print(":)".join(lst))


