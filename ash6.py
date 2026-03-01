numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print("Squares:", squares)
numbers.append(3)
numbers.sort()
print("Sorted list:", numbers)
numbers.remove(max(numbers))
print("List after removing max:", numbers)
