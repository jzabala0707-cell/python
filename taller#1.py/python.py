'''comentarios en python'''
'''variables y tipos de datos'''

entero = 42 # int
decimal = 3.14 # float
texto = "Hola" # str
bandera = True # bool
nada = None # NoneType

'''OPERADORES'''
Aritméticos: + - * / // % **
Comparación: == != > >= < <=
Lógicos: and or not
Asignación compuesta: += -= *= /=
Pertenencia: 'py' in 'python', 3 in [1,2,3]

'''ESTRUCTURAS DE DATOS'''

'''python'''
lista = [1, 2, 3]                       # mutable, ordenada
tupla = (10, 20)                        # inmutable, ordenada
conjunto = {1, 2, 2, 3}                 # únicos, sin orden -> {1,2,3}
dic = {"nombre": "Ana", "edad": 30}     # pares clave-valor

'''CADENAS (STRINGS)'''
'''python'''
s = "python"
s.upper() # "PYTHON"
s.capitalize() # "Python"
s.replace("py", "ru")
s[0] # 'p'
s[1:4] # "yth" (slicing)
f"Hola {s}!" # f-strings

'''CONTROL FLUJO'''
'''python'''
x = 7
if x > 10:
            print("Mayor a 10")
elif x == 10:
            print("Igual a 10")
else:
            print("Menor a 10")

for n in [1,2,3]:
 print(n) #print definido correctamente por qué esta en el contexto de un bucle
i = 0
while i < 3:
 i += 1 #incremento abreviado es lo mismo que i = i + 1


 


