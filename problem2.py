#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""
a=int(input("Number:"))
a1=int(input("Another Number:"))
if a>a1 and a%a1==0:
    print(f"{a1}is a factor of{a}")
elif a1>a and a1%a==0:
    print(f"{a}is not a factor of {a1}")
else:
    print(f"{min(a,a1)}is not a factor of {max(a,a1)}")