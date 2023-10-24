#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    num_bytes = 0

    for byte in data:
        byte_bin = format(byte, '08b')

        if num_bytes == 0:
            if byte_bin[0] == '0':
                num_bytes = 0
            elif byte_bin[:3] == '110':
                num_bytes = 1
            elif byte_bin[:4] == '1110':
                num_bytes = 2
            elif byte_bin[:5] == '11110':
                num_bytes = 3
            else:
                return False
        else:
            if not byte_bin.startswith('10'):
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
