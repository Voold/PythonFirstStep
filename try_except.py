try:
    x = int(input("Введите число: "))
    print(5//x)
except ValueError:
    print('ОШипка 1')
except ZeroDivisionError:
    print('оШипка 2')
else:
    print('Если нет except\`ov')
finally:
    print('finally')