# Problema 1
nombre = input("Por favor, ingresa tu nombre de usuario: ")
print("¡Hola {}!".format(nombre))

# Problema 2
consumo = float(input("Ingrese el costo de su comida en el restaurante: "))
propina_porcentaje = float(input("Ingrese el porcentaje de propina que desea dejar: "))
propina = consumo * (propina_porcentaje / 100)
print("La cantidad de dinero a dejar como propina es: ${:.2f}".format(propina))

# Problema 3
payasos = int(input("Ingrese el número de payasos vendidos: "))
muñecas = int(input("Ingrese el número de muñecas vendidas: "))
peso_total = (payasos * 112 + muñecas * 75) / 1000
print("El peso total del paquete a enviar es: {:.2f} kg".format(peso_total))

# Problema 4
N = int(input("Ingrese un número entero positivo: "))
suma = N * (N + 1) / 2
print("La suma de todos los enteros desde 1 hasta {} es: {}".format(N, suma))

# Problema 5
shows_musicales = int(input("¿Cuántos shows musicales has visto en el último año? "))
ha_visto_mas_de_3 = shows_musicales > 3
print(ha_visto_mas_de_3)

# Problema 6
edad = int(input("Ingrese la edad del cliente: "))
if edad < 4:
    print("El cliente puede entrar gratis.")
elif edad <= 18:
    print("El precio de la entrada es $5.")
else:
    print("El precio de la entrada es $10.")

# Problema 7
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
opcion = input("Elija una opción:\n1. Mostrar la suma de los dos números\n2. Mostrar la resta de los dos números\n3. Mostrar la multiplicación de los dos números\n")
if opcion == '1':
    print("La suma de los dos números es:", num1 + num2)
elif opcion == '2':
    print("La resta de los dos números es:", num1 - num2)
elif opcion == '3':
    print("La multiplicación de los dos números es:", num1 * num2)
else:
    print("Opción inválida.")

# Problema 8
hora = input("Por favor, ingrese la hora en formato HH:MM: ")
horas, minutos = map(int, hora.split(":"))
if 7 <= horas <= 8:
    print("Es hora del desayuno.")
elif 12 <= horas <= 13:
    print("Es hora del almuerzo.")
elif 18 <= horas <= 19:
    print("Es hora de la cena.")

# Problema 9
lista_original = ['Di', 'buen', 'día', 'a', 'papa']
lista_invertida = lista_original[::-1]
print(lista_invertida)

# Problema 10
lista = ['Rojo', 'Verde', 'Blanco', 'Negro', 'Rosa', 'Amarillo']
del lista[5]
del lista[4]
del lista[0]
print(lista)

# Problema 11
lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_sin_duplicados = list(set(lista_original))
print(lista_sin_duplicados)

# Problema 12
nombre_archivo = input("Ingrese el nombre del archivo: ")
tipos_mimetype = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}
extension = nombre_archivo.lower().split(".")[-1]
print(tipos_mimetype.get('.' + extension, 'application/octet-stream'))
