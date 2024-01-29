# try:
#     file = open('text.txt','r')
#     file.read()
#     file.close
# except FileNotFoundError:
#     print("Файл не найден")
# finally:
#     file.close() Ошибка, т.к. переменная локальна

try:
    with open('text.txt','r',encoding="utf-8") as file:
        print(file.read())
        for line in file: print(line)
except FileNotFoundError:
    print("Файл не найден")