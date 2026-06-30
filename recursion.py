            #DAY 30
#Factorial of 5=5*4*3*2*1 =>120
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return (n*factorial(n-1))
    
n=5
print("Number:",n)
print(f"factorial of {n} is",factorial(n))

        #recommiting

# Simple Fibonacci Series Program

n = int(input("Enter the number of terms: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b