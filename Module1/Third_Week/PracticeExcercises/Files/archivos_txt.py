def crear_archivo_txt(nombre_archivo, contenido):
    """Crea un archivo de texto con el nombre y contenido especificados."""
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    return f"Archivo '{nombre_archivo}' creado con éxito."

def leer_archivo_txt(nombre_archivo):
    """Lee y devuelve el contenido de un archivo de texto."""
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return f"El archivo '{nombre_archivo}' no existe."
    except Exception as e:
        return f"Ocurrió un error al leer el archivo: {e}"

def agregar_a_archivo_txt(nombre_archivo, contenido):
    """Agrega contenido al final de un archivo de texto existente."""
    try:
        with open(nombre_archivo, 'a') as archivo:
            archivo.write(contenido)
        return f"Contenido agregado al archivo '{nombre_archivo}' con éxito."
    except Exception as e:
        return f"Ocurrió un error al agregar contenido al archivo: {e}"

