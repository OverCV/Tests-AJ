import openpyxl
from src.controllers.manager import Manager
from src.testing.data import (
    NUM_NODOS,
    PRUEBAS,
    RED_10,
    RED_15,
    RED_20,
    RED_22,
    RED_23,
    RED_25,
)
from src.models.base.application import aplicacion
from src.models.core.solution import Solution
from mpi4py import MPI

# ESTRATEGIAS #

from src.controllers.strategies.q_nodes import QNodes as QNodesMPI


# CONSTANTES #

fila_inicial = 3
cols_qnodes = ["I", "J", "K"]


def iniciar_pruebas_mpi():
    red_selecta = RED_15
    columnas = cols_qnodes
    preparar_pruebas(red_selecta, columnas)


def preparar_pruebas(red_selecta, columnas):
    nodos = red_selecta[NUM_NODOS]
    pruebas = red_selecta[PRUEBAS]

    estado_inicial = "1" + "0" * (nodos - 1)
    condiciones = "1" * nodos

    gestor_redes = Manager(estado_inicial)
    analizador = QNodesMPI(gestor_redes)

    inicio: int = 16
    iterador: int = 0

    for bloque in pruebas:
        print()
        for alcance, mecanismo in bloque:
            comm = MPI.COMM_WORLD
            rank = comm.Get_rank()
            sia = analizador.aplicar_estrategia(
                condiciones,
                alcance,
                mecanismo,
            )

            if iterador < inicio:
                continue

            iterador += 1

            if not rank:
                # Analizamos el proceso maestro
                # print("nueva prueba")
                perdida, particion, tiempo = (
                    sia.perdida,
                    sia.particion,
                    sia.tiempo_ejecucion,
                )
                # print(perdida, particion, tiempo)

                # Guardar resultados inmediatamente en Excel
                guardar_qnodes_en_excel(perdida, particion, tiempo, nodos, columnas)

                # Limpiar memoria para que no afecte siguientes pruebas
                del sia
                # analizador.limpiar_memoria()
            else:
                # Si el objeto retornado no es de tipo Solution, significa que el proceso no es el maestro y por lo tanto no se debe guardar ningún resultado
                continue

            # break
        # break

    # print(resultados)


def guardar_qnodes_en_excel(perdida, particion, tiempo, numero_nodos, columnas):
    """Guarda los resultados eficientemente en F3-H3 y filas siguientes"""
    archivo_excel = "src/testing/PruebasIniciales.xlsx"

    # Primera fila vacía desde F3
    global fila_inicial
    fila = fila_inicial

    try:
        # Abrir Excel existente
        workbook = openpyxl.load_workbook(archivo_excel)
        hoja = workbook[f"{numero_nodos}{aplicacion.pagina_sample_network}-Elementos"]

        # Escribir directamente en las celdas según la estrategia
        primera, segunda, tercera = columnas
        hoja[f"{primera}{fila}"] = perdida
        hoja[f"{segunda}{fila}"] = particion[:-1]  # ignoramos último '\n'
        hoja[f"{tercera}{fila}"] = tiempo

        # Guardar cambios
        workbook.save(archivo_excel)
        workbook.close()

        fila_inicial += 1

    except Exception as e:
        print(f"Error guardando en Excel: {e}")
        # Fallback simple
        with open("resultados_backup.txt", "a") as f:
            f.write(f"{perdida},{particion},{tiempo}\n")
