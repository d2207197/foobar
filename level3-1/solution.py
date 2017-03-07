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
    target_M, target_F = int(M), int(F)

    steps = []
    MFs = [(1, 1)]
    next_step = 1

    def step_in(step):
        if step == 1:
            M, F = rep1(*MFs[-1])
        elif step == 2:
            M, F = rep2(*MFs[-1])

        MFs.append((M, F))
        steps.append(step)

    while True:
        print steps
        print MFs
        print next_step
        print

        M, F = MFs[-1]

        if M == target_M and F == target_F:
            return str(len(steps))

        elif next_step == 3 and len(steps) == 0:
            return 'impossible'

        elif M > target_M or F > target_F or next_step == 3:
            last_step = steps.pop()
            MFs.pop()
            next_step = (last_step + 1)

        else:
            step_in(next_step)
            next_step = 1



def rep1(M, F):
    return M, F+M


def rep2(M, F):
    return M+F, F
