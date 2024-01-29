word = 'string'
print(word[0])
print(len(word))
print(word.count('r'))

print(word.upper())
print(word.isupper())
print(word.lower())
print(word.islower())
print(word.capitalize())

print('\'r\' index is',word.find('r'))

words = 'one,two,apple'

print(words.split(','))

hobby = words.split(',')

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)

result = ", ".join(hobby)
print(result)

burbur = "Football"

print(burbur[0:4])
print(burbur[4:])
print(burbur[-1:])
print(burbur[1:-1:1])
print(burbur[1:-1:2])

lis = [6, 4, "Stroka", True, 6.5]
print(lis[0:-1])
print(lis[::])
print(lis[::-1])