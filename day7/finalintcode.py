def getparams(command,memory,ip):
    modes = command[:-2]
    args = []
    for i in range(1,len(modes)+1):
        if modes[len(modes)-i] == '0':
            arg = memory[memory[ip + i]]
        else:
            arg = memory[ip+i]
        args += [arg]
    return args

def runProgram(filename):
    f = open(filename, 'r')
    strings = f.read().split(',')
    memory = []
    for thing in strings:
        memory += [int(thing)]
    ip = 0
    while ip < len(memory):
        command = str(memory[ip])
        opcode = int(command[-2:])
        if opcode == 1 or opcode == 2:
            params = getparams(command.zfill(4),memory,ip)
            arg3 = memory[ip+3]
            if opcode == 1:
                memory[arg3] = int(params[0]) + int(params[1])
            elif opcode == 2:
                memory[arg3] = int(params[0]) * int(params[1])
            ip += 4
        elif opcode == 3:
            arg1 = memory[ip+1]
            memory[arg1] = int(input())
            ip += 2
        elif opcode == 4:
            if len(command) > 2:
                arg1 = memory[ip+1]
            else:
                arg1 = memory[memory[ip+1]]
            print(arg1)
            ip += 2
        elif opcode == 5 or opcode == 6:
            params = getparams(command.zfill(4),memory,ip)
            if opcode == 5 and params[0] != 0:
                ip = params[1]
            elif opcode == 6 and params[0] == 0:
                ip = params[1]
            else:
                ip += 3
        elif opcode == 7:
            params = getparams(command.zfill(4),memory,ip)
            if params[0] < params[1]:
                memory[memory[ip+3]] = 1
            else:
                memory[memory[ip+3]] = 0
            ip += 4
        elif opcode == 8:
            params = getparams(command.zfill(4),memory,ip)
            if params[0] == params[1]:
                memory[memory[ip+3]] = 1
            else:
                memory[memory[ip+3]] = 0
            ip += 4
        elif opcode == 99:
            break;

#runProgram("input.txt")
