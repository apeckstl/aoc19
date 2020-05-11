f = open('input.txt', 'r')
strings = f.read().split(',')
inputmem = []
for thing in strings:
    inputmem += [int(thing)]
memory = inputmem.copy()
for noun in range(99):
    for verb in range(99):
        memory = inputmem.copy()
        memory[1] = noun
        memory[2] = verb
        pc = 0
        while pc < len(memory):
            opcode = memory[pc]
            arg1 = memory[pc+1]
            arg2 = memory[pc+2]
            arg3 = memory[pc+3]
            if opcode == 1:
                memory[arg3] = memory[arg1] + memory[arg2]
            elif opcode == 2:
                memory[arg3] = memory[arg1] * memory[arg2]
            elif opcode == 99:
                break;
            pc += 4
        if memory[0] == 19690720:
            print(noun * 100 + verb)
            break
