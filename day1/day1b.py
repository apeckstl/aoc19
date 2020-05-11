f = open('input.txt', 'r')
strings = f.readlines()
summ = 0
for thing in strings:
    mass = int(thing)
    while mass > 0:
        newmass = (mass // 3) - 2
        if (newmass > 0):
            summ += newmass
        mass = newmass
print(summ)
