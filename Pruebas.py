from copy import*


a = [5,4,[1,2]]
b = deepcopy(a)
b[2][0] = 3

print(a)
