###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   result1 = (x+y)/2
   return result1

# takes two numbers from keyboard
n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')