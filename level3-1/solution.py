# Test cases
# ==========

# Inputs:
#     (string) M = "2"
#     (string) F = "1"
# Output:
#     (string) "1"

# Inputs:
#     (string) M = "4"
#     (string) F = "7"
# Output:
#     (string) "4"


from itertools import count


def answer(M, F):
    S, L = sorted((int(M), int(F)))
    step = 0
    for step in count(0):
        if S == L == 1:
            return str(step)

        if S == 1:
            return str(L - 1 + step)

        remainder = L % S

        if remainder == 0:
            return 'impossible'
        else:
            S, L = remainder, S
