#For checking vowel
ch=input("Enter a char: ")
ch = ch.lower()
if ch in('a''e''i''o''u'):
    print(ch," is vowel")
else:
    print(ch,"is not vowel")


#Sum of to numbers
a = 20
b = 30
sum = a+b
print("Sum of two values are= ",sum)


#printing Name
name=input("Enter your name: ")
print("Welcome",name)


#Finding even & odd numbers
num=int(input("Enter your number= "))
if num%2==0:
	print("Even")
else:
	print("Odd")
	

#For finding area
length=float(input("Enter length= "))
width=float(input("Enter width= "))
area=length * width
print("Total area= ",area)


#Result of two numbers
float(input("Enter a number= "))
b=float(input("Enter a number= "))
print("1.Add")
print("2.subtract")
print("3.Multiple")
print("4.Division")
choice=int(input("Enter choice from 1 to 4= "))
if(choice==1):
	print("Result= ",a+b)
elif(choice==2):
	print("Result= ",a-b)
elif(choice==3):
	print("Result= ",a*b)
elif(choice==4):
	print("Result= ",a/b)
else:
	print("invalid choice")


#Factorial of a number
num=int(input("Enter a number= "))
fact=1	
for i in range(1, num+1):
	fact *=i
print("Factorial",fact)


#For largest value
int(input("Enter first number= "))
b=int(input("Enter second number= "))
c=int(input("Enter third number= "))
if(a>b) and (a>c):
	print("A is largest=",a)
elif(b>c) and (b>a):
	print("B is largest=",b)
else:
	print("C is largest=",c)
	

#for Positive and negative numbers
num=int(input("Enter your Number: "))
if num>0:
	print("Positive")
elif num<0:
	print("Negative")
else:
	print("No value")
	

#nested loop
for i in range(1, 6):
	for j in range(1, 6):
		print(i*j," ")
		print()


