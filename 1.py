"""
The area of an equilateral triangle is ¼(√3a2) where "a" represents a side of the triangle. You are provided with the side "a". Find the area of the equilateral triangle.

Input Description:
The side of an equilateral triangle is provided as the input.

Output Description:
Find the area of the equilateral triangle and print the answer up to 2 decimal places after rounding off.

Sample Input :
20
Sample Output :
173.21

"""
import math

side_length = int(input()) # Replace with the desired side length

area = (math.sqrt(3) * side_length ** 2) / 4

print(round(area,2))

