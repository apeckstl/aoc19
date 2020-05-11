start = 108457
end = 562042

def checkDouble(number):
    for i in range(0,5):
        if int(number[i]) == int(number[i+1]):
            if i > 0 and i < 4:
                if int(number[i-1]) != int(number[i]) and int(number[i+1]) != int(number[i+2]):
                    return True
            elif i > 0:
                if int(number[i-1]) != int(number[i]):
                    return True
            elif i < 4:
                if int(number[i+1]) != int(number[i+2]):
                    return True
    return False

def checkIncreasing(number):
    for i in range(1,6):
        if int(number[i]) < int(number[i-1]):
            return False
    return True 

count = 0
for i in range(start,end):
    if checkIncreasing(str(i)) and checkDouble(str(i)):
        count += 1
print(count)
