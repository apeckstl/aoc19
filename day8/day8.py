f = open("input.txt","r")
line = f.read().strip()
layers = [line[i:i+150] for i in range(0, len(line), 150)]
di = {}
for i in range(len(layers)):
    zeroes = 0
    ones = 0
    twos = 0
    for char in layers[i]:
        if char == '0':
            zeroes += 1
        if char == '1':
            ones += 1
        if char == '2':
            twos += 1
    di[i] = [zeroes,ones,twos]
minzeroes = min(di.items(), key=lambda i: i[1][0])
print(minzeroes[1][1] * minzeroes[1][2])
