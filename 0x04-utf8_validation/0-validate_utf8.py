#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    # Initialize the number of expected following bytes
    num_following_bytes = 0

    for byte in data:
        # Check if the byte is a following byte
        if 128 <= byte <= 191:
            if num_following_bytes:
                num_following_bytes -= 1
            else:
                return False
        else:
            # Determine the number of following bytes based on the MSB
            if 192 <= byte <= 223:
                num_following_bytes = 1
            elif 224 <= byte <= 239:
                num_following_bytes = 2
            elif 240 <= byte <= 247:
                num_following_bytes = 3
            elif byte > 247:
                return False

    # If all bytes were processed, and we expected 0 following bytes,
    # it's valid
    return num_following_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))

    data = [80, 121, 116, 104, 111, 110, 32, 105,
            115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
