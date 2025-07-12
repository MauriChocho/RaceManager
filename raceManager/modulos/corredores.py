#Impotamos stream error para maneros de errores, path para rutas, rich para mejorar aspectos
from os import strerror,path
from rich.console import Console
from rich.table import Table
from rich import box
import csv,os
from datetime import datetime

console = Console()

def guardar_corredores(corredores, archivo="data/corredores.csv"):
    """
    Guarda la lista completa de corredores en el archivo CSV, 
    sobrescribiendo cualquier contenido anterior.
    """

    campos = ["id", "nombre", "apellido", "num_corredor", "fecha_nac", "edad", "genero", "categoria", "distancia"]

    with open(archivo, "w", newline='', encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(corredores)


def leer_corredores(corredores):
    
    """
        Mostramos corredores de nuestro 
        data ordenados por id
    """
        

    #Chequeamos si tenemos algun corredor para mostrar
    if not corredores:
        console.print("[bold red] No hay corredores para mostrar.[/bold red]")
        return

    #Creamos tabla 
    tabla = Table(title="Corredores Registrados", box=box.SIMPLE)

    tabla.add_column("ID", justify="right", style="cyan", no_wrap=True)
    tabla.add_column("Nombre", style="bold magenta")
    tabla.add_column("Apellido", style="bold magenta")
    tabla.add_column("Numero corredor", style="yellow")
    tabla.add_column("Fecha Nacimiento", style="green")
    tabla.add_column("Edad", style="bright_cyan")
    tabla.add_column("Genero", style="yellow")
    tabla.add_column("Categoría", style="green")
    tabla.add_column("Distancia", style="bright_cyan")

    for corredor in corredores:
        tabla.add_row(
        str(corredor["id"]),
        str(corredor["nombre"].upper()),
        str(corredor["apellido"].upper()),
        str(corredor["num_corredor"]),
        str(corredor["fecha_nac"]),
        str(corredor["edad"]),
        str(corredor["genero"].upper()),
        str(corredor["categoria"]),
        str(corredor["distancia"]),
    )

    console.print(tabla)


def calcular_edad(fecha_nac):

    """
    Funcíon para calcular la edad del corredor con su fecha de nacimiento 
      esto nos asegura menos inconsistencias en los datos ingresados

    """

    fecha_nac = datetime.strptime(fecha_nac, "%Y-%m-%d")
    hoy = datetime.today()
    edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
    return edad


def asignar_categoria(genero,edad):
     
     """
     Asigna categoria según la edad y género,
     Esto permite una carga de corredores mas fluida

     """

     if genero.upper()== 'F':
         if 0 < edad <= 19:
          return "F0-19"
         elif 20<= edad<=29:
           return "F20-29"
         elif 30<= edad<=39:
           return "F30-39"
         elif 40<= edad<=49:
           return "F40-49"
         elif 50<= edad<=59:
           return "F50-59"
         else:
             return "F50+"
     elif genero.upper()== 'M':
        if 0 < edad <= 19:
          return "M0-19"
        elif 20<= edad<=29:
           return "M20-29"
        elif 30<= edad<=39:
           return "M30-39"
        elif 40<= edad<=49:
           return "M40-49"
        elif 50<= edad<=59:
           return "M50-59"
        else:
             return "M50+"


def agregar_corredor(corredores,nombre,apellido,fecha_nac,genero,distancia):

        """
        Función donde agregamos nuevos corredores

        """

        #Llamamos nuestras funciones 'especiales' para agregar estos datos calculados
        edad = calcular_edad(fecha_nac)
        categoria = asignar_categoria(genero, edad)

        #Agregamos un ID nuevo
        nuevoId= 1
        if corredores:
            ultimo_id = int(corredores[-1]['id'])
            nuevoId = ultimo_id + 1

        #Cargamos datos del nuevo corredor
        corredor={
             'id':nuevoId,
             'nombre': nombre,
             'apellido': apellido,
             'num_corredor': nuevoId+15,
             'fecha_nac':fecha_nac,
             'edad': edad,
             'genero':genero,
             'categoria': categoria,
             'distancia': distancia

        }
        corredores.append(corredor)


        #REESCRIBIMOS NUESTRO ARCHIVO corredores.CSV PARA ACTUALIZARLO

        with open("data/corredores.csv", "a", newline='', encoding="utf-8") as archivo:
            campos = ["id", "nombre", "apellido", "num_corredor","fecha_nac","edad","genero","categoria","distancia"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            if os.stat("data/corredores.csv").st_size == 0:
                escritor.writeheader()
            escritor.writerow(corredor)


def eliminar_corredor(corredores, id_eliminar):
   """
    Función donde eliminamos a un corredor selecionado con su ID
   
   """
    #Buscamos id a eliminar
   for corredor in corredores:
      if int(corredor["id"])== id_eliminar:
        corredores.remove(corredor)

        #Renumeramos corredores, manteniendo su numero de corredor y ordenando datos internamente
        for indice, corredor in enumerate(corredores, start=1):
                corredor["id"]=indice


#Al igual que agregarCorredor, actualizamos IDs del listado 

        with open("data/corredores.csv", "w", newline='', encoding="utf-8") as archivo:
                campos = ["id", "nombre", "apellido", "num_corredor","fecha_nac","edad","genero","categoria","distancia"]
                escritor = csv.DictWriter(archivo, fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(corredores)
        return True  
   return False


