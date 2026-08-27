def bubble_sort(numbers):

    n = len(numbers)

    for i in range(n):

        for j in range(0, n-i-1):

            if numbers[j] > numbers[j+1]:

                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


numbers = [5, 2, 8, 1, 3]

print("Original:", numbers)

result = bubble_sort(numbers)

print("Sorted:", result)
