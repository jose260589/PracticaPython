#directiva normal, se usa para llamar las funciones de otro modulo
"""
import funciones_matematicas

funciones_matematicas.sumar(7,10)
funciones_matematicas.restar(7,10)
funciones_matematicas.multiplicar(7,10)
"""

# otra forma de usar otras funciones
"""from funciones_matematicas import sumar

sumar(7,5)"""
"""
el problema con esta que si se quiere usar otra funciones hay que importarla.
"""

#tercera forma es igual solo se usa el *
from funciones_matematicas import *

sumar(7,5)
restar(17,10)
multiplicar(7,10)
