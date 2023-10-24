#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    bytes_to_follow = 0

    for byte in data:
        if bytes_to_follow == 0:
            if byte & 0x80 == 0:  # Single-byte character
                bytes_to_follow = 0
            elif byte & 0xE0 == 0xC0:  # Two-byte character
                bytes_to_follow = 1
            elif byte & 0xF0 == 0xE0:  # Three-byte character
                bytes_to_follow = 2
            elif byte & 0xF8 == 0xF0:  # Four-byte character
                bytes_to_follow = 3
            else:
                return False
        else:
            if byte & 0xC0 != 0x80:  # Check if the byte is a following byte
                return False
            bytes_to_follow -= 1

    return bytes_to_follow == 0


# Test cases
data1 = [65]
print(validUTF8(data1))  # Should print True

data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data2))  # Should print True

data3 = [229, 65, 127, 256]
print(validUTF8(data3))  # Should print False
