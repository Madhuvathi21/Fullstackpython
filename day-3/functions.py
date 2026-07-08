################# Functions , reusable block of code that performs a specific task , can be called multiple times in the program

def greeting():
    print("Hello World")
greeting()  ################### calling the function

def welcoming():
    return "Heyyyyyyyyyyyyyyyyyyyy love <3"
result = welcoming()
print(result)  ################### calling the function and storing the returned value(return function)

def add(a,b):       ################passing arguments to the functions
    print(a+b)
add(90,80)

############ args used for tuples * (values) and kwargs used for dictionaries ** (key.values)in functions
def mo(*numbers):
    print(numbers)
mo(10,20,30,40,50)

def add(*num):
    total=0
    for i in num:
        total+=i
    print(total)
add(10,20,30,40,50,60)

################ kwargs
def student(**data):
    print("name:",data["name"])
    print("age:",data["age"])
    print("course:",data["course"])
student(name="ram", age=20, course="python")

########## square root of a number using function
def square_root(num):
    return num**0.5
print(square_root(16))

########## square of a number using function
def square(num):
    return num*num         ##num**2
print(square(5))


########## lambda functions :It can take any number of arguments
#It can only contain one expression
#It returns the value of that expression automatically
square = lambda x: x*x
print(square(5))

odd_even= lambda x: "even" if x % 2 == 0 else "odd"
print(odd_even(5))