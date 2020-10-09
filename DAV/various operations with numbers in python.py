Python 3.3.3 (v3.3.3:c3896275c0f6, Nov 18 2013, 21:19:30) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Program to print difference of two numbers
>>> num1=int(input("Enter First number:"))
Enter First number:5
>>> num2=int(input("Enter second number:"))
Enter second number:7
>>> diff=num1-num2
>>> print("The difference of",num1,"and",num2,"is",diff)
The difference of 5 and 7 is -2
>>> 
>>> # program to print the positive difference of two numbers
>>> num1=int(input("Enter first number:"))
Enter first number:5
>>> num2=int(input("Enter Second number"))
Enter Second number6
>>> if num1>num2:
	diff=num1-num2
else:
        diff=num2-num1
print("the difference of",num1,"and",num2,"is",diff)
SyntaxError: invalid syntax
>>> 
>>> # Check whether a number is positive,negative, or zero
>>> number=int(input("Enter a number:"))
Enter a number:2
>>> if number > 0:
	print("Number is positive")
    elif number < 0:
	    
SyntaxError: unindent does not match any outer indentation level
>>>  print("Number is negative")
 
SyntaxError: unexpected indent
>>> else:
	
SyntaxError: invalid syntax
>>>       print("Number is zero")
      
SyntaxError: unexpected indent
>>> 
