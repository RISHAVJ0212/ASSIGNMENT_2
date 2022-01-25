print("\n" , "-"*50,"\n" , "1".center(50," ") ,"\n" ,"-"*50 ,"\n \n")


Given_string = "Python is a case sensitive language"

print("Given String is  : \n", Given_string)

print("\n------- a ------\n")
#To Find lenght of String

Length = len(Given_string)
print("Length of Given String is\t:\t",Length)

print("\n------- b ------\n")
#To Reverse the Sting

Reverse = Given_string[::-1]
print("Reversed order of Given Sting is   :\n", Reverse)

print("\n------- c ------\n")
#To use Slice Function

New_string = Given_string[10:26]
print(New_string)

print("\n------- d ------\n")
#To replace "a case sensitive" with "object oriented"

Replaced = Given_string.replace("a case sensitive", "object oriented")
print("After Replacing, Sting is  :\n" ,Replaced)

print("\n------- e ------\n")
#To Find index of "a"
print("the position of a is ", Given_string.find("a"))

print("\n------- f ------\n")
#To remove the White spaces

print("After removing the white, String is :\n",Given_string.replace(" ", ""))



print("\n" , "-"*50,"\n" , "2".center(50," ") ,"\n" ,"-"*50 ,"\n \n")

#Q-2
#To us String Formatting to print

Name = input("Enter your Name\t:\t")
SID = input("Enter your SID\t:\t")
Department = input("Enter your Department Name\t:\t")
CGPA = input("Enter your CGPA\t:\t")

print(
    "Hey,{} here! \n My SID is {} \n I am from {} department and my CGPA is {}".format(Name, SID, Department, CGPA)
)



print("\n\n" , "-"*50,"\n" , "3".center(50," ") ,"\n" ,"-"*50 ,"\n \n")

#Q-3
#To use Bitwise Operators

a = 56
b = 10
print("a=",a,"b=",b)
print("'a&b' is \t:\t", a&b)   #operator is "AND"
print("'a|b' is \t:\t", a|b)   #operator is "OR"
print("'a^b' is \t:\t", a^b)   #operator is "XOR"

#To shift a and b with 2 bits
print(
    "'a' and 'b' after shifting left with 2 bits are \t:\t", a<<2,"and", b<<2
)


#To shift a with 2 bits and b with 4 bits
print(
    "'a' and 'b' after shifting right with 2 and 4 bits respectively are \t:\t", a>>2,"and",b>>4
)



print("\n\n" , "-"*50,"\n" , "4".center(50," ") ,"\n" ,"-"*50 ,"\n \n")
#To Find the Greatest Number out of three Numbers

print("To find the largest number out of 3 input numbers")
First_num = float(input("Enter the First Number\t:\t"))
Second_num = float(input("Enter the second number\t:\t"))
Third_num = float(input("Enter the third number\t:\t"))
Greatest_num = ""

if First_num >Second_num and First_num > Third_num:
    Greatest_num = First_num
elif Second_num > Third_num and Second_num > First_num:
    Greatest_num = Second_num
elif Third_num > First_num and Third_num > Second_num:
    Greatest_num = Third_num
else:
    print("Out of the given Numbers Two Or Three Numbers are equal")

print("The Largest Number is\t:\t",Greatest_num)



print("\n\n" , "-"*50,"\n" , "5".center(50," ") ,"\n" ,"-"*50 ,"\n \n")
#To Find the word 'name' in the String

print("To check if word'name'is in data entered by you")
String_input = input("Enter the sentence in which you wnat to check 'name' word\t:\t")
Index = String_input.find(" name ")
if Index >= 0:
    print("Yes")
else:
    print("No")



print("\n" , "-"*50,"\n" , "6".center(50," ") ,"\n" ,"-"*50 ,"\n \n")
#To check if the Triangle is possible or not

print("To check if Tra=iangle is possible or not")
First_side = int(input("Enter the First Number\t:\t"))
Second_side = int(input("Enter the second number\t:\t"))
Third_side = int(input("Enter the third number\t:\t"))
Sides = [First_side, Second_side, Third_side]

# After sorting Largest side is 3rd elemnts of Sides list
#Theorem says that a Triangle can only be posiible if the largest side is smaller than the sum of other two sides

if Sides[2]>= (Sides[1]+Sides[0]) or Sides[1]>= (Sides[2]+Sides[0]) or Sides[0]>= (Sides[1]+Sides[2]):
    print("No")
else:
    print("Yes")
