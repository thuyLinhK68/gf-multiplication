
# So bit cua truong GF(2^8)
BITS = 8

# Da thuc bat kha quy:
# x^8 + x^4 + x^3 + x + 1
# Bieu dien hexadecimal: 0x11B
MODULUS = 0x11B

MASK = (1 << BITS) - 1
TOP_BIT = 1 << (BITS - 1)


def multiply(a, b):
    """Nhan hai phan tu trong GF(2^8)."""
    result = 0

    for _ in range(BITS):
        # Neu bit thap nhat cua b la 1
        if b & 1:
            result ^= a

        # Kiem tra bit cao nhat cua a
        carry = a & TOP_BIT

        # Nhan a voi x va giu lai 8 bit
        a = (a << 1) & MASK

        # Rut gon theo da thuc bat kha quy
        if carry:
            a ^= MODULUS & MASK

        # Chuyen sang bit tiep theo cua b
        b >>= 1

    return result
