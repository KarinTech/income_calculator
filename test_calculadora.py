#funciones

hours =int(input("Enter the hours you have worked: "))

salary= (hours*968)
print("The salary is: " + str( hours* 968))

def Suma(salary,particulares):
    return salary+particulares


particulares = float(input("Ingrese el segundo valor a sumar: "))
print("La suma es: ", Suma(salary,particulares))

