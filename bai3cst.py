n = int(input("Nhập số nguyên dương n: "))
#Tính giá trị biểu thức sc
sc = 0
for i in range(n):
    sc += 3
    sc = sc**0.5
print(format(sc, ".3f"))

#Tính giá trị biểu thức sd
sd = 0
factorials = 1
for i in range(1, n + 1):
    factorials = factorials * i
    sd = sd + factorials
print(format(sd, ".3f"))
