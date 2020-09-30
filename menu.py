
import os

def Numeros():
    print ("***** Opción de Números *****")
    #ingresar n números, donde n es un número ingresado por teclado, calcular y mostrar: 
    #cantidad de números positivos, cantidad de números negativos, y cantidad de iguales a cero
    veces= int(input("Cuantos números desea ingresar?: "))
    pos=0
    neg=0
    cero=0
    for x in range(veces): 
        nume=int(input("Ingrese un número: "))
        if (nume>0):
            pos=pos+1
        elif(nume<0):
            neg=neg+1
        else:
            cero=cero+1

    print("Cantidad de números positivos: " + str(pos)+ 
          "\nCantidad de números negativos : "+ str(neg)+ 
          "\nCantidad de números iguales a cero: " + str(cero))    

    pausa=input("Presione una tecla para continuar")

def Datos():
    print ("**** Opción de Datos de Personas *****")


    pausa=input("Presione una tecla para continuar")

seguir=True
while (seguir):
    os.system('cls')
    print("1. Opción Numeros ")
    print("2. Opción Datos de Personas ")
    print("3. Finalizar")
    op=int(input("Ingrese opción 1,2,3: "))
    if (op==1):
        Numeros()           #invocamos a una función o def
    if (op==2):
        Datos()             #invocamos a una función o def 
    if (op==3):
        seguir=False
        break

