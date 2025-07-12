import numpy as np
#Importamos clases de la libreria Rich para trabajar con ellas en nuestro menú
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.text import Text
import csv,os
console= Console()


#Importamos y configuracion de libreria para trabajar con logs(registro de acciones)
import logging, os

logging.basicConfig(
     filename="registro.log",
     level=logging.INFO,
     format='%(asctime)s - %(levelname)s - %(message)s'
)


#Importacion de funciones para utilizar
from modulos.resultados import leer_resultados,top_3_distancia,guardar_resultados,metricas,graficar_histogramas
from modulos.categorias import leer_categorias
from modulos.corredores import leer_corredores,agregar_corredor,eliminar_corredor,guardar_corredores


#Inicializamos nuestro archivo de corredores en caso de que no exista

def inicializar_corredoresCSV():
    nombre_archivo = "data/corredores.csv"
    campos = ["id", "nombre", "apellido","num_corredor", "fecha_nac", "edad","genero", "categoria", "distancia"]

    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
        print("Archivo 'corredores.csv' creado correctamente.")
    else:
        print("El archivo 'corredores.csv' ya existe.\n")

inicializar_corredoresCSV()

#Inicializamos nuestro archivo de resultados en caso de que no exista
def inicializar_resultadosCSV():
    nombre_archivo = "data/resultados.csv"
    campos = ["num_corredor","nombre","apellido","tiempo","categoria","distancia"]

    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "w", newline='', encoding="utf-8") as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
        print("Archivo 'resultados.csv' creado correctamente.")
    else:
        print("El archivo 'resultados.csv' ya existe.\n")

inicializar_resultadosCSV()


#Leemos archivo csv para trabajar con ellos

#Archivo corredores
with open("data/corredores.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    corredores = list(lector)

#Archivo categorias
with open("data/categorias.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    categorias = list(lector)

#Archivo resultados
with open("data/resultados.csv", "r", encoding="utf-8") as archivo:
    lector = csv.DictReader(archivo)
    resultados = list(lector)




#Menú de opciones
opcion_menu=-1 

while opcion_menu != 0:
        titulo= Text("Race Manager:",style="blue", justify="left")
        menu=""" 
          [bold cyan]1[/bold cyan]. Cargar DEMO de corredores y resultados
          [bold cyan]2[/bold cyan]. Visualizar corredores
          [bold cyan]3[/bold cyan]. Agregar un nuevo corredor
          [bold cyan]4[/bold cyan]. Eliminar corredor por ID
          [bold cyan]5[/bold cyan]. Ver resultados
          [bold cyan]6[/bold cyan]. Ver categorias
          [bold red]0[/bold red]. Salir del programa
             """             
        console.print(Panel.fit(menu, title=titulo, border_style="bright_blue"))
        try:
         opcion_menu = int(input("Selecciona una opción del menú: " ))
        except ValueError:
                print("Por favor, ingrese un número válido.")
                continue
        logging.info(f"Opción elegida: {opcion_menu}")
        if opcion_menu == 1:
            logging.info("Opción 1: Cargamos datos demo para prueba del programa")

            print("[¡Atención!] Se reemplazarán los datos cargados actualmente por datos de prueba.")
            confirmar = input("¿Desea continuar? (s/n): ").lower()
            if confirmar=="s":

                with open("data/corredores_demo.csv", "r", encoding="utf-8") as archivo:
                    corredores = list(csv.DictReader(archivo))
                    guardar_corredores(corredores)
                with open("data/resultados_demo.csv", "r", encoding="utf-8") as archivo:
                    resultados = list(csv.DictReader(archivo))
                    guardar_resultados(resultados)
                print("Datos de prueba cargados correctamente.")
            else:
                 print("Carga de datos DEMO cancelada")

        elif opcion_menu==2:
                logging.info("Opción 2 : Visualizamos todas los corredores")
                leer_corredores(corredores)
        
        elif opcion_menu==3:
                logging.info("Opción 3 : Cargamos corredor nuevo")
                nombre= str(input("Ingrese su nombre: "))
                apellido= str(input("Ingrese su apellido: "))
                fecha_nac=str(input("Ingrese su fecha de nacimiento en formato YYYY-MM-DD: "))

                while True:
                  genero= str(input("Ingrese su género, 'F' para femenino, 'M' para masculino:  ")).lower().strip()
                  if genero in ["f","m"]:
                        break
                  print("Género inválido. Intente nuevamente.\n" \
                  "Opciones válidas: F - M ")

            #Agregamos distancias según el evento
                while True:
                    distancia= str(input("Ingrese la distancia en la que participa: "))
                    if distancia in ["7","15"]: #Este caso tomamos estas 2 distancias disponibles
                        break
                    console.print("[red]Distancia inválida. Intente nuevamente.[/red]\n" \
                    "Opciones válidas: 7 - 15 ")
                agregar_corredor(corredores,nombre,apellido,fecha_nac,genero,distancia)
                logging.info("Corredor cargado")

        elif opcion_menu==4:
             logging.info("Opción 4: Eliminamos corredor")
             while True:
                 try: 
                    id_eliminar= int(input("Ingrese el ID del corredor que desea eliminar: "))

                    #Buscamos corredor para extraer unos datos 
                    corredor_buscado=next((corredor for corredor in corredores if str(corredor['id'])== str(id_eliminar)), None) 

                    if corredor_buscado and eliminar_corredor(corredores,id_eliminar):
                         print(f"Corredor {corredor_buscado['nombre']} {corredor_buscado['apellido']} con ID {id_eliminar} eliminado.")
                         logging.info(f"Corredor con ID {id_eliminar} eliminado")
                         break
                    else:
                         console.print("[red] No se encontró ningún corredor con ese ID[/red]")
                 except ValueError:
                                print("Ingrese un ID válido")

        elif opcion_menu==5:
            logging.info("Opción 5: Submenú de resultados")
            while True:
                titulo= Text("Sección Resultados:",style="blue", justify="left")
                menu=""" 
                [bold cyan]1[/bold cyan]. Visualizar resultados
                [bold cyan]2[/bold cyan]. TOP 3 por distancia
                [bold cyan]3[/bold cyan]. TOP 3 Categorías (PROXIMAMENTE)
                [bold cyan]4[/bold cyan]. Promedio de tiempos, mejor y peor tiempo
                [bold cyan]5[/bold cyan]. Generar gráfico de resultados
                [bold red]0[/bold red]. Volver al menú inicial
                """             
                console.print(Panel.fit(menu, title=titulo, border_style="bright_blue"))
            
                try:
                    opcion_resultados = int(input("Selecciona una opción del menú: " ))
                    
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                    continue
                logging.info(f"Opción elegida: {opcion_menu}")

        
                if opcion_resultados==1:
                    logging.info("Opción 5.1: Visualizamos resultados por tiempo")
                    leer_resultados(resultados)

                elif opcion_resultados==2:
                    logging.info("Opción 5.2: Top 3 por distancia ")
                    top_3_distancia(resultados)
                
                elif opcion_resultados==3:
                    logging.info("Opción 5.3: Top 3 por Categoría ")
                    print("Proximamente función disponible")

                elif opcion_resultados==4:
                    logging.info("Opción 5.4: Promedios - Mejor tiempo - Peor tiempo ")
                    metricas(resultados)

                elif opcion_resultados==5:
                    logging.info("Opción 5.5: Histograma tiempos ")
                    graficar_histogramas(resultados)

                elif opcion_resultados == 0:
                    logging.info("Opción 5.0: Volviendo al menú principal.")
                    break
                else:
                    print("Opción inválida. Por favor elija entre 0 y 6.")
                

        elif opcion_menu==6:
             logging.info("Opción 6: Visualizamos categorias disponibles")
             leer_categorias(categorias)     

