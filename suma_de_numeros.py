print("-------------------------------------------------------------------")
print("--------------------SUMA DE ENTEROS POSITIVOS----------------------")
print("-------------------------------------------------------------------")

n = int (input("Escriba el número de los enteros que quiere sumar: "))

i = 1
sum = 0
while i <= n:
    sum = sum + i
    i = i + 1

print ("El valor de la suma de los números es: " + str (i))