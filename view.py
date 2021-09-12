from helpers import (getConfigData,
                     printInputValues,
                     printSingleTable,
                     printOnConsole)
from DAO import Opcion


@ printInputValues
def getInputOpcion(str_msg):
    is_error = True
    opcion_seleccionada = None
    opciones = getListaOpciones()

    if len(opciones) > 1:
        data_table = []
        data_table.append(["#", "Cod", "Descripción"])
        for opcion in opciones:
            data_table.append([
                opciones.index(opcion) + 1,
                opcion.codigo,
                opcion.descripcion
            ])
        printSingleTable(data_table, " LISTA DE OPCIONES ")

    while is_error:
        is_error = True
        try:
            if len(opciones) > 1:
                indx_opcion_selaccionada = int(input(str_msg))
                if indx_opcion_selaccionada > 0:
                    opcion_selaccionada = opciones[indx_opcion_selaccionada - 1]
                    is_error = False
                else:
                    printOnConsole(
                        "El valor debe ser mayor a Cero ( 0 ).", "w")
            else:
                opcion_selaccionada = opciones[0]
                is_error = False
        except ValueError as verr:
            printOnConsole("El valor ingresado no es númerico.", "w")
        except IndexError as ierr:
            printOnConsole(
                "Debe seleccionar uno de las opciones en la lista.", "w")

    return opcion_selaccionada


def getListaOpciones():
    lista_opciones = []
    data = getConfigData("opciones")

    if len(data["opciones"]) > 0:
        for opcion in data["opciones"]:
            serv = Opcion(
                opcion["codigo"],
                opcion["descripcion"]
            )

            lista_opciones.append(serv)
    else:
        printOnConsole("No existen opciones configuradas.", "e")
        exit()

    return lista_opciones
