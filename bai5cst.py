import math
#Tìm ƯSCLN
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#Tìm BSCNN của hai số
def lcm(a, b):
    return a * b // gcd(a, b)
#Tìm BSCNN của 4 số
def lcm_of_four(a, b, c, d):
    return lcm(lcm(lcm(a, b), c), d)

# Nhập số lượng học sinh cho từng hàng
a = int(input("Nhập số học sinh trong hàng a: "))
b = int(input("Nhập số học sinh trong hàng b: "))
c = int(input("Nhập số học sinh trong hàng c: "))
d = int(input("Nhập số học sinh trong hàng d: "))

# Tính số sinh viên tối thiểu cần trong lớp
minimum_students = lcm_of_four(a, b, c, d)

print("Số sinh viên tối thiểu cần trong lớp là:", minimum_students)