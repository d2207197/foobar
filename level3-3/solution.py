import operator as op


def answer(start, length):
    checksum = 0
    for row in range(length):
        end = start + length - row

        start_nearest_even = start >> 1 << 1
        end_nearest_even = end >> 1 << 1
        checksum ^= ((start_nearest_even >> 1) - (end_nearest_even >> 1)) % 2

        if start % 2 == 1:
            checksum ^= start_nearest_even
        if end % 2 == 1:
            checksum ^= end_nearest_even

        start = end + row

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
