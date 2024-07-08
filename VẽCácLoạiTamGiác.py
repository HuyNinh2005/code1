n = int(input("Nhập số nguyên n: "))
#Vẽ tam giác cân
for i in range(1, n+1):
    for j in range(n - i + 1):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
#Vẽ hình chữ nhật
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print("*", end = "")
    print()
#Vẽ hình tam giác đối xứng
for i in range(1, n + 1):
    print(end = "")
    for j in range(0, 2*i - 1):
        print("*", end = "")
    print()
for i in range (n - 1, 0, -1):
    print(end = "")
    for j in range(1, 2 * i):
        print("*", end = "")
    print()