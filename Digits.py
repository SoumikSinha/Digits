n = int(input("ENTER: "))
a = 1
d = 0
b = 1

while b >= 0:
        a = a * 10
        b = n - a
        d = d + 1

i = 2
digits = []
digits.append(n%10)
while i <= d:
        p = (n%(10**i) - n%(10 **(i -1)))/(10**(i -1))
        digits.append(int(p))
        i = i + 1
print("The digits are: ")
q = d
while q > 0:
        print(digits[q - 1], end = "  ")
        q = q - 1
        
