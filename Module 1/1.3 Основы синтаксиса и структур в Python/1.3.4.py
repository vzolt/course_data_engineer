# Валидность скобок
txt = input("Введите строку: ")

s1, s2, s3 = 0, 0, 0

for i in range(0, len(txt)):
    if s1 < 0 or s2 < 0 or s3 < 0:
        break
    if txt[i] == '[':
        s1 += 1
    if txt[i] == '(':
        s2 += 1
    if txt[i] == '{':
        s3 += 1
    if txt[i] == ']':
        s1 -= 1
    if txt[i] == ')':
        s2 -= 1
    if txt[i] == '}':
        s3 -= 1


if s1 == 0 and s2 == 0 and s3 == 0:
    print('True')
else:
    print('False')
