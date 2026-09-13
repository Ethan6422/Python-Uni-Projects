def find_max(numbers):
     max_value = numbers[0] # Initialize max_value with the first list element
     for number in numbers: # Iterate through the list
        if number > max_value: # Check if the current number is greater than max_value
            max_value = number # Update max_value to the current number
     return max_value # Return the maximum value

result = find_max([7, 2, 9, 4, 5])
print(result)



