# define function to calculate
def cube(number):
    return number*number*number
#define a function which executes cube function if the number entered is divsible by 3
def by_three(number):
    if number %3 ==0:
        return cube(number)
    else:
        return False
#display result
print(by_three(9))
print(by_three(4))