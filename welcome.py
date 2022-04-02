'''
@Author : Priyanka
@Date : 2022-04-02  16:29:00
@Last Modified by : Priyanka
@Last Modified Time : 2022-04-02  16:35:00
@Title : Checking employee is present or not.
'''

import random

print("Welcome to the employee wage builder program.")

IS_Full_Time = 1
empCheck = random.randint(0,1)

if empCheck == IS_Full_Time:
    print("Employee is present")
else:
    print("Employee is absent")