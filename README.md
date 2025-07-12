# 🏃‍♂️ Race Manager

**Race Manager** es una aplicación simple pero poderosa para la gestión y visualización de datos de una carrera de running. Permite trabajar con información clave como corredores, resultados, categorías y más, facilitando la organización y el análisis de eventos deportivos.

---

## 🌟 ¿Cómo nació este proyecto?

La idea de Race Manager surge de una experiencia personal: haber participado en la organización de carreras de running, colaborando tanto en la **acreditación de participantes** como en la **toma de tiempos y clasificación**.

A partir de eso, me propuse crear una herramienta que no solo facilite el manejo de esos datos, sino que también los **haga más visuales y analizables**. Esto lo logré gracias a conceptos aprendidos en la materia de **Programación**, junto con el uso de bibliotecas como **NumPy**, que permite aplicar estadísticas y organizar la información de manera eficiente.

---

## 🔧 ¿Qué hace el programa?

Inicialmente, Race Manager permite:

- Leer datos desde archivos `.txt` o `.csv`.
- Mostrar información de corredores y categorías.
- Visualizar resultados generales o por categoría.

Próximamente se sumarán funciones como:

- Filtrado de datos específicos.
- Modificación y agregación de nuevos registros.
- Menú interactivo con más opciones para el análisis.
- Exportación o visualización avanzada de resultados.

---

## 🚧 Estado actual

El proyecto se encuentra en una **fase inicial**, con foco en:

- La lectura de archivos.
- La visualización básica de datos.
- Agregación y eliminación de corredores.
- La estructura base de un menú que se irá expandiendo con el tiempo.

A medida que avance, se irán sumando nuevas funcionalidades para brindar un análisis más completo y útil para quienes organizan o participan en eventos de running.

---

## ⚙️ Requisitos  

- Python 3.8 o superior
- Git (opcional, para clonar el repo)

---

## 🔧 Pasos para crear un entorno virtual

---

### 1. Abrir la terminal o consola
Asegúrate de tener Python instalado:

```bash
python --version
# o
python3 --version
```

Si no está instalado, descárgalo desde [https://www.python.org](https://www.python.org).

---

### 🔁 2. Clonar el repositorio (o descargarlo manualmente)

git clone https://github.com/MauriChocho/RaceManager.git

cd RaceManager

---

### 3. Crear el entorno virtual

Ejecuta este comando dentro del directorio de tu proyecto:

```bash
python -m venv nombre_del_entorno
```

Ejemplo:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` con todas las herramientas necesarias para trabajar de forma aislada.

---

### 3. Activar el entorno virtual

#### En Windows:
```bash
source raceManager/.venv/Scripts/activate
```

Después de activarlo, verás algo así en la terminal:
```
(venv) C:\ruta\de\tu\proyecto>
```

#### En macOS / Linux:
```bash
source venv/bin/activate
```

También verás `(venv)` al inicio de la línea de comandos.

---

4. **Instalamos dependencias**

pip install -r requirements.txt

---

5. **Ejecutamos programa**

python main.py

-- Se proporiona unos datos DEMO para hacer pruebas del programa, estos datos pueden ser cargados desde el menú(opción 1)
-- en caso de no tener datos propios aún.