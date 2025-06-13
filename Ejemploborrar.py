#Eliminar lineas del archivo
#Abrir archivo y leer las lineas
with open("datos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()

#Filtrar las lineas que no contienen "segunda linea"
lineas_fitradas=[linea for linea in lineas if linea.strip() != "Segunda linea"]

#Sobrescribir el archivo con las lineas filtradas
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas_fitradas) 