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


def answer(M, F):
    S, L = sorted((int(M), int(F)))
    step = 0
    while True:
        if S == 1:
            return str(L - 1 + step)

        remainder = L % S

        if remainder == 0:
            return 'impossible'
        else:
            step += L / S
            S, L = remainder, S
