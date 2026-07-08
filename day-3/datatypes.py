################## tuples are immutable and cannot be changed after creation and can be accessed by index value  ####################

students =("ram", "sam" , "raj")
print(students[-1])
################## can have multiple values in single variable (_)
numbers= (1,2,3,4,5,6,7,8,9)
print(numbers[-3])

################# List doesn't have index values , and are mutable [_] , can't add duplicate value

data= [1 , 2 , 3]
data[1] =100
print(data)

x= (1,2,1,4,5,1,1,8,9)         ################### counts the number of times it repeats in tuple , can add duplicate value
print(x.count(1))

colors= ("red", "green", "blue", "yellow", "orange")
print(colors.index("blue"))  ################### returns the index value of the element in tuple

num= (10,20,30,40,50)
print(num[1:4])  ################### slicing in tuple , ending values are not included in the output

################ sets are unordered and mutable , removes duplicate value,  unique values are stored in set , can be used to perform mathematical operations like union, intersection, difference

################# sets {_} , they don't have index values , can't be accessed by index value 

num={1,2,3,4}
print(num)

a= {1,3 ,5}
b= {2,5,9}
print(a|b)  ################### union of two sets

print(a&b)  ################### intersection of two sets

print(a-b)  ################### difference of two sets

