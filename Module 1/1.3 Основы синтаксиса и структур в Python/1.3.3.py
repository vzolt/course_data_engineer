# Перевод арабского числа в римское
n = int(input("Введите натуральное число от 1 до 2000: "))

roman_num = ''
if n == 2000:
    roman_num = 'MM'
    n = 0

if n >= 1000:
    roman_num = 'M'
    n -= 1000

if n >= 100:
    k = n // 100
    
    if k == 1:
        roman_num += 'С'
    elif k == 2:
        roman_num += 'СC'
    elif k == 3:
        roman_num += 'СCC'
    elif k == 4:
        roman_num += 'СD'
    elif k == 5:
        roman_num += 'D'
    elif k == 6:
        roman_num += 'DC'
    elif k == 7:
        roman_num += 'DCC'
    elif k == 8:
        roman_num += 'DCCC'
    elif k == 9:
        roman_num += 'CM'

    n = n - 100 * k

if n >= 10:
    k = n // 10
    if k == 1:
        roman_num += 'X'
    elif k == 2:
        roman_num += 'XX'
    elif k == 3:
        roman_num += 'XXX'
    elif k == 4:
        roman_num += 'XL'
    elif k == 5:
        roman_num += 'L'
    elif k == 6:
        roman_num += 'LX'
    elif k == 7:
        roman_num += 'LXX'
    elif k == 8:
        roman_num += 'LXXX'
    elif k == 9:
        roman_num += 'XC'

    n = n - 10 * k

if n == 1:
    roman_num += 'I'
elif n == 2:
    roman_num += 'II'
elif n == 3:
    roman_num += 'III'
elif n == 4:
    roman_num += 'IV'
elif n == 5:
    roman_num += 'V'
elif n == 6:
    roman_num += 'VI'
elif n == 7:
    roman_num += 'VII'
elif n == 8:
    roman_num += 'VIII'
elif n == 9:
    roman_num += 'IX'

print(roman_num)
