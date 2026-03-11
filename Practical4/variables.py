#2004 Scotland population
a=5080000
#2014 Scotland population
b=5330000
#2024 Scotland population
c=5550000
#Change in population between 2004 and 2014
d=b-a
#Change in population between 2014 and 2025
e=c-b
if d>e:
	print("d is larger")#Scotland population is decelerating
elif e>d:
	print("e is larger")#Scotland population is accelerating
else:
	print("e=d")
X=True
Y=False
W=X or Y
#the truth table for W
#X Y W
#True True True
#True False True
#False True True
#False False False

