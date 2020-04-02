import datetime
from random import randint, choice

current_date = datetime.datetime.today()
one_day = datetime.timedelta(days=1)
sum_of_dates = current_date + one_day
date_string = sum_of_dates.strftime("%d-%m-%Y %H:%S")
print("Your date: " + date_string)

date_string_one = "2020-02-03 09:18:36.000"
converted_date = datetime.datetime.strptime(date_string_one, "%Y-%m-%d %H:%M:%S.%f")
print("Your day: " + converted_date.strftime("%d"))
print("Your month: " + converted_date.strftime("%m"))
print("Your year: " + converted_date.strftime("%Y"))
print("Your hour: " + converted_date.strftime("%H"))
print("Your second: " + converted_date.strftime("%S"))

array = []
while len(array) < 3:
    number = randint(100, 999)
    if number % 5 == 0:
        array.append(number)
print(array)

string = ""
while len(string) < 10:
    char = chr(randint(33, 125))
    string += char
print(string)

array_of_tickets = []
for i in range(100):
    ticket = randint(10 ** 9, 10 ** 10 - 1)
    array_of_tickets.append(ticket)

winning_ticket_one = choice(array_of_tickets)
array_of_tickets.remove(winning_ticket_one)
winning_ticket_two = choice(array_of_tickets)
print("Winning tickets :", winning_ticket_one, ",", winning_ticket_two)


class MyError(Exception):
    pass


def number_division(number1, number2):
    if number1 == number2:
        raise MyError("Numbers should not be equal")
    return number1 / number2


try:
    number_one = number_division(10, 5)
except ZeroDivisionError:
    print("The value of the second number should not be 0")
except TypeError:
    print("Invalid argument type")
except MyError:
    print("Arguments must not be equal.", MyError)
else:
    print("Your result :", number_one)
finally:
    print("You have been working with feature - number_division")
