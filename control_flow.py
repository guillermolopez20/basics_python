#if…else statement 
edad = input('introduce tu edad:')
if int(age) >= 18:
    print("puedes votar")
#---------------------------------------
    a = 2 + 3
if a == 4: 
    print ("A es igual a cuatro") # Imprimir
else:
    print ("No se cumple la condicion")
#---------------------------------------
x = 5
if x == 5:
    print("Es 5")
else:
    print("No es 5")

#Ternary operator

energy = 5
if energy <= 0:
    game_over = True

print(f"Is the game over? {game_over}")
#----------------------
es_feo = True
estado = "Es feo" if es_feo else "No es feo"
#-------------------
es_bonito = True
apariencia = ("Feo", "Bonito")[es_bonito]
print("El gato es ", apariencia)

#Python for Loop with Range

for i in range(5):
    print(i, end=", ") # prints: 0, 1, 2, 3, 4, 
    #------------------------------------------
    for i in range(-1, 5):
    print(i, end=", ") # prints: -1, 0, 1, 2, 3, 4, 
    #------------------------------------------
    for i in range(-1, 5, 2):
    print(i, end=", ") # prints: -1, 1, 3, 
    
    #while
    x = 1
while x < 10:
	print(x)
    x += 1
    #-----------
n = 0
while n <= 5:
    print(n)
    n = n + 1
    #----------------
    i = 1
while i <= 3:
    print(i)
    i += 1
print("tarea terminad")

#BREAK
for x in range(5):
    if x == 2:
        break
    print(x)
#--------------
 numero = 0
while numero < 10:
if numero == 5:
    break
print('el número es ', numero)
numero += 1
#----------------
i = 0
while True:
    print("Hello World")
    i+=1
    if i == 10:
        break
#CONTINUE
coleccion = [2, 4, 5, 7, 8, 9, 3, 4]
for e in coleccion:
    if e % 2 != 0:
        continue
    print(e)
    #-------------------------
    for x in range(5):
    if x == 2:
        continue
    print(x)
    #----------------
    i=1
    while i < 10
        i+=1
        if i ==5
         continue
    print (i)
#pass
for letra in "Python":
    if letra == "h":
        pass
    print ("Letra actual :" + letra)

# ------------
var = 10
while var > 0:
    var = var -1
    if var == 5:
        pass
    print ("Valor actual de la variable :" + str(var))

print ("fin del script")
#----------------------
 for x in (1, 2, 3):
    print (x)
    pass
    print (str(x) + " nuevamente")







