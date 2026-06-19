n = int(input("Enter a number: "))
a = n
s = 0
while n > 0:
    d = n % 10
    s += d ** 3
    n //= 10
if s == a:
    print(a, "is armstrong")
else:
    print(a, "is not armstrong")