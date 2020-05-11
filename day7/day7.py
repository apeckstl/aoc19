import intcode
import io
import sys
from itertools import permutations
from contextlib import redirect_stdout

l = list(permutations(range(5, 9)))
r = []
for phasecombo in l:
    output = 0
    for i in range(0,5):
        with io.StringIO() as f, redirect_stdout(f):
            sys.stdin = io.StringIO(str(phasecombo[i]) + "\n" + str(output))
            intcode.runProgram("input.txt")
            output = f.getvalue()
    r.append(int(output.strip()))
print(max(r))
