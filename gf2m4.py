
# So bit cua truong GF(2^4)
BITS = 4

# Da thuc bat kha quy: x^4 + x + 1
# Bieu dien nhi phan: 10011
MODULUS = 0x13

MASK = (1 << BITS) - 1
TOP_BIT = 1 << (BITS - 1)


def multiply(a, b):
    """Nhan hai phan tu trong GF(2^4)."""
    result = 0

    for _ in range(BITS):
        # Neu bit thap nhat cua b la 1
        if b & 1:
            result ^= a

        # Kiem tra bit cao nhat cua a
        carry = a & TOP_BIT

        # Nhan a voi x va giu lai 4 bit
        a = (a << 1) & MASK

        # Rut gon theo da thuc bat kha quy
        if carry:
            a ^= MODULUS & MASK

        # Chuyen sang bit tiep theo cua b
        b >>= 1

    return result
