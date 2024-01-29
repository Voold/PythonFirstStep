#CONST ARRAY - меньше памяти

data = (1, 2, 3, 4, 5, 6, True, 5.6, "Hello")
data1 = 1, 2, 3, 4, 5, 6, True, 5.6, "Hello"

print(data[0])
print(data[:5])
print(data.count(5))
print(len(data))

print(data)
print(*data)

for el in data: print(el,end=' ')

nums=[2,6,3]
nums = tuple(nums)
print("\n")
print(tuple("Hello"))