f = open("input.txt","r")
line = f.read().strip()
layers = [line[i:i+150] for i in range(0, len(line), 150)]
image = ['.'] * 150
for i in range(len(layers)-1,-1,-1):
    print(i)
    for j in range(150):
        char = layers[i][j]
        if char == '0':
            image[j] = '0'
        if char == '1':
            image[j] = '.'

for i in range(0,150,25):
    print(image[i:i+25])
