# Entrada de datos del usuario
print("BIENVENIDO STALIN MENDIETA TE SALUDA :)")
print("Aprendamos: Operadores aritméticos, lógicos y relacionales")
print()
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
# Operadores aritméticos
print("________________________")
print("OPERADORES ARITMÉTICOS")
suma = num1 + num2
producto = num1 * num2
print(f" El resultado de la suma de {num1} y {num2} es = {suma}")
print(f" El resultado del producto de {num1} y {num2} es = {producto}")
# Operadores lógicos
print("________________________")
print("OPERADORES LÓGICOS")
es_positivo = suma > 0 and producto > 0
print(f" ¿La suma y el producto son positivos?")
print(f" {'Sí' if es_positivo else 'No'}")
alguno_negativo = suma < 0 or producto < 0
print(f" ¿Alguno de los resultados es negativo?")
print(f" {'Sí' if alguno_negativo else 'No'}")
# Operadores relacionales
print("________________________")
print("OPERADORES RELACIONALES")
if suma > producto:
 print(f" El resultado de la suma es mayor que el del producto.")
elif suma < producto:
 print(f" El resultado del producto es mayor que el de la suma.")
else:
 print(f" El resultado de la suma es igual que el del producto.")
if suma % 2 == 0:
 print(" El resultado de la suma es par.")
else:
 print(" El resultado de la suma es impar.")
if producto % 2 == 0:
 print(" El resultado del producto es par.")
else:
 print(" El resultado del producto es impar.")