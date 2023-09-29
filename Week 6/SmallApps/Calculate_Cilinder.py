PI = 3.14


def calculate_contents_cylinder(radius, height, colour):
    surface_cylinder = radius * radius * PI
    contents_cylinder = height * surface_cylinder
    return surface_cylinder, contents_cylinder, colour


print(calculate_contents_cylinder(5, 20, 'Yellow'))
