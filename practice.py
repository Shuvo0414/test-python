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