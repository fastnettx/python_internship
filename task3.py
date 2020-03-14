# A function that displays the job of the previous week.
def display_the_task_of_the_previous_lesson():
    numbers_one = 1254
    strings_one = 'First line'

    # A method that compares types of variables and the result of execution is a message about comparing types.
    def compare_types(variable1, variable2):
        if type(variable1) is type(variable2):
            print("Data types match")
        else:
            print("Data types are different")

    compare_types(numbers_one, strings_one)

    strings_two = str(numbers_one)

    # Work with the list according to the terms of the assignment.
    my_list = list('Convert string')
    print(my_list)
    my_list.append('element')
    print(my_list)
    my_list.insert(7, 'Y')
    print(my_list)
    del my_list[0]
    my_list.pop(7)
    print(my_list)
    my_list.reverse()
    print(my_list)
    count_list = len(my_list)
    print(count_list)

    my_list_copy = my_list.copy()

    # Sorting method by bubble sorting algorithm.
    # The code is taken from https://webdevblog.ru/algoritmy-sortirovki-v-python/
    def bubble_sort(uncoated):
        flag = True
        while flag:
            flag = False
            for i in range(len(uncoated) - 1):
                if uncoated[i] > uncoated[i + 1]:
                    uncoated[i], uncoated[i + 1] = uncoated[i + 1], uncoated[i]
                    flag = True

    bubble_sort(my_list)
    print(my_list)

    my_list_copy.sort()
    print(my_list_copy)

    strings_three = 'This is a test string for Internship Onix for python'

    # We divide the line by spaces and add the received elements to the set.
    unique_set = set(strings_three.split())
    unique_list = list(unique_set)
    print(unique_list)
    unique_list.sort(reverse=True)
    print(unique_list)

    # Create a dictionary
    client_base = {723: "Aria", 325: "Bob", 943: "Bill", 304: "Karl"}
    print(client_base)
    client_base[432] = "Viktor"
    print(client_base)
    # We check for compliance with the key, and if the key is found, display the value that corresponds to it.
    if 325 in client_base: print(client_base.get(325))

    # A method that removes a value in a dictionary. It takes a dictionary and the value to be deleted as input.
    def delete_by_value(vocabulary, value):
        for key, values in vocabulary.copy().items():
            if values is value:
                vocabulary.pop(key)

    delete_by_value(client_base, 'Bill')
    print(client_base)
    # First we get a list of keys, values
    keys_client_base = list(client_base.keys())
    values_client_base = list(client_base.values())
    print(keys_client_base)
    print(values_client_base)

    # Sorts our dictionary into a list of pairs of sets by dictionary key
    sorted_key = sorted(client_base.items(), key=lambda value: value[0])
    # Sorts our dictionary into a list of pairs of sets by dictionary value
    sorted_values = sorted(client_base.items(), key=lambda value: value[1])
    print(sorted_key)
    print(sorted_values)


variable = 100
list_of_values = []


# A function that multiplies the specified value by a variable value of 100 and adds the result to the list.
def to_add_a_value_to_the_list(var):
    if type(var) is int:
        list_of_values.append(var * variable)
        print(list_of_values, len(list_of_values))
    else:
        print("Enter a numeric variable")


# The function that displays the values ​​of the arguments
def derive_arguments(*args, **kwargs):
    print(args)
    print(kwargs)


# A function that checks whether the first number is divisible without a remainder by the second
def is_divisible_by(num, divisor):
    if isinstance(num, (int, float)) and isinstance(divisor, (int, float)):
        if num % divisor == 0:
            print("Is divided")
        else:
            print("Not shared")
    else:
        print("Enter a numeric variable")


# A function that returns a fibonacci sequence.
# The argument of the function is the number to which the Fibonacci sequence is built.
def fibonacci(num):
    if isinstance(num, int):
        number1 = number2 = 1
        fibonacci_series = []
        if 0 < num < 2:
            fibonacci_series.append(number1)
            fibonacci_series.append(number2)
        if num >= 2:
            fibonacci_series.append(number1)
            fibonacci_series.append(number2)
            while (number1 + number2) <= num:
                number1, number2 = number2, number1 + number2
                fibonacci_series.append(number2)
        print(fibonacci_series)


if __name__ == "__main__":
    to_add_a_value_to_the_list(2)
    to_add_a_value_to_the_list(7)
    to_add_a_value_to_the_list(9)
    derive_arguments(2, 32, 323, 323, "32323", a=1, b="4", c=9)
    is_divisible_by(25, 5)
    fibonacci(124)
