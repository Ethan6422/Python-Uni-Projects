total_3 = 0     # used to find the total number of numbers divisible by 3
sum_3 = 0       # used to find the average

for n in range(5):
    number = int(input(f"Enter number {n+1}: "))

    if number % 3 == 0:
        total_3 += 1
        sum_3 += number

if total_3 > 0:
    print(f"The total numbers that are divisible by 3 are {total_3}")
    average = sum_3 / total_3
    print(F"The average of these numbers is {average}")

else:
    print("There are no numbers divisible by 3")
