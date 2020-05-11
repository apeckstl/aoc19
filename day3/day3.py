f = open("input.txt", "r")
in_wires = f.read().splitlines()
wire1_string = in_wires[0]
wire2_string = in_wires[1]
wire1_inputs = wire1_string.split(',')
wire2_inputs = wire2_string.split(',')

def setupMap(strings):
    startx = 0
    starty = 0

    wiremap = {}
    for move in strings:
        if move[0] == 'U':
            for i in range(starty,starty + int(move[1:])):
                if i in wiremap:
                    wiremap[i].add((startx,startx))
                else:
                    wiremap[i] = set()
                    wiremap[i].add((startx,startx))
            starty += int(move[1:])
        elif move[0] == 'D':
            for i in range(starty,starty - int(move[1:]),-1):
                if i in wiremap:
                    wiremap[i].add((startx,startx))
                else:
                    wiremap[i] = set()
                    wiremap[i].add((startx,startx))
            starty -= int(move[1:])
        elif move[0] == 'R':
            if starty not in wiremap:
                wiremap[starty] = set()
            wiremap[starty].add((startx,startx+int(move[1:])))
            startx = startx + int(move[1:])
        else:
            if starty not in wiremap:
                wiremap[starty] = set()
            wiremap[starty].add((startx - int(move[1:]), startx))
            startx = startx - int(move[1:])
    return wiremap

wire1_map = setupMap(wire1_inputs)
wire2_map = setupMap(wire2_inputs)

def findOverlap(tuple1, tuple2):
    if (tuple1[0] > tuple2[1]):
        return []
    if (tuple1[1] < tuple2[0]):
        return []
    return range(max(tuple1[0], tuple2[0]), min(tuple1[-1], tuple2[-1])+1)

def makeIntersect(y, overlap):
    return (overlap,y)

intersections = []
for i in wire1_map:
    if i in wire2_map:
        for set1 in wire1_map[i]:
            for set2 in wire2_map[i]:
                intersections += map(lambda x1:(x1,i),findOverlap(set1,set2))

def intersectionDistance(intersection, inputs):
    wire1d = 0
    wire1 = (0,0)
    for step in inputs:
        char = step[0]
        number = int(step[1:])
        if wire1 == intersection:
            return wire1d
        if char == 'U':
            if (wire1[0] == intersection[0] and wire1[1] + number >= intersection[1]):
                return wire1d + (intersection[1] - wire1[1])
            wire1d += number
            wire1 = (wire1[0],wire1[1] + number)
        if char == 'D':
            if (wire1[0] == intersection[0] and wire1[1] - number <= intersection[1]):
                return wire1d + (wire1[1] - intersection[1])
            wire1d += number
            wire1 = (wire1[0],wire1[1] - number)
        if char == 'L':
            if (wire1[1] == intersection[1] and wire1[0] - number <= intersection[0]):
                return wire1d + (wire1[0] - intersection[0])
            wire1d += number
            wire1 = (wire1[0] - number, wire1[1])
        if char == 'R':
            if (wire1[1] == intersection[1] and wire1[0] + number >= intersection[0]):
                return wire1d + (intersection[0] - wire1[0])
            wire1d += number
            wire1 = (wire1[0] + number, wire1[1])
    return 0

distances = list(map(lambda x1:intersectionDistance(x1, wire1_inputs) + intersectionDistance(x1,wire2_inputs),intersections))
distances.pop(0)

print(min(distances))
f.close()
