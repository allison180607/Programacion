#Leer el contenido del archivo de texto 'datos.txt' linea por linea
archi1=open("datos.txt","r")
for linea in archi1:
    print(linea, end='')
archi1.close()