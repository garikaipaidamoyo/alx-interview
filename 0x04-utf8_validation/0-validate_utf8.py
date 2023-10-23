#!/usr/bin/python3


def validUTF8(data):
    i = 0
    while i < len(data):
        byte = data[i]
        if byte & 0x80 == 0:
            # 1-byte character, the leading bit is '0'
            i += 1
        elif byte & 0xE0 == 0xC0:
            # 2-byte character, the leading bits are '110'
            i += 1
            if i >= len(data) or (data[i] & 0xC0 != 0x80):
                return False
            i += 1
        elif byte & 0xF0 == 0xE0:
            # 3-byte character, the leading bits are '1110'
            i += 1
            for _ in range(2):
                if i >= len(data) or (data[i] & 0xC0 != 0x80):
                    return False
                i += 1
        elif byte & 0xF8 == 0xF0:
            # 4-byte character, the leading bits are '11110'
            i += 1
            for _ in range(3):
                if i >= len(data) or (data[i] & 0xC0 != 0x80):
                    return False
                i += 1
        else:
            return False

    return True


if __name__ == "__main__":
    # You can add test cases here for testing
    data1 = [65]
    print(validUTF8(data1))  # Should print True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105,
             115, 32, 99, 111, 111, 108, 33]

    print(validUTF8(data2))  # Should print True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # Should print False
