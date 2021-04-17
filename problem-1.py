# Estudiante:
#     Marcos Daniel Bonifasi de León

print("---------- Bienvenido al Juego ---------")
print("** Tienes que adivinar el color de la fruta**")


def guessTheFruit(attempts):
    if attempts > 0:
        fruitName = input(f"\nIngresa el nombre de la fruta: ")
        if fruitName.lower() == "naranja":
            print("Correcto!! \nGangaste :)")
        else:
            attempts -= 1
            print(f"Incorrento, tienes {attempts} intentos más")
            guessTheFruit(attempts)
    else:
        print("Perdiste... :(")


attempts = 3
guessTheFruit(attempts)
