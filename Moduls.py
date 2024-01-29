import time as tm
import datetime as dtm, sys, os, platform
from math import sqrt as s
from moduleSUP import add_three_numbers as ad
from moduleSUP import hello as h
import cowsay as c


# tm.sleep(3)

print("Hello")

print(dtm.datetime.now())
print(sys.path)
print(os.name)
print(platform.system())

print(s(100))

h()
print(ad(1,2,3))

c.cow("Hello")