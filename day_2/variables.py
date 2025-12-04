#Day 2: 30 Days of python programming
first_name="Aseel"
last_name="Ali"
full_name="Aseel Ali"
country="Palestine"
city="Gaza"
age=20
year=2025
is_married=False
is_true=False
is_light_on=True
study_topic, degree, family_num  ="Python Language programming", 83.73, 7

#1. Check the data type of all your variables using type() built-in function
print(type(first_name ))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

#2. Using the len() built-in function, find the length of your first name
len_first=len(first_name)
#3. Compare the length of your first name and your last name
len_last=len(last_name)
print("first name longer than last name?", len_first>len_last)

#4. Declare 5 as num_one and 4 as num_two
num_one=5
num_two=4

#5. Add num_one and num_two and assign the value to a variable total
total=num_one+num_two
print("the total= ", total)
#6. Subtract num_two from num_one and assign the value to a variable diff
diff=num_one-num_two
print("diffrance= ", diff)

#7. Multiply num_two and num_one and assign the value to a variable product
product=num_one*num_two
print("product= ", product)
#8. Divide num_one by num_two and assign the value to a variable division
division=num_one/num_two
print("division= ", division)
#9. Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder=num_two % num_two
print("remainder= ", remainder)
#10. Calculate num_one to the power of num_two and assign the value to a variable exp
exp=num_one**num_two
print("exp= ", exp)
#11. Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division=num_one//num_two
print("floor_division = ", floor_division)

"""
12. The radius of a circle is 30 meters.
i. Calculate the area of a circle and assign the value to a variable name of area_of_circle
ii. Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
iii. Take radius as user input and calculate the area.
"""
pi=3.14
radius=30
area_of_circle=pi * radius**2
circum_of_circle=2 * pi * radius
print("the area of the circle", area_of_circle)
print("the circum of the circle", circum_of_circle)
radius=float(input("Enter the new value to the radius: "))
area_of_circle=pi * radius**2
print(" the new area= ", area_of_circle)

#13. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
print(first_name, last_name, country, age)
first_name=input("Enter your first name: ")
last_name=input("Enter your last name: ")
country=input("Enter your country: ")
age=int(input("Enter your age: "))
print(first_name, last_name, country, age)

#14. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')
