# палиндром строки

txt = input("Введите строку: ")
txt_without_spaces = txt.replace(" ", "")
if txt_without_spaces[::-1] == txt_without_spaces:
    print('true')
else:
    print('false')
