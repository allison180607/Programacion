""""""

#Ejemplo simple de como leer un archivo completo de python3

nombre_archivo = "datos.txt" 
with open(nombre_archivo, "r",encoding="utf-8") as archivo:
    contenido = archivo.read()
    print("El contenido es: ", contenido)
    