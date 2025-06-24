#Armstrong Numbers 
num = int(input("Enter Number: "))
order = len(str(num))
sum_power = sum(int(d)**order for d in str(num))
if num == sum_power:
    print("Armstrong Number")
else:
    print("Not an Armstrong number")
