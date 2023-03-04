# programa para identificar el punto de corte con el eje x de una funcion lineal 

print("---------------------------------")
print("---PUNTO DE CORTE CON EL EJE X---")
print("---------------------------------")

#input
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

#procesing

if(a != 0):
    x= -b/a
    rta= "El punto de corte con el eje x es: " +str(x)
else:
    rta= "los numeros ingresados son de una funcion constante"

# output
print(str(rta))