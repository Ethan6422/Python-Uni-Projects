count = 0

number = int(input("Enter an even integer: "))

if number % 2 == 0:
    for integers in range(2, number + 1, 2):
        count += integers

    print(F"The sum of all even numbers up to {number} is {count}")
else:
    print("This number is not an even integer")