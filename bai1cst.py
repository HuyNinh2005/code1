n = int(input())
#Đếm số các chữ số của n
cout = len(str(n))
m = n

#Kiểm tra xem một số nguyên dương có phải là số Armstrong không
total = 0
while n > 0:
    digit = n % 10
    total += digit ** cout
    n //= 10
print(total)
print("-")
print(n)
print(m)

if(m == total):
    print("Co")
else:
    print("Khong")


