nombre = input("Por favor digite el nombre: ")
edad = int(input("Escriba su edad, por favor: "))
if edad >= 18:
    print(f"{nombre}, Eres mayor de edad")
elif edad >= 60 and edad <=99:
    print(f"{nombre}, eres de la tercera edad")
else:
    print(f"{nombre}, Eres menor de edad")