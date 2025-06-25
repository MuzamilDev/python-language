putInt = int(input("Enter Number: "))
sum_divisors = sum(i for i in range(1,putInt)if putInt % i ==0)
if sum_divisors == putInt:
    print("Perfect Number")
else:
    print("No Perfect Number")
