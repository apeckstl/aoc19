f = open('input.txt', 'r')
strings = f.readlines()
summ = 0
for thing in strings:
    summ += (int(thing) // 3) - 2
print(summ)
