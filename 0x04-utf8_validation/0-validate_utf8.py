#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    # Create a mask for the most significant bit (MSB) of a byte
    msb_mask = 1 << 7
    # Create a mask to check if the byte is a multibyte character
    multibyte_mask = 1 << 6
    # Initialize the number of expected following bytes
    num_following_bytes = 0

    for byte in data:
        # If we expect following bytes, check if the byte is a following byte
        if num_following_bytes:
            if byte & msb_mask and not byte & multibyte_mask:
                num_following_bytes -= 1
            else:
                return False
        else:
            # Determine the number of following bytes based on the MSB
            while byte & msb_mask:
                num_following_bytes += 1
                byte <<= 1

            # For a single-byte character, num_following_bytes should be 0
            if num_following_bytes == 1 or num_following_bytes > 4:
                return False

    # If all bytes were processed, and we expected 0 following bytes, it's valid
    return num_following_bytes == 0
