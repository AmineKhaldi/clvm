def int_from_bytes(blob):
    size = len(blob)
    if size == 0:
        return 0
    return int.from_bytes(blob, "big", signed=True)


def int_to_bytes(v):
    byte_count = (v.bit_length() + 8) >> 3
    if v == 0:
        return b""
    r = v.to_bytes(byte_count, "big", signed=True)
    while len(r) > 1 and r[0] == (0xff if r[1] & 0x80 else 0):
        r = r[1:]
    return r


def limbs_for_int(v):
    """
    Return the number of bytes required to represent this integer.
    """
    return (v.bit_length() + 7) >> 3
