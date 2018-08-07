import os
import subprocess
from subprocess import call
# a = subprocess.call(['python', '.py', somescript_arg1, somescript_val1,...]).
f = open("abc.txt", "w")  # output of the chuthads program
q = open("abc1.txt", "r")  # database testcase input
subprocess.call(['python', 'hello.py'], stdin=q, stdout=f, shell=True)
# f = open("abc.txt", "w")

# print(a)
# f.write(a)
# f.close()
f = open("abc.txt")
print("\n asidhaisdhaihdiahsd\n")
for line in f:
    print(line)
