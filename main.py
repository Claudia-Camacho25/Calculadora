import math

def calculadora():
    print("Suma = 1")
    print("Resta = 2")
    print("Multiplicacion = 3")
    print("Division = 4")
    print("Potencia = 5")
    print("Raiz cuadrada = 6")

    opcion = int(input("Elige un número: "))



    if opcion == 6:  
        a = float(input("Ingrese el número: "))
        if a >= 0:
            print("El resultado es:", math.sqrt(a))
        else:
            print("Error: no se puede calcular raíz cuadrada de un número negativo")

    elif opcion == 5:
            a = float(input("Ingrese el número: "))
            b = float(input("Ingrese el exponente: "))
            print("El resultado es:", a ** b)
    else:
            print("Opción no válida")


calculadora()