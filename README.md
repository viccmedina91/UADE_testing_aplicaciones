# Instalación
1. Instalar Python en el sistema operativo tal cual se detalla en el siguiente link \
[Link de instalación de Python](https://www.python.org/downloads/)

2. Abrimos la terminal de Windows y nos aseguramos que la instalación se ha realizado de manera correcta con el siguiente comando: \
`python --version`
`Python 3.11.3`

3. Verificamos que tenemos instalado el módulo pip de Python con el siguiente comando: \
`pip --version`
`pip 22.3.1 from C:\Users\Victoria\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)`

4. Instalamos el módulo virtualenv que nos permitirá trabajar en el proyecto de forma aislada: \
`pip install virtualenv`

Verificamos la instalación con el siguiente comando: \
`pip list`
`Package      Version`
`------------ -------`
`virtualenv   20.23.0`

5. Instalamos la consola bash de github, los pasos se detallan en el siguiente sitio: \
[Descarga de GitHub](https://gitforwindows.org/)
---

# Configuración del entorno

1. Clonamos el respositorio con el comando: \
`git clone  https://github.com/viccmedina91/UADE_testing_aplicaciones.git`

2. Ingresamos a la carpeta del proyecto.

3. Creamos el entorno virtual con el siguiente comando: \
`python -m venv testing`

4. Activamos el entorno virutal: \
`testing\Scripts\activate.bat`

A mano izquierda nos aparecerá el nombre del entorno creado. En mi caso es:

`(testing) C:\Users\Victoria\tpo_testing>`

5. Instalamos los requerimientos del proyecto: \
`pip install -r requeriments.txt`

6. Ejecutamos el siguiente comando para correr el test de prueba: \
`python test_prueba.py`

Si todo sale bien, se espera que una salida como esta: \
`Ran 1 test in 4.808s `

`OK`