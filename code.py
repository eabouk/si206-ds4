import unittest

# function to return the factorial of a number
# Add comments
def factorial(num):
    #factorial of 1 is 1 
    ans = 1
    if num < 0:
        return None

    #cannot do a factorial of a negative number
    elif num < 2:
        return ans

    else:
        #multiply all the numbers in the range of the number given to the function
        for i in range(1, num + 1):
            ans = ans * i
        return ans


# function to check if the input year is a leap year or not
def check_leap_year(year):
    isLeap = False
    if (year % 4) == 0:
        #if remainder for the year div. by 4 is zero, leap year
        if (year % 100) == 0:
            #if remainder for year div. by 100 is zero, leap year
            if (year % 400) == 0:
                #if remainder fro year div. by 400 is zero, leap year
                isLeap = True
        else:
            #leap year will be true if year mod. 100 is zero, and year mod. 4 is zero
            isLeap = True

    #OTHERWISE, return isLeap, which is set to false at the top of the function
    return isLeap

print("factorial(0): {}".format(factorial(0)))
print("factorial(1): {}".format(factorial(1)))
print("factorial(5): {}".format(factorial(5)))
print("factorial(-3): {}".format(factorial(-3)))

print("check_leap_year(2000): {}".format(check_leap_year(2000)))
print("check_leap_year(1990): {}".format(check_leap_year(1990)))
print("check_leap_year(2012): {}".format(check_leap_year(2012)))
print("check_leap_year(2100): {}".format(check_leap_year(2100)))

class test_cases(unittest.TestCase)

    def test_factorial(self):
        

if __name__ == "__main__":
    unittest.main(verbosity=2)






