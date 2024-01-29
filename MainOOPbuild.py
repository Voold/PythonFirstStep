import Building
from Building import School as Sc, House as Hs, Shop as Sh
# import OOP234

school = Sc(100, 1997, 'Moscow')
house = Hs(1999, 'Moscow')
shop = Sh(1994, 'Moscow')
school1 = Sc()
school2 = Sc(None,1980)
school3 = Sc(None,None,"Moscow")

school.get_info()
school1.get_info()
school2.get_info()
school3.get_info()
