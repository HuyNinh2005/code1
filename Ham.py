n = int(input("Nhập giá trị của n: "))
s = 0
max = 0
min = 10
while n > 0:
    cSDV = n % 10 #Lấy chữ số hàng đơn vị của N
    s = s + cSDV
    #Tìm số lớn nhất, nhỏ nhất của n
    if (cSDV > max): 
        max = cSDV
    else:
        min = cSDV
    n = n // 10
print(s)
print(min)
print(max)

