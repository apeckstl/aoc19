import intcode

def turnleft(d):
    if d == (0,1):
        return (-1,0)
    elif d == (1,0):
        return (0,1)
    elif d == (0,-1):
        return (1,0)
    elif d == (-1,0):
        return (0,-1)



