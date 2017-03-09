import operator as op


def answer(start, length):
    checksum = 0
    for line in range(length):
        end = start + length - line

        if length - line >= 4:
            first_prod_of_4 = (start + (4 - start % 4)
                               if start % 4 != 0 else start)
            last_prod_of_4 = (end - end % 4 if end % 4 != 0 else end)
            all_numbers = (
                range(start, first_prod_of_4) + range(last_prod_of_4, end))
        else:
            all_numbers = range(start, end)

        checksum ^= reduce(op.xor, all_numbers, 0)

        start = end + line

    return checksum

# 95 - 60 = 35

# 60        0b111100
# 61        0b111101
# 62        0b111110
# 63        0b111111

# 64       0b1000000
# 65       0b1000001
# 66       0b1000010
# 67       0b1000011
# 68       0b1000100
# 69       0b1000101
# 70       0b1000110
# 71       0b1000111
# 72       0b1001000
# 73       0b1001001
# 74       0b1001010
# 75       0b1001011
# 76       0b1001100
# 77       0b1001101
# 78       0b1001110
# 79       0b1001111

# 80       0b1010000
# 81       0b1010001
# 82       0b1010010
# 83       0b1010011
# 84       0b1010100
# 85       0b1010101
# 86       0b1010110
# 87       0b1010111
# 88       0b1011000
# 89       0b1011001
# 90       0b1011010
# 91       0b1011011
# 92       0b1011100
# 93       0b1011101
# 94       0b1011110
# 95       0b1011111
