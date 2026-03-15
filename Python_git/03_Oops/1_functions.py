######################## FUNCTIONS #######################
# Function definition
def _sum():
    x = [1, 2, 3]
    sum_x = sum(x)

    return sum_x

# output = _sum() # Function Call
# print(output)

######################## local Scope & Global Scope #######################
a = "Rakesh"


def myname():
    global a
    a = 'Sima'
    print("In myname, My name is ", a)


def myname1():
    print("In myname1, My name is ", a)

# myname()
# myname1()


############################ Args and Kwargs #####################
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

# my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


################################# DECORATOR ###############################
def print_decorator(operation):
    def print_decorator(func): # func = _sum2
        def inner_function():
            val = func()
            print(f"{operation} value is", val)
            return val
        return inner_function
    return print_decorator


@print_decorator("Summation")
def _sum2():
    x = [1, 2, 3]
    sum_x = sum(x)

    return sum_x

@print_decorator("Multiplication")
def _multiply():
    x = [1, 2, 3, 4, 5]
    value = 1
    for i in x:
        value *= i

    return value

# output1 = _sum2() # Function Call
# output2 = _multiply() # Function Call



########################### LAMBDA #############################

x = lambda a, b : sum(a) * b
# print(x([1,2,3], 8))


