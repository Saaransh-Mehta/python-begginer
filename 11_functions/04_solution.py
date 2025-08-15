import math
pi = math.pi
def circle_area_and_circumference(r):
    area = round(pi * r**2,2)
    cir = round(2 * pi * r**2,2)
    return [area,cir]

result = circle_area_and_circumference(4)
area_circle = result[0]
circumference = result[1]
print(area_circle)
print(circumference)
