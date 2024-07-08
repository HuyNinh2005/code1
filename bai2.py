n = int(input("Nhập số nguyên dương n: "))
sum = 0
for i in range (1,n + 1):
    sum += 1/i
print("Tổng của S = ", format(sum, ".2f"))