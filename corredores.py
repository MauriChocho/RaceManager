#Impotamos stream error para maneros de errores y path para rutas
from os import strerror,path


def leerCorredores(data_corredores):
    
    '''Leemos corredores de nuestro 
        data para poder trabajar
        con ellos o mostrarlos luego de nuestro main
    '''

    try: 
        corredores= open(data_corredores,'rt',encoding='utf-8')
        contador_linea = 0
        linea = corredores.readline()

    
        while linea !='':
            print(linea, end='')
            contador_linea += 1
            linea = corredores.readline()

        corredores.close()

        return  print(f"Se leyo el archivo {data_corredores}")

    except Exception as e:
        print(f"Error: {strerror(e.errno)}")