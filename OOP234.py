import Building


class School(Building):
    pupils = 0

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils


class House(Building):
    pass


class Shop(Building):
    pass
