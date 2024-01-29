def func(a):
    print("Hello")
    print("Hello,",a)

def pass_func():
    pass

def res(a,b):
    return a+b

pass_func()

func("Voold")
func("Voold")

print(res(1,2))


L_func = lambda x,y: x*y

res =L_func(5,2)

print(res)