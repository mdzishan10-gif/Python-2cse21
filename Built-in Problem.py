Problem Statement: The Architect's Calculator
Background
You have been hired by a construction firm to build a specialized calculation tool. The architects provide raw measurements, but they need a program that handles the precision math required for building safety and material ordering.
Objective
Write a Python program using the math module to process construction dimensions and output specific values.
Requirements
Your program must perform the following tasks:
1.	Material Estimation (Rounding):
o	Accept a float value (e.g., 14.2) representing the number of floor tiles needed.
o	Use a function to Round Up the value, because tiles must be bought in whole boxes.
o	Use a function to Round Down the value to determine how many full tiles can fit in a specific row.
2.	Structural Calculations (Powers & Roots):
o	Calculate the length of a support beam using the square root of a provided area.
o	Calculate the volume of a cubic water tank by raising the side length to the power of 3.
3.	Geometry Constants:
o	Calculate the circumference of a circular pillar using the built-in constant for pi.
o	Formula: Circumference = 2*pi*radius
4.	Angle Conversion:
o	Architects provide angles in degrees. Use a function to convert a 45 degree angle into radians so it can be used in further trigonometric calculations.


import math
# 1. Material Estimation
tiles = 14.2
print("=== Material Estimation ===")
print(f"Tiles needed (float): {tiles}")
print(f"Round Up (ceil): {math.ceil(tiles)}")
print(f"Round Down (floor): {math.floor(tiles)}")

# 2. Structural Calculations
area = 225.0
side_length = 5.0
print("\n=== Structural Calculations ===")
print(f"Support beam length (sqrt of {area}): {math.sqrt(area)}")
print(f"Water tank volume ({side_length}^3): {math.pow(side_length, 3)}")

# 3. Geometry Constants
radius = 7.0
print("\n=== Geometry Constants ===")
print(f"Pi value: {math.pi}")
print(f"Circumference of pillar (radius={radius}): {2 * math.pi * radius:.4f}")

# 4. Angle Conversion
degrees = 45
print("\n=== Angle Conversion ===")
print(f"Angle in degrees: {degrees}")
print(f"Angle in radians: {math.radians(degrees):.4f}")
