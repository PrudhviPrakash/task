n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
for i in range(min(n1, n2), 0, -1):
    if n1 % i == 0 and n2 % i == 0:
        print(i, "is the HCF of", n1, "and", n2)
        break