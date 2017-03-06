from collections import Counter
def answer(x, y):
    x_cntr = Counter(x)
    y_cntr = Counter(y)
    for num in x_cntr:
        if x_cntr[num] != y_cntr[num]:
            return num
        del y_cntr[num]
    else:
        return y_cntr.popitem()[0]
