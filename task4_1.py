class ClassOne:
    def __init__(self, number):
        self.number = number
        print("Class '%s' with attribute '%s' created" % (self.__class__.__name__, self.number))

    def __del__(self):
        return "The class '%s', object attribute '%s' has been removed" % (self.__class__.__name__, self.number)

    def is_divisible_by(self, divisor):
        if self.number % divisor == 0:
            print("The number '%s' is divided by the number '%s'." % (self.number, divisor))
        else:
            print("The number '%s' is not divided by the number '%s'.") % (self.number, divisor)

    @staticmethod
    def static_method(number_one, number_two):
        print("%s * %s = " % (number_one, number_two), (lambda x, y: x * y)(number_one, number_two))


test = ClassOne(21)
print(test.__del__())
test.is_divisible_by(7)
ClassOne.static_method(12, 10)


class ClassTwo(ClassOne):
    __var = "String variable"

    def __variable_check(self, variable):
        if isinstance(variable, str):
            print("Variable -'%s'-> String" % variable)
        else:
            print("Variable -'%s'-> Not a string" % variable)


test1 = ClassTwo(2222)
test1.is_divisible_by(11)
test1._ClassTwo__variable_check("test")
print(test1._ClassTwo__var)


class ClassThree(ClassTwo):
    @staticmethod
    def static_method(one, two):
        if isinstance(one, int) and isinstance(two, int) and one > 0 and two > 0:
            number_one = one
            number_two = two
            while number_one != number_two:
                if number_one > number_two:
                    number_one = number_one - number_two
                else:
                    number_two = number_two - number_one
            NOD = number_one
            NOK = int((one * two) / NOD)
            print("NOD =", NOD, ", NOK =", NOK)
        else:
            print("The value entered must be a positive integer.")


test2 = ClassOne(1)
test3 = ClassThree(2)
test2.static_method(12, 122)
test3.static_method(12, 122)
