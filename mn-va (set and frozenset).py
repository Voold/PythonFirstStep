data = set("hello")
print(data)

data = {5,6,3,5,3}
print(data)

data.add(23)

data.update([True, "lol", 2, 7, 8 ,4])
print(data)
data.remove(True)
print(data)
data.pop()
print(data)
data.clear()

nums=[5,7,3,5,5]
nums=set(nums)
print(nums)

new_data = frozenset([5,6,3,5,3,True, "lol", 2, 7, 8 ,4]) #св-ва картежей
print(new_data)
print(*new_data)
