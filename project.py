# Function to calculate the sum of even numbers in a given range
def sum_of_even_numbers(start, end):
    total_sum = 0
    for num in range(start, end + 1):
        if num % 2 == 0:
            total_sum += num
    return total_sum

# Taking user input for the range
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Call the function and display the result
result = sum_of_even_numbers(start, end)
print(f"The sum of even numbers between {start} and {end} is: {result}")
hi
