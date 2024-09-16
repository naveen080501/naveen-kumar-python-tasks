#Hello World Program
print("hello word")

#data Type Identification
x=(10.05)
print(type(x))

#String Manipulation
#Convert the string to uppercase.
text=("naveen kumar")
print(text.upper())

# Find the length of the string.
text=("find the lengthof the string")
print(len(text))

# Replace all occurrences of a specific character.
text=("thulasi neela")
print(text.replace("neela", "kumar"))

#Type Casting
x=1228
x=str(1228)
print(type(x))

#String Methods Exploration
#Count the number of vowels.

input_str = input('Enter the string: ')
count = 0
input_str = input_str.lower()
vowels = 'aeiou'
for char in input_str:
    if char in vowels:  
        count += 1
if count == 0:
    print('No vowels found')
else:
    print('Total vowels are: ' + str(count))
    
#Reverse the string.
str1="naveenkumar"
print(str1[::-1])

# Check if the string is a palindrome.
str_1 = input("Enter the string to check if it is a palindrome: ")
str_1 = str_1.lower()
x= (str_1[::-1])
if list(str_1) == list(x):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Write a Python program that concatenates three strings entered by the user and prints the result.

x= str1= "gunji"
y= str2= "naveen"
z= str3= "kumar"
name = x+y+z
print(name)

#the space we need to add between the name 
name= x+" "+y+" "+z 
print(name)


# Function to check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"
print(f"The number is {result}.")

     
     

#Basic List Operations
#Append a new element to the list.
fruits=["apple", "banana", "orange", 500, True]
fruits.append("grapers")
print (fruits)

# Remove the third element.
fruits.remove("orange")
print(fruits)

# Sort the list in ascending order
my_list=[1,8,2,9,3,5]
sorted_list = sorted(my_list)
print(sorted_list)
     
     
# Function to perform arithmetic operations
def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
            return num1 / num2
    print = int(input("Enter the first number: "))
    print = int(input("Enter the second number: "))
        
    print("\nSelect an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")
        
    if choice == '1':
            operation = 'add'
    elif choice == '2':
            operation = 'subtract'
    elif choice == '3':
            operation = 'multiply'
    elif choice == '4':
            operation = 'divide'
    else:
            print("Invalid choice. Please select a valid option.")
            return
        
    result = perform_operation(num1, num2, operation)
        

    print(f"Result: {result}")
    
