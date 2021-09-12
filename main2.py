from helpers import (preInit,
                     printOnConsole,
                     executeOnBucle)
from view import *
from controller import *
from DNAToolkit import *
from utilities import colored


@ executeOnBucle
def main():
    preInit()

    opcion = getInputOpcion("Opción: ")

    if opcion.codigo == '01':
        #print(f"Seleccionó la opción {opcion.codigo} - {opcion.descripcion}")
        imprimirDNATabla()


if __name__ == '__main__':
    try:
        main()
    except(KeyboardInterrupt, EOFError, AttributeError):
        printOnConsole("\n[  PROGRAMA FINALIZADO POR EL USUARIO  ]")
