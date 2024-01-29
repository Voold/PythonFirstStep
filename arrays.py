arr1 = [1, "2", [2, True], 4.67]
arr2 = [0 for i in range(10)]

print(*arr2)
arr2.append(7)
print(*arr2)
arr2.insert(2, 7)
print(*arr2)
arr2.extend([1,2,3]);
print(*arr2)
arr2.sort()
print(*arr2)
arr2.reverse()
print(*arr2)
arr2.pop()
print(*arr2)
arr2.pop(1) #Удаляет индекс
print(*arr2)
arr2.remove(2) #Удаляет элемент
print(*arr2)
print("Count 0 is: ",arr2.count(0),sep="")
print("len arr2 is: ",len(arr2),sep="")
arr2.clear()
print(arr2)

nums = [5, 2, 7, "50", False]

for el in nums: print(el)
