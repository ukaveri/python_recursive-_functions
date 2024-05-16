#write a program to print 1 to 10 natural numbers using recurssion
'''
def show(n):
    if(n>1):
        show(n-1)
    print(n)

show(10)
'''
#write a program to print factorial value of a number using recurssion
'''
def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

a=int(input("Enter a number "))
f=fact(a)
print(f)
'''

