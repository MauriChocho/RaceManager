#Impotamos stream error para maneros de errores, path para rutas, rich para mejorar aspectos
from os import strerror,path
from rich.console import Console
from rich.table import Table
from rich import box
import csv,os


console = Console()

def leer_categorias(categorias):
    
    """Mostramos categorias cargadas en archivo csv"""

    tabla =Table(title="Categorías disponibles", box=box.SQUARE)

    tabla.add_column("Nombre", justify="center",style="green", no_wrap=True)
    tabla.add_column("Edad min",style="green")
    tabla.add_column("Edad max",style="green")
    tabla.add_column("Género",style="green")
    

    for categoria in categorias:
        tabla.add_row(
            str(categoria["nombre"]),
            str(categoria["edad_min"]),
            str(categoria["edad_max"]),
            str(categoria["genero"]),
    )
    console.print(tabla)
    
    


