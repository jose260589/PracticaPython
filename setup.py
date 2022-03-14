# con esto se crean paquetes distribuibles, video 36
"""
en la carpeta que se usa como raiz de python se crea el archivo
'setup.py', con las siguientes caracteristicas.
"""

from setuptools import setup

setup(
    # * obligatorio, - opcional
    name="paquetescalculos", #nombre de los paquetes *
    version="1.0", #version de los paquetes *
    descripcion="Paquete de redondeo y potencia",#descripcion *
    author="Juan",#autor o quien los creo *
    author_email="jose260589@yahoo.com", # correo autor -
    url="",# pagina wed -
    packages=["calculos","calculos.redondeo_potencia"]# direccion de los paquetes *

    )

"""
despues de realizar o llenar correctamente lo de arriva,
se usa ya sea el cmd o el shell de python para llegar a la carpeta
donde estan los archivos de python.

luego de esto, se ejecuta el comando:
python setup.py sdist
programa, nombre archivo, comando

si no hubo errores, crea dos carpetas
una con el nombre del paquete o lo que dice en name
y la otra que es la importante con el nombre "dist" en el cual
estara el paquete.

para instalarlo
se puede usar la consola
comando
pip3 install nombre del paquete


para desinstalar un paquete
se usa este comando.
pip3 uninstall nombre del paquete.
"""
