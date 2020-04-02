
import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    i=0
    t=0
    for i in range(len(ar)):
        t=t+ar[i]

    return t
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
