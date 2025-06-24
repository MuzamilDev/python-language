#factor programm

numb = int(input("Enter number for finding factors: "))
print("Factors",end=' ')
for i in range(1, numb+1):
 if numb%i == 0:
    print(i, end=" ")
