class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name=None, age=None, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.get_data()

    def set_data(self, name=None, age=None, isHappy=None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print("Name is:", self.name, "\nAge is:", self.age, "\nisHappy:", self.isHappy)


cat1 = Cat("Jopen", 2, False)

# cat1.name = "Barsik"
# cat1.age = 3
# cat1.isHappy = True

cat2 = Cat("Jopen", 2, False)

# cat2.name = "Jopen"
# cat2.age = 2
# cat2.isHappy = False

cat1.get_data()
print("\n")
cat2.get_data()

cat1.set_data()
cat1.get_data()
