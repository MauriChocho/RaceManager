#Impotamos stream error para maneros de errores, path para rutas, rich para mejorar aspectos
from os import strerror,path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich import box
import csv,os
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

console = Console()


def guardar_resultados(resultados, archivo="data/resultados.csv"):
    """
    Guarda la lista completa de resultados en el archivo CSV, 
    sobrescribiendo cualquier contenido anterior.
    """
    campos = ["num_corredor","nombre","apellido","tiempo","categoria","distancia"]

    with open(archivo, "w", newline='', encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(resultados)

def tiempo_seg(tiempo):

    """
    Función para convertir los tiempos a segundos para funciones 
        de podio(top3)
    """

    #Tomamos minutos y segundos separados por :

    minutos, segundos = map(int, tiempo.split(":"))
    return minutos * 60 + segundos

def ordenar_por_tiempo(resultado):
    """Función clave(key function) que recibe por parametro un resultado
      y retorna su clave tiempo_segundos, la utilizaremos adelante para 
      ordenar los resultados por tiempo
    """
    return resultado["tiempo_segundos"]

def leer_resultados(resultados):

    """
        Mostramos resultados ordenados por tiempo
         con todos sus campos

    """

         #Chequeamos si tenemos algun corredor para mostrar
    if not resultados:
        console.print("[bold red] No hay resultados disponibles.[/bold red]")
        return

    #Ordenamos resultados por tiempo usando nuestra key function (linea 63)
    for resultado in resultados:
        resultado["tiempo_segundos"] = tiempo_seg(resultado["tiempo"])
    
    resultados.sort(key=ordenar_por_tiempo)


    #Creamos tabla para mostrar datos
    tabla = Table(title="Resultados", box=box.SIMPLE)

    tabla.add_column("Número corredor", justify="center", style="cyan", no_wrap=True)
    tabla.add_column("Nombre", style="bold magenta")
    tabla.add_column("Apellido", style="bold magenta")
    tabla.add_column("Tiempo", style="yellow")
    tabla.add_column("Categoría", style="green")
    tabla.add_column("Distancia", style="bright_cyan")

    for resultado in resultados:
        tabla.add_row(
        str(resultado["num_corredor"]),
        str(resultado["nombre"]).upper(),
        str(resultado["apellido"]).upper(),
        str(resultado["tiempo"]),
        str(resultado["categoria"]),
        str(resultado["distancia"]),
    )
    console.print(tabla)

def top_3_distancia(resultados):

    """
    Función donde obtenemos el Top 3 por distancia
    
    """


    distancias= ["7", "15"]


    for resultado in resultados:
        resultado["tiempo_segundos"] = tiempo_seg(resultado["tiempo"])

    for distancia in distancias:
    #Creamos tablas para mejor visualizacíon

        tabla = Table(title=f"TOP 3 - {distancia}KM", box=box.SIMPLE)
        tabla.add_column("Nº Corredor", style="cyan", justify="center")
        tabla.add_column("Nombre", style="bold magenta")
        tabla.add_column("Apellido", style="bold magenta")
        tabla.add_column("Tiempo", style="yellow")
        tabla.add_column("Categoría", style="green")
        tabla.add_column("Distancia", style="bright_cyan")

 
        puesto= [r for r in resultados if r["distancia"] == distancia]
        puesto.sort(key=ordenar_por_tiempo)
        top3=puesto[:3]
        
        for corredor in top3:
            tabla.add_row(
                corredor["num_corredor"],
                corredor["nombre"].upper(),
                corredor["apellido"].upper(),
                corredor["tiempo"],
                corredor["categoria"],
                corredor["distancia"]
            )

        console.print(tabla)
    
def metricas(resultados):

    """     Función de métricas varias.  """


    if not resultados:
        console.print("[red]No hay resultados disponibles para calcular métricas.[/red]")
        return
    distancias= ["7","15"]

    #Recorremos en las distancias disponibles para calcular métricas
    for distancia in distancias:
        resultado = [r for r in resultados if (r["distancia"]).strip() == distancia]
        if not resultado:
            console.print(f"[red]No hay resultados para {distancia} km[/red]")
            continue

        tiempos = [tiempo_seg(r["tiempo"]) for r in resultado]

        tiempos_np= np.array(tiempos)

        tiempo_promedio=str(round(np.mean(tiempos_np)/60,2))
        tiempo_minimo=str(round(np.max(tiempos_np)/60,2))
        tiempo_maximo=str(round(np.min(tiempos_np)/60,2))

    
    #Creamos tabla para mejor visualizacíon

        tabla = Table(title=f" Métricas Resultadoos - {distancia}KM", box=None)
        tabla.add_column("Métrica", style="cyan")
        tabla.add_column("Valor", style="yellow")

        tabla.add_row("Promedio de tiempos: ", tiempo_promedio)
        tabla.add_row("Peor tiempo: ", tiempo_minimo)
        tabla.add_row("Mejor tiempo: ", tiempo_maximo)

        console.print(Panel(tabla, border_style="green", title="Estadísticas Generales"))
                
def graficar_histogramas(resultados):

    """Función donde muestra histograma de relación tiempo/cantidad corredores"""    

    for distancia in ["7", "15"]:
        tiempos = [tiempo_seg(r["tiempo"]) / 60 for r in resultados if str(r["distancia"]).strip() == distancia]
        plt.hist(tiempos, bins=10, alpha=0.6, label=f"{distancia}K")

    plt.xlabel("Tiempo (minutos)")
    plt.ylabel("Cantidad de corredores")
    plt.title("Histograma de tiempos por distancia")
    plt.legend()
    plt.grid(True)
    plt.show()       


    


    


