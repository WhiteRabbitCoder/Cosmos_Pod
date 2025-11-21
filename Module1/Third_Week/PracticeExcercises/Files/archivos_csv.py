import csv

def crear_archivo_csv(nombre_archivo, encabezados):
    with open(nombre_archivo, 'w', newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(encabezados)


