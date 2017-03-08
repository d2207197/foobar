import re
RIGHT_ZEROS_RE = re.compile(r'.*?(0+)$')


def answer(n):
    n = int(n)
    steps = 0
    while n > 1:
        print(n)
        bn = bin(n)
        if bn[-2:] == '01':
            n -= 1
            steps += 1
        elif n == 3:
            n = 1
            steps += 2
        elif bn[-2:] == '11':
            n += 1
            steps += 1
        else:
            n_zeros = len(RIGHT_ZEROS_RE.match(bn).group(1))
            n >>= n_zeros
            steps += n_zeros

    return steps
