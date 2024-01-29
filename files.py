# data = input('Введите текст: ')
#
#
# file = open("data/text.txt", 'a')
#
# file.write(data+'\n')
#
# file.close()

file = open('data/text.txt','r')

# print(file.read(20))
# print(file.read())

for line in file:
    print(line, end='')

file.close()