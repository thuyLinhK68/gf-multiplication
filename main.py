
from gf2m4 import multiply as multiply4
from gf2m8 import multiply as multiply8


def main():
    print("=== Phep nhan trong GF(2^4) ===")

    a4 = 0b1011
    b4 = 0b0101

    result4 = multiply4(a4, b4)

    print(f"a = {a4:04b}")
    print(f"b = {b4:04b}")
    print(f"Ket qua nhi phan: {result4:04b}")
    print(f"Ket qua hex: 0x{result4:X}")

    print("\n=== Phep nhan trong GF(2^8) ===")

    a8 = 0x57
    b8 = 0x83

    result8 = multiply8(a8, b8)

    print(f"a = 0x{a8:02X}")
    print(f"b = 0x{b8:02X}")
    print(f"Ket qua nhi phan: {result8:08b}")
    print(f"Ket qua hex: 0x{result8:02X}")


if __name__ == "__main__":
    main()
