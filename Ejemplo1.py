#Trabajando con archivos de texto en python
#1. Abrir el archivo en modo creacion
archi1=open("datos.txt","w")
archi1.write("Primera linea\n")
archi1.write("Segunda linea\n")
archi1.write("Tercera linea\n")
archi1.close()
print("Fin del programa")