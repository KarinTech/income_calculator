#funciiones
def Suma(a,b):
    return a+b

#función resta:
def Resta(a,b):
    return a-b

#función multiplicar
def Multiplicacion(a,b):
    return a*b

#función division
def Division(a,b):
    return a/b

def Salir(a,b):
    return 



print("CALCULADORA")

opcion=int(input("Selecione Opcion"))
print(1.- Suma)
print(2.- Resta)
print(3.-Multiplicacion)
print(4.- Division)
print(5.- Salir)

if opcion == 1:
    Suma 
valor1 = float(input("Ingrese el primer valor : "))
valor2 = float(input("Ingrese el segundo valor: "))
print("La suma es: ", Suma(valor1,valor2))



elif opcion == 2:
borrarPantalla()
print("Operación Restar")
print(‘—————‘)
print(»)
valor1 = float(input("Ingrese el primer valor : "))
valor2 = float(input("Ingrese el segundo valor: "))
print(»)
print("La Resta es: ",Resta(valor1,valor2))
elif opcion == 3:
borrarPantalla()
print("Operación Multiplicar")
print(‘—————‘)
print(»)
valor1 = float(input("Ingrese el primer valor : "))
valor2 = float(input("Ingrese el segundo valor: "))
print(»)
print("La multiplicacón es: ",Multiplicacion(valor1,valor2))
elif opcion == 4:
borrarPantalla()
print("Operación División")
print(‘—————‘)
print(»)
valor1 = float(input("Ingrese el primer valor : "))
valor2 = float(input("Ingrese el segundo valor: "))
print(»)
print("La división es: ",Division(valor1,valor2))
elif opcion == 5:
break
else:
borrarPantalla()
print("Opción incorrecta")