# i = int(input("Enter the number: "))
#
# if i == 5: print("Hello"); print(12)
# elif i == 7: print("Hello, Voold")
# else: print("Hello, Bro")
#
# if i == 5:
#     print("Yes, it`s 5")
#
# data = input()
#
# number = 5 if data == "five" else 0
#
# if data == "five":
#     number = 5
# else:
#     number =0

q = [i for i in range(1,11)]

for i in range(6):
    print(i);

print(*q,sep=" ")

word = "hello"

count= 0

for i in word:
    if i == "l": count+=1

print("Count is: ", count)


i = 2

while i<15:
    print(i)
    i+=1


