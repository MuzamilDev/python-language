n = int(input("Enter numb of terms: "))
a, b = 0, 1 #we declare variable in python this type too
for _ in range(n):
    print(a, end=' ')
    a,b = b, a + b
