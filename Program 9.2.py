# main.py — Import and use shapes module
import P9_1 as shapes

def main():
    print('=== Shape Area Calculator ===')
    print('1. Circle')
    print('2. Rectangle')
    print('3. Triangle')
    choice = int(input('Enter your choice (1/2/3): '))

    if choice == 1:
        r = float(input('Enter radius of circle: '))
        area = shapes.area_circle(r)
        print(f'Area of Circle = {area:.4f} sq. units')

    elif choice == 2:
        l = float(input('Enter length of rectangle: '))
        w = float(input('Enter width of rectangle: '))
        area = shapes.area_rectangle(l, w)
        print(f'Area of Rectangle = {area:.4f} sq. units')

    elif choice == 3:
        b = float(input('Enter base of triangle: '))
        h = float(input('Enter height of triangle: '))
        area = shapes.area_triangle(b, h)
        print(f'Area of Triangle = {area:.4f} sq. units')

    else:
        print('Invalid choice!')

main()
