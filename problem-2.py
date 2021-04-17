# Estudiante:
#     Marcos Daniel Bonifasi de León

x = 0
y = 1
z = 0
iterator = 0
strOut = "01"


def fibonacci(x=0, y=1, z=0, n=0, iterator=0, strOut=""):
    if (n > iterator):
        z = x + y
        x = y
        y = z
        strOut = f"{strOut} {z}"
        iterator += 1
        fibonacci(x, y, z, n, iterator, strOut)
    elif n == 0:
        print(strOut)
    else:
        print(f"No existe sucesion para {n}")


try:
    n = int(input("Ingrese la serie a calcular: "))
except:
    print("Ingrese un numero entero valido")
    exit(1)

fibonacci(x, y, z, n, iterator, strOut)
