#dir -- to see WHAT YOU HAVE IN THE CURRENT DIRECTORY
#CD(CHDIR) -- TO CHANGE DIRECTORY


# Faqat harf yoki pastki chiziqcha (underscore) bilan boshlash mumkin
# Son bilan boshlanishi mumkin emas
#Faqat harf, son yoki underscore ishlatsa boladi
#Variable Names are Case Sensitive
# Python keywordlarni variable name ga berish mumkin emas(berilmaydi)


#first_name = 'Josh'

#ism = 'John'
#print(id(ism))


#NUmbers (Numerics)

#int
#float
#complex
# i j


#int

#age = 18
#print(age)
#print(18)

#age = '18'
#print (age, id(age), type(age))
#type() returns the data type of a given object

#int() converts values from other data type to int
#print(int(age))
#print (type(int(age)))

#float

#price = 15.50

#print(type(price))

#salary = '65.10'

#print(type(salary))
#float() converts the value of a given object to float

#price_float = float(salary)
#print(type(price_float))

#complex

#complex = 1 + 2j
#print(complex.imag)
#print(complex.real)
#COMPLEX(a,b) complex(5,20)
#example = complex(5,20)
#print(example.imag)

#print(summa)

#oybek = 5+2
#print(oybek)


#devision

#bolinma = 20/2
##print(bolinma)

#multiplication

#kopaytma = 5*9
#print(kopaytma)

## to get the int part of a devision

#whole_part = 19//4
#print(whole_part)


#qoldiq
#qoldiq = 19 % 4

#print(qoldiq)

#percent = 19 / 100 * 4
#print(percent)


## // + %

#divmod

#example = divmod(55,3)
#print(example)

#power

#powerr = power(9,3)
#print(powerr)

#powerr = 9**3
#print(powerr)

#Augmented Assigment
number = 15
#number = number +10
number += 10
print(number)

number1 = 13
number1 /= 3

print(number1)

# 1. Given a side of a square, find its perimeter and area
side = 5
perimeter = 4 * side
area = side ** 2
print(perimeter, area)

# 2. Given the diameter of a circle, find its circumference
diameter = 5
circumference = 3.14 * diameter
print(circumference)

# 3. Given two numbers a and b, find their mean
a= 2
b=3
mean1 = (a + b) / 2
print(mean1)

# 4. Given two numbers a and b, find their sum, product and square of each number
a = 2
b = 3
sum_ab = a + b
product_ab = a * b
square_a = a ** 2
square_b = b ** 2
print(sum_ab, product_ab, square_a, square_b)
