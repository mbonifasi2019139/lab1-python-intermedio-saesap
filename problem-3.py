# Estudiante:
#     Marcos Daniel Bonifasi de León

# Programa de factorial aplica unicamente para numeros mayores a 0

iterator = 1
multiplication = 1


def factorial(iterator=1, number=0, multiplication=1):
    if number == 0:
        print("\nEl factorial es: \n1")
    elif iterator <= number:
        multiplication *= iterator
        iterator += 1
        if iterator > number:
            print(f"\nEl factorial es: \n{multiplication}")
        else:
            factorial(iterator, number, multiplication)
    else:
        print(
            "\nHa ingresado un numero negativo, aun no se ha desarrollado esa opcion :("
        )


try:
    number = int(input("Ingrese el numero para calcular su factorial: "))
except:
    print(f"Ingrese un numero entero valido {number}")
    exit(1)

factorial(iterator, number, multiplication)