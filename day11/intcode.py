import io
import sys
from itertools import permutations

def getparams(command,memory,state):
    modes = command[:-2]
    args = []
    ip = state[0]
    for i in range(1,len(modes)+1):
        if modes[len(modes)-i] == '0':
            position = memory[ip + i]
        elif modes[len(modes)-i] == '1':
            position = ip+i
        else:
            position = memory[ip+i] + state[1]
        if position >= len(memory):
            memory.extend([0]*(position+1-len(memory)))
        arg = memory[position]
        args += [arg]
    return args

def setoutput(command,memory,state,value):
    #3,103,203,11101,10001,21101,10007,21107,etc
    #first char will always be the mode, if opcode == 3, then the 1st arg is the location to set
    #otherwise it is 3rd arg
    if command[-2:] == '03':
        arg = memory[state[0]+1]
    else:
        arg = memory[state[0]+3]
    if command[0] == '2':
        position = arg+state[1]
    else:
        position = arg
    if position >= len(memory):
        memory.extend([0]*(position+1-len(memory)))
    memory[position] = value
   
def runProgram(memory,ip):
    relativebase = 0
    #instruction pointer points to current opcode, followed by arguments at ip+1, ip+2, etc
    while ip < len(memory):
        command = str(memory[ip])
        #1001 becomes 01, 1104 becomes 04, etc
        opcode = int(command[-2:])
        #switch on opcode
        #1: addition, 2: multiplication
        if opcode == 1 or opcode == 2:
            #get arguments using full command, getparams uses modes, first argument turns 1 to 0001
            params = getparams(command.zfill(4),memory,(ip,relativebase))
            #extend memory if result wants to be in BAD MEMORY
            if opcode == 1:
                result = int(params[0]) + int(params[1])
            elif opcode == 2:
                result = int(params[0]) * int(params[1])
            setoutput(command.zfill(5),memory,(ip,relativebase),result)
            ip += 4
        #3: input
        elif opcode == 3:
            result = int(input())
            setoutput(command.zfill(3),memory,(ip,relativebase),result)
            ip += 2
        #4: output
        elif opcode == 4:
            params = getparams(command.zfill(3),memory,(ip,relativebase))
            ip += 2
            print(params[0])
        #5: jump if arg != 0, 6: jump if arg == 0
        #CHANGE IP HERE
        elif opcode == 5 or opcode == 6:
            params = getparams(command.zfill(4),memory,(ip,relativebase))
            if opcode == 5 and params[0] != 0:
                ip = params[1]
            elif opcode == 6 and params[0] == 0:
                ip = params[1]
            else:
                ip += 3
        #7: set position to 1 if 1st argument is less than 2nd argument, otherwise 0
        elif opcode == 7:
            params = getparams(command.zfill(4),memory,(ip,relativebase))
            result = 1 if params[0] < params[1] else 0
            setoutput(command.zfill(5),memory,(ip,relativebase),result)
            ip += 4
	#8: set position to 1 if arguments are equal, otherwise 0
        elif opcode == 8:
            params = getparams(command.zfill(4),memory,(ip,relativebase))
            result = 1 if params[0] == params[1] else 0
            setoutput(command.zfill(5),memory,(ip,relativebase),result)
            ip += 4
        #9: increase relative base by 1st argument
        elif opcode == 9:
            params = getparams(command.zfill(3),memory,(ip,relativebase))
            relativebase += params[0]
            ip += 2
        elif opcode == 99:
            return -1,-1

f = open("test1.txt", 'r')
strings = f.read().split(',')
memory = []
for thing in strings:
    memory += [int(thing)]

runProgram(memory,0)


#runProgram("input.txt")
