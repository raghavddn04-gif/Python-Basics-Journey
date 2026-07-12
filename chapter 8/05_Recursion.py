""""
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2* 1
factorial(3) = 3* 2* 1
factorial(4)= 4* 3* 2* 1
factorial(5) = 5* 4* 3* 2* 1
factorial(n) = n* n-1* n-2 ...... 3* 2* 1


factorial(n)= n* factoral(n-1)


"""


# we use mathematical formula to call itself (recursion makes easier to solve problem in few lines of code )
def factorial(n):
    if (n==1 or n==0):
        return 1
    return n* factorial(n-1)


n=int(input("Enter the number: "))
print(f"The factorial of this number is :{factorial(n)}")