# Write the Python code of a program that reads two numbers from the user, and prints their sum product, and difference.
#Hint: subtract the second number from the first one =======================================================Example 1:
# Sample Input: 4 and 5
# Sample Output:
#Sum = 9
#product = 20
#Difference = -1

num_1 = 4
num_2 = 5

sumResult = num_1 + num_2

sumProductResult = num_1 * num_2

productDefference = num_1 - num_2


print("Sum Result : ", sumResult  )
print("Sum Product Result : ", sumProductResult)
print("Product Defference : ", productDefference)





'''
Write the Python code of a program that reads two numbers from the user. The program should then
print "First is greater" if the first number is greater, "Second is greater" if the second number is
greater, and "The numbers are equal" otherwise.
==========================================================
Sample Input 1:
7
3
Sample Output 1:
First is greater
'''

#Sample Input for two number:
x = 7 
y = 3

if x > y:
    print("First is Greater")
elif x < y:
    print("Second is Greater")
else:
    print("The numbers are Equal")
    
    
    
'''
Write the Python code of a program that reads two numbers, subtracts the smaller number from the
larger one, and prints the result.
Hint: First, we may check which number is greater
=======================================================
Sample Input 1:
-40
-4
Sample Output 1:
36
Explanation: -4 > -40 so -4 - (-40) = -4 + 40 = 36
'''

#Check which number is larger, then subtract the smaller from the larger
a = -40
b = -4


if a > b:
     difference = a - b
else:
    difference = b - a
    
print("The difference is :", difference)