# coding: utf-8


def answer(x, y):
    num = 1
    for i in range(2, x + y):
        num += i
    return num - y + 1
