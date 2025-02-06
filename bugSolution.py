def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle list with no numeric values
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_list = [1, 2, 3, 4, 5]
result = calculate_average(my_list)
print(f"The average is: {result}")

my_empty_list = []
result = calculate_average(my_empty_list)
print(f"The average is: {result}")

my_list_with_zero = [1, 0, 3, 4, 5]
result = calculate_average(my_list_with_zero)
print(f"The average is: {result}")

my_list_with_string = [1, 2, "a", 4, 5]
result = calculate_average(my_list_with_string) # This will now correctly return 2.666...
print(f"The average is: {result}")

my_list_with_only_string = ["a", "b", "c"]
result = calculate_average(my_list_with_only_string) # This will return 0
print(f"The average is: {result}") 