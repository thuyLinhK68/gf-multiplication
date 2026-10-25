## 1. Đa thức bất khả quy
 GF(2^4): x^4 + x + 1 (0x13)
 GF(2^8): x^8 + x^4 + x^3 + x + 1 (0x11B)

## 2. Thuật toán
Sử dụng phép XOR, dịch bit và rút gọn theo đa thức bất khả quy.

## 3. Cấu trúc project
 gf2m4.py: nhân trong GF(2^4)
 gf2m8.py: nhân trong GF(2^8)
 main.py: minh họa
 tests/: kiểm thử