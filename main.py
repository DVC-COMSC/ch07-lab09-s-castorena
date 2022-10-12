# ******************************
# Make your Code
# ******************************
# Sarah Castorena

names = []
name = input('Enter names: ')
names = name.split()
sortednames = sorted(names)
print(min(sortednames,key=len), max(sortednames,key=len))
