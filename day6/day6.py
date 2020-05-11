with open("input.txt", "r") as f:
    inputs = f.read().split('\n')
    inputs = list(map(lambda x : x.split(')'), inputs))[:-1]
    all_planets = []
    santa = None
    you = None

    class Planet:
        def __init__(self, name):
            self.name = name
            self.children = []

        def __str__(self):
            return self.name + ":" + str(self.children)
        def __repr__(self):
            return self.__str__()

    def walkplanet(planet,inp):
        global santa 
        global you
        if planet.name == inp[0]:
            newChild = Planet(inp[1])
            if newChild.name == "SAN":
                santa = newChild
            if newChild.name == "YOU":
                you = newChild
            planet.children.append(newChild)
            return True
        for child in planet.children:
            if walkplanet(child,inp):
                return True
        return False

    for i in inputs: 
        #i[0] is parent
        #i[1] is child
        #check if parent in the structure already and if it is, add the child
        #else add parent to structure with child
        added = False
        for planet in all_planets:
            if walkplanet(planet,i):
                added = True
                break;
        if not added:
            parent = Planet(i[0])
            child = Planet(i[1])
            if child.name == "SAN":
                santa = child
            if child.name == "YOU":
                you = child
            parent.children.append(child)
            all_planets.append(parent)


    #if planet has the same name as input, we add all of inp's children to planet, 
    #otherwise we run method on all of planet's children until one returns true. if none do, we return false
   
    def walkplanet2(planet,inp):
        if planet.name == inp.name:
            for thing in inp.children:
                planet.children.append(thing)
            return True
        for child in planet.children:
            if walkplanet2(child,inp):
                return True
        return False

    length = len(all_planets)
    for i in range(length):
        added = False
        for planet in all_planets[i+1:]:
            if walkplanet2(planet, all_planets[i]):
                added = True
        if not added:
            print("found center of mass")
            all_planets.append(all_planets[i])


    #calculate orbits
    def calculate_orbit(distance,planet):
        if planet.children == []:
            return distance
        else:
            sum = distance
            for child in planet.children:
                sum += calculate_orbit(distance+1,child)
            return sum

    print(santa)
    def downPath(top,goal,distance):
        if top.name == goal.name:
            return distance - 1
        if top.children == []:
            return float("inf")
        best = float("inf")
        for child in top.children:
            childDist = downPath(child,goal,distance+1)
            if childDist < best:
                best = childDist
        return best

    def possiblePath(top):
        toSanta = downPath(top,santa,0)
        toYou = downPath(top,you,0)
        if toSanta == float("inf") or toYou == float("inf"):
            return float("inf")
        return toSanta + toYou

    print(calculate_orbit(0,all_planets[-1]))

    com = all_planets[-1]
    best = possiblePath(com)
    print(best)
    changed = True
    while changed:
        changed = False
        for child in com.children:
            calc = possiblePath(child)
            if calc < best:
                best = calc
                com = child
                changed = True
    print(best)


