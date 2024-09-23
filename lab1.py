'''
Task 1.
Write a Python program that prints "hello world" in a console.
Sample Outpu :
hello world
'''
# Print "hello world" to the console
print("Hello world")


'''
Task 2.
Write a Python program that prints the summation of 54 and 56. The program must use Python.
operators and numbers but not use any variables.
#Sample Output:
406
'''

# Print the summation of 54 and 56.

print(54 + 56)


'''
Task 3.
Write a Python program that assigns the values "Fall" and 2024 to variables `season` and `year`
respectively. Then, print the values of both variables in separate lines.
Sample Output:
Fall
2024
'''
# Assign values to variables 
season = "Fall"
year = 2024

# Print the values of both variables in separate lines.
print(season)
print(year)


'''
Task 4.
Write a Python program that reads the user's name and prints it back as shown in the example
below.

Sample Input : John
Sample Output: Your name is John
'''

name = "John"

print("Your name is",name)


'''
Task 5.
Write a Python program that reads two integers M and N respectively and finds the value of
M^N (or 𝑀 ) and prints the value as shown in the example. 𝑁

#Sample Input : 2
                3
#Sample Output : 2^3: 8

'''


M = 2
N = 3

## Calculate M raised to the power of N .
result = M ** N

# Print the result in the specified format and for this reason Using f-strings method
print(f"{M}^{N}: {result}")



'''
Task 6.
A sailor has a boat known as Téssares Boat, which has four corners. The boat is capable of
carrying goods of any weight as long as there is equal distribution of loads on each corner of the
boat - the center area has been occupied by the engine. The sailor needs your help to know the
maximum amount of weight he can carry in each shipment.
Write a Python program that reads the total weight of the shipment and prints the maximum load
(or weight) the boat can take from the given shipment. We can assume that the weight of each
good is exactly 1 unit, therefore, the weight of 5 units means there are 5 (loose) items in the
shipment.

#Sample Input : 9
#Sample Output : 8 
'''
# The total weight of the shipment
totalWeight = 9

#Calculate the maximum load that can be carried equally at the four corners
maxLoad = totalWeight - (totalWeight % 4)

print(maxLoad)


'''
Task 7.
Write a python program that takes an integer from the user which represents the number of
chocolates that he/she has. He/She decided to distribute the chocolates equally among 3 friends,
keeping the remaining chocolates for him/herself. Find out the number of chocolates each friend
will receive and the number of chocolates that will be remaining.

#Sample Input 1:
50
#Sample Output 1:
Each friend will receive 16 chocolates
The number of remaining chocolates is 2

'''

#Get the total number of chocolates from he/she

totalChocolates = 50

# Calculate the number of chocolates each friend receives and the remaining chocolates.

chocolatesPerFriends = totalChocolates // 3 # Division 
remainingChocolates = totalChocolates % 3  # Remainder

print(f"Each friend will receive {chocolatesPerFriends} chocolates")
print(f"The number of remaining chocolates is {remainingChocolates}")


'''
Task 8.
Write a Python program that reads an integer and prints "True" if the number is even, otherwise,
"False".

#Sample Input : 7
#Sample Output : False
'''
#Sample user input.
number = -26

# Check if the number is even.
if number % 2 == 0 : 
    print("True")  # Print "True" if the number is even.
else : 
    print("False") # Print "False" if the number is odd.