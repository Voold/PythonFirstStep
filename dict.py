dict1 = {4:"Russia", 2:3, "seven":23}
# country = {'code':"RU", 'name':'Russia', 'population':144}
country = dict(code="RU", name="Russia", population = 144)

print(country['code'])
print(country)
print(country.items()) #Каждый элемент - кортеж с ключем и содержимым
print(*country)

for key in country: print(key)
for key, value in country.items(): print(key, value)


print(country["code"])
print(country.get("code"))

# country.clear()

print(country)
# country.pop("name")
country.popitem() #Последний элемент
print(country)


print(country.keys())
print(country.values())
print(country.items())

country.update([("reg",42),("lang_count",190)])
print(country)

person ={
    'user_1':{
        'first_name':'Voold',
        'second_name':'Kostromskoj',
        'age':45,
        'address':['Moscow','Street of Pushkin','kolotushkina'],
        'grades':{'math':5,'physics':5}
    }
}

print(person['user_1']['grades']['math'])
print(person['user_1']['age'])
print(person['user_1']['address'][1])