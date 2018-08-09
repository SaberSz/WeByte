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
        opfile = os.path.join('.', 'SubmissionFiles', 'op.txt')
        f = open(opfile, "w+")  # output of the chuthads program
        q = open(test_inp, "r")  # database testcase input
        # INCLUDE A TIMEOUT AS SOMETIMES INFINITE LOOPS MAY BE PRESENT
        subprocess.call(['python', pg_file], stdin=q, stdout=f, shell=True)

        og_opfile = os.path.join('.', 'SubmissionFiles', testy['output'])
        if filecmp.cmp(og_opfile, opfile):
            judgements[cnt] = "PASSED"
        else:
            judgements[cnt] = "NOT PASSED"
        cnt += 1
    print(judgements)
    return judgements
