from temperature.Celsius import c_to_f , c_to_k
from temperature.Fahrenheit import f_to_c , f_to_k
from temperature.Kelvin import k_to_c , k_to_f


def main():
    print ("Temperature converter options")
    print ("1 : C to F ")
    print ("2 : C to K")
    print ("3 : F to C")
    print ("4 : F to K")
    print ("5 : K to C")
    print ("5 : K to F")

while True :
    choice = int(input("Enter the numeric before the convertion you want to perform : "))

    if choice == 1:
        Celsius = float(input("Enter the temperature in celsius: "))
        print (f" {Celsius} = {c_to_f(Celsius)}")

    elif choice == 2:
        Celsius = float(input("Enter the temperature in celsius: "))
        print (f" {Celsius} = {c_to_k(Celsius)}")

    elif choice == 3:
        Fahrenheit = float(input("Enter the temperature in fahrenheit: "))
        print (f" {Fahrenheit} = {f_to_c(Fahrenheit)}")

    elif choice == 4:
        Fahrenheit = float(input("Enter the temperature in fahrenheit: "))
        print (f" {Fahrenheit} = {f_to_k(Fahrenheit)}")

    elif choice == 5:
        Kelvin = float(input("Enter the temperature in kelvin: "))
        print (f" {Kelvin} = {k_to_c(Kelvin)}")


    elif choice ==6 :
        Kelvin = float(input("Enter the temperature in kelvin: "))
        print (f" {Kelvin} = {k_to_f(Kelvin)}")

    else :
        print ("Invalid operation ")
