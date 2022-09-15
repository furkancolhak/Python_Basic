# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 22:03:14 2022

@author: enes
"""

print("Hello World")

# Divison
print(16/5)

# Modulo
print(29%7)

# exponentitation
print(5**2)

"""Problem"""



"""170$ in my account, 6% return and I do this for 7 years, how much money do I have?"""

# Create a variable account
account = 170

# growth_multiplier
growth_multiplier = 1.06

years = 7

# Calculate result
result = account*growth_multiplier**years

result

# types of data in python
# homework, find the 4 types of data in python, give examples to each of them, use in one operation.
# jupyter or colab
# separate cells for each type
# add headings and texts if needed
# explain the type

print("I started with $" + str(account) +" and now I have $" + str(result) +". Dammm!")

# I started with $170 and now I have $255.6171440285313. Dammm!

pi = "3.1415926"

pi_new = float(pi)
pi_new

int(True)

True != 1

# 0546 785 1007
# 20151709009@stu.khas.edu.tr

"""Lists"""

# area in square meters
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

areas = [hall,kit,liv,bed,bath]

areas

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom",bath]]

house

# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

areas[1]

areas[-1]

areas[5]

down = areas[0:6]

down

up = areas[6:10]

up

house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom",bed],
         ["bathroom",bath]]

house[0][1]

house[0][1]

areas

areas[-1] = 10.5

areas

areas_new = areas + ["garage", 15.45]
areas_new

del(areas[-4:-2])

areas

rm()

x= 1
while x < 4:
  print(x)
  x = x+1

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for x in areas:
  print(x)

