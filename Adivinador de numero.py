print("Adivina el numero del 1 al 10 \n")
numero = 7
intento = 0

while intento != numero:
    intento = int(input("Adivina el número: "))

    if intento < numero:
        print("Muy bajo")

    elif intento > numero:
        print("Muy alto")

print("¡Correcto!")