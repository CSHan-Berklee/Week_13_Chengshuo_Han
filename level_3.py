def Find_Max_In_List(numbers):
    if not numbers:
        print("List is Empty")
    maximum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum
numbers = [1, 2, 5, 10.2, 120, -250, 360.5]
print(Find_Max_In_List(numbers))

