class Building:
    year = None
    city = None

    def __init__(self, year=None, city=None):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year:", self.year, " city:", self.city)


class School(Building):
    pupils = 0

    def __init__(self, pupils=None, year=None, city=None):
        super(School, self).__init__(year, city)
        self.pupils = pupils

    def get_info(self):
        super(School,self).get_info()
        print("Pupils is:", self.pupils) #Или сделать ретерн от супера и к строке итога добавить этот вывод


class House(Building):
    pass


class Shop(Building):
    pass
