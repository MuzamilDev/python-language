#digits sum 
n = int(input("Enter a number "))
sum_digits = sum(int(digits) for digits in str(n))
print(f"Sum of digits is: {sum_digits}")
