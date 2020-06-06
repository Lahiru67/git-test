num1=int(input("Enter the first number:\n"))
num2=int(input("Enter the second number:\n"))
num3=int(input("Enter the third number:\n"))
header = ['Number', 'Square','Cube']
print('       '.join(header))
for x in range(1):
    print(" {0}             {1}            {2}".format(
        num1, num1**2, num1**3
    ))
    print(" {0}             {1}           {2}".format(
        num2, num2**2, num2**3
    ))
    print(" {0}             {1}           {2}".format(
        num3, num3**2, num3**3
    ))
#edited




