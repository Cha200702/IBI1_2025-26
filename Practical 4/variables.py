a = 5.08*(10**6)
b = 5.33*(10**6)
c = 5.55*(10**6)
d = b - a
e = c - b
if d > e:
    print("d is larger than e")
    print("The population growth is decelerating in Scotland.")
elif d < e:
    print("e is larger than d")
    print("The population growth is accelerating in Scotland.")
else:
    print("d and e are equal")
    print("The population growth is constant in Scotland.")
# The population growth is decelerating in Scotland.
X = True
Y = False
W = X or Y
print (f"W is {W}")
# The following is the truth table for W = X or Y:
  # When X = True and Y = True, W will be True
  # When X = True and Y = False, W will be True
  # When X = False and Y = True, W will be True
  # When X = False and Y = False, W will be False