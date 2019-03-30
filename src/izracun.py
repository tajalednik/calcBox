# hash key is comment
# create a program that calculates box sizes for wood cutting

# 1. let user enter box dimensions
g = 600
w = 450
h = 450

# 2. let user enter plywood width
d = 8

# 3. let some magic happen
w1 = g
h1 = w
w2 = g
h2 = h-d*2
w3 = w-d*2
h3 = h-d*2
# 4. print out calculated dimensions


print('calculated dimentions:')
print('2x {}x{}'.format(w1, h1))
print('2x {}x{}'.format(w2, h2))
print('2x {}x{}'.format(w3, h3))