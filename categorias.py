#Impotamos stream error para maneros de errores y path para rutas
from os import strerror,path


def leerCategorias(data_categorias):
    
    '''Leemos categorias de nuestro 
        data para poder trabajar
        con ellos o mostrarlos luego de nuestro main
    '''

    try: 
        categorias= open(data_categorias,'rt',encoding='utf-8')
        contador_linea = 0
        linea = categorias.readline()

    
        while linea !='':
            print(linea, end='')
            contador_linea += 1
            linea = categorias.readline()

        categorias.close()

        return  print(f"Se leyo el archivo {data_categorias}")

    except Exception as e:
        print(f"Error: {strerror(e.errno)}")