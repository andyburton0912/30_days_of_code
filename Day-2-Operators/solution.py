#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):

    if __name__ == '__main__':
        meal_cost = float(input())
        tip_percent = int(input())
        tax_percent = int(input())
        tip = meal_cost * tip_percent / 100
        tax = meal_cost * tax_percent /100
        totalcost = meal_cost + tax + tip

    print(str(round(totalcost)))


solve(12.00, 20, 8)