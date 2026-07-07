product_price =5000
delivery_charges= 100

total = product_price + delivery_charges
print(total)

a=10
b=3

print(a+b)    
print(a-b)
print(a*b)
print(a/b)  
print(a//b)  # integer division
print(a%b)   # remainder
print(a**b)  # power

##########
followers=10000
followers +=1
print(followers)

###########
x="abc"
y="abc"
print(x==y)  # comparison operator

###########
balance=1000
pin_correct=True
if balance>=500 and pin_correct:
    print("You can withdraw money")
else:
    print("You cannot withdraw money")    

############### Billing system

#item = input("Enter item name: ")
#quantity= int(input("Enter quantity: "))
#price=float(input("Enter price: "))
#total = quantity * price
#print("Total price: ", total)

################# conditional operator

password=input("Enter password: ")
if password=="admin":
    print("Access granted")
else:
    pass
#     print("Access denied")



# CGPA= int (input ("enter your CGPA:"))
# if CGPA>=9:
#     print("A grade")
# elif CGPA>= 7:
#     print("B grade")
# elif CGPA>= 5:
#     print("C grade")
# else:
#     print("fail")

################## logical condition

########### AND Operator
salary = int(input("Enter your salary: "))
age= int(input("Enter your age: "))
if salary>=10000 and age>=18:
    print("You are eligible for loan")

########### OR Operator
day= input("Enter day: ")
if day=="saturday" or day=="sunday":
    print("You can go for picnic")

############ Functions
def withdraw_money():
    pin=input("enter thr pin:")
    if pin=="1234":
        print("login successful")
        amount=int(input("enter the amount:"))
        balance=5000
        if amount<=balance:
            balance=balance-amount
            print("withdraw successful")
            print("remaining balance:",balance)
        else:
            print("insufficient balance")
    else:
        print("incorrect pin")

withdraw_money()

################# for loop ( for list ) (used for iterating over a sequence of elements in range)
for i in range(2,6):
 print(i)
users =[ "madhu" , "adaka"]  
for users in users:
    print("message sent to", users)

########### to print characters from a string( ch / char)
name = "madhu"                 
for char in name:
    print(char)

############  while loop ( kept executing until the condition is true)
count = 1
while count<=5:
    print(count)
    count+=1

########### continue statement ( only the specified iteration will be skipped  and the other iterations are executed)
for i in range(10):
    if i == 5:
         continue
    print(i)

############### break statement ( the loop will be terminated when the specified condition is met)
for i in range(10):
    if i == 5:
        break
    print(i)

############LIST##################################
student=[
    "sam",
    "madhu",
    "ram"
]
student.append("adaka")
student.append("ss")
print(student)

