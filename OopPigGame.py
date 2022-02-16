import sys

sys.path.append(".")
from PIGClasses import Player as p
from PIGClasses import Dice as d
k = p("rodri")
y = d()
print(y.roll())
print(k.getName())