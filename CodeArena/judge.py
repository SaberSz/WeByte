import os
import subprocess
from subprocess import call
import filecmp


def judge_me(prg_file, test_cases):
    judgements = []
    cnt = 0
    for testy in test_cases:
        test_inp = os.path.join('.', 'SubmissionFiles', testy['input'])
        pg_file = os.path.join('.', 'SubmissionFiles', prg_file)
        opfile = os.path.join('.', 'SubmissionFiles', "UJNH9889" + testy['input'])
        f = open(opfile, "w+")  # output of the chuthads program
        q = open(test_inp, "r")  # database testcase input
        subprocess.call(['python', pg_file], stdin=q, stdout=f, shell=True)
        op1file = os.path.join('.', 'SubmissionFiles', testy['output'])
        f.close()
        q.close()
        if filecmp.cmp(opfile, op1file, shallow=True):
            judgements.append("PASSED")
        else:
            judgements.append("NOT PASSED")
        cnt += 1
        os.remove(opfile)
    # print(judgements)
    return judgements


# t = [{'testcase': 1, 'input': '00bee00c11-sample-input-00be49f.txt', 'output': '01f3c4d811-sample-output-01f3124.txt'}, {'testcase': 2, 'input': 'e9886f5a11-input-e988145.txt.clean (1).txt', 'output': 'e9cc5c2411-output-e988165.txt'}]
# p = "AZOZKYRXPVYSZJPNOGFAZVSRAZYXZA.txt"
# # # Hihi and Crazy Bits
# judge_me(p, t)
