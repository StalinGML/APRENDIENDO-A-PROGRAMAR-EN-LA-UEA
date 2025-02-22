# Declaración de variables de diferentes tipos de datos
# Enteros
entero_1 = 24
entero_2 = 17
# Flotantes
numero_flotante_1 = 22.08
numero_flotante_2 = 31.10
# Cadenas de texto
nombre = "Stalin"
apellido = "Mendieta"
# Booleanos
es_estudiante = True
es_maestro = False
# Realizando operaciones con enteros y flotantes
suma_entera = entero_1 + entero_2
resta_entera = entero_1 - entero_2
multiplicacion_flotante = numero_flotante_1 * numero_flotante_2
division_flotante = numero_flotante_1 / numero_flotante_2
# Concatenando cadenas de texto
nombre_completo = nombre + " " + apellido
# Usando operadores lógicos con booleanos
es_estudiante = es_estudiante and not es_maestro
es_empleado = es_maestro and not es_estudiante
# Mostrando los resultados
print("Resultados de las operaciones:")
print(f"Suma de enteros: {suma_entera}")
print(f"Resta de enteros: {resta_entera}")
print(f"Multiplicación de flotantes: {multiplicacion_flotante}")
print(f"División de flotantes: {division_flotante}")
print(f"Nombre completo: {nombre_completo}")
print(f"¿Es estudiante de la UEA?: {es_estudiante}")
print(f"¿Es maestro de la UEA?: {es_maestro}")