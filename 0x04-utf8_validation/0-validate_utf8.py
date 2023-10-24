#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))

    # Additional test cases
    data = [197, 130, 1]
    print(validUTF8(data))

    data = [235, 140, 4]
    print(validUTF8(data))

    data = [240, 160, 130, 130]
    print(validUTF8(data))

    data = [194, 160]
    print(validUTF8(data))
