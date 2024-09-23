#1. Write the Python code of a program that reads two numbers from the user, and prints their sum product, and difference.
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
2.
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
3.
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

#Sample Input:
a = -40
b = -4

#Check which number is larger, then subtract the smaller from the larger

if a > b:
     difference = a - b
else:
    difference = b - a
    
print("The difference is :", difference)


'''
4.
Write the Python code of a program that reads a number, and prints "The number is even" or "The
number is odd", depending on whether the number is even or odd.
hint(1): we may use the modulus (%) operator to check for even or odd
hint(2): we can consider the number to be an integer.

Sample Input 1:
7
Sample Output 1:
The number is odd

Sample Input 2:
10
Sample Output 2:
The number is even

'''

#Sample Input number
number = 7

# Check if the number is Even or Odd.
if number % 2 == 0 :
    print("The number is Even")
else:
    print("The number is Odd")


'''
5.
Write the Python code of a program that reads an integer as input from the user, and prints the integer
if it is a multiple of 2 OR 5 and prints "Not a multiple of 2 OR 5" otherwise.
For example, 2, 4, 5, 6, 8, 10, 12, 14, 15, 16, 18, 20, 22 … i.e. this includes multiples of 2 only,
multiples of 5 only and multiples of 2 and 5 both.
===
hint(1): we may use the modulus (%) operator for checking the divisibility
hint(2): we can consider the number to be an integer
===
Sample Input 1:
5
Sample Output 1:
5
'''

# Get integer from the user
num = 5

# Check if the number is a multiple of 2 or 5
if num % 2 == 0 or num % 5 == 0:
    print(num)
else:
    print("Not a multiple of 2 OR 5")
