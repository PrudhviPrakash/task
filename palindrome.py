n = int(input("Enter a number: "))
a = n
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
if rev == a:
    print(a, "is palindrome")
else:
    print(a, "is not palindrome")