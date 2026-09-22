# Programmer: Aubrey Knowles
# Class: ENSC 201, Fall 2026
# Lab Task: Circle Calculations
# Date: 9/14/26
#
# Description:
# This program computes the area and circumference of a circle
# using a given radius value.

import math

def compute_circle_values(radius: float) -> None:
    """Computes and prints the area and circumference of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        None: Prints the computed area and circumference.
    """
    circle_area = math.pi * radius ** 2
    circle_circumference = 2 * math.pi * radius

    print(circle_area)
    print(circle_circumference)
    