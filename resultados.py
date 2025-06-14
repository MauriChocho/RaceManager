#Impotamos stream error para maneros de errores y path para rutas

from os import strerror,path


def leerResultados(data_resultados):

    '''Leemos resultados de nuestro 
        data para poder trabajar
        con ellos o mostrarlos luego de nuestro main
    '''

    try: 
        resultados= open(data_resultados,'rt',encoding='utf-8')
        contador_linea = 0
        linea = resultados.readline()

    
        while linea !='':
            print(linea, end='')
            contador_linea += 1
            linea = resultados.readline()

        resultados.close()

        return  print(f"Se leyo el archivo {data_resultados}")

    except Exception as e:
        print(f"Error: {strerror(e.errno)}")
