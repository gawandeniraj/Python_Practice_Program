
a = 5
b = 6

#first way - using 3rd var
temp = a
a = b
b = temp
print("First Way a b:",a,b)


# 2nd way - using formula
c = 10
d = 20
c = c + d
d = c - d
c = c - d
print("2nd Way c d:",c,d)

# 3rd way
e = 30
f = 40
e = e ^ f
f = e ^ f
e = e ^ f
print("3rd way e f:",e,f)

# 4th way
g = 50
h = 60
g,h = h,g # it store in stack and during swaping it pop one by one so easy to swap in python
print("4th way g h:",g,h)