a = input("masukan bilangan A :")
b = input("masukan bilangan B :")
c = input("masukan bilangan C :")

if a > b and a > c:
    terbesar = a
else:
    if b > c and b > a:
        terbesar = b
    else:
        terbesar = c

print(terbesar)

