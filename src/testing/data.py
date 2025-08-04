from typing import Union

import numpy as np


PRUEBAS = "pruebas"
NUM_NODOS = "num_nodos"


RED_10: dict[
    str,
    Union[int, list[list[tuple[str, str]]]],
] = {
    NUM_NODOS: 10,
    PRUEBAS: [
        [
            ("1111111111", "1111111111"),
            ("1111111111", "1111111110"),
            ("1111111111", "0111111111"),
            ("1111111111", "0111111110"),
            ("1111111111", "1101101101"),
            ("1111111111", "1010101010"),
            ("1111111111", "0101010101"),
        ],
        [
            ("1111111110", "1111111111"),
            ("1111111110", "1111111110"),
            ("1111111110", "0111111111"),
            ("1111111110", "0111111110"),
            ("1111111110", "1101101101"),
            ("1111111110", "1010101010"),
            ("1111111110", "0101010101"),
        ],
        [
            ("0111111111", "1111111111"),
            ("0111111111", "1111111110"),
            ("0111111111", "0111111111"),
            ("0111111111", "0111111110"),
            ("0111111111", "1101101101"),
            ("0111111111", "1010101010"),
            ("0111111111", "0101010101"),
        ],
        [
            ("0111111110", "1111111111"),
            ("0111111110", "1111111110"),
            ("0111111110", "0111111111"),
            ("0111111110", "0111111110"),
            ("0111111110", "1101101101"),
            ("0111111110", "1010101010"),
            ("0111111110", "0101010101"),
        ],
        [
            ("1101101101", "1111111111"),
            ("1101101101", "1111111110"),
            ("1101101101", "0111111111"),
            ("1101101101", "0111111110"),
            ("1101101101", "1101101101"),
            ("1101101101", "1010101010"),
            ("1101101101", "0101010101"),
        ],
        [
            ("1010101010", "1111111111"),
            ("1010101010", "1111111110"),
            ("1010101010", "0111111111"),
            ("1010101010", "0111111110"),
            ("1010101010", "1101101101"),
            ("1010101010", "1010101010"),
            ("1010101010", "0101010101"),
        ],
        [
            ("0101010101", "1111111111"),
            ("0101010101", "1111111110"),
            ("0101010101", "0111111111"),
            ("0101010101", "0111111110"),
            ("0101010101", "1101101101"),
            ("0101010101", "1010101010"),
            ("0101010101", "0101010101"),
        ],
    ],
}


def generar_subarreglos(arr) -> list[list[int]]:
    return [
        arr,  # 1. Todo el arreglo original
        arr[:-1],  # 2. Excluir el último elemento
        arr[1:],  # 3. Excluir el primer elemento
        arr[1:-1],  # 4. Excluir los extremos
        np.delete(arr, np.arange(2, len(arr), 3)),  # 5. Omitir múltiplos de 3
        arr[::2],  # 6. Tomar los elementos en posiciones pares
        arr[1::2],  # 7. Tomar los elementos en posiciones impares
    ]


def generar_dataset(num_nodos: int) -> list[list[tuple[str, str]]]:
    variables = range(num_nodos)
    pruebas = []

    for futuro in generar_subarreglos(variables):
        conjunto = []

        futuro = set(futuro)
        for presente in generar_subarreglos(variables):
            # Para vista binaria
            presente = set(presente)
            bits_alcance = "".join(["1" if j in futuro else "0" for j in variables])
            bits_mecanismo = "".join(["1" if i in presente else "0" for i in variables])
            conjunto.append((bits_alcance, bits_mecanismo))

        pruebas.append(conjunto)

    return pruebas


RED_15 = {
    NUM_NODOS: 15,
    PRUEBAS: generar_dataset(15),
}

RED_20 = {
    NUM_NODOS: 20,
    PRUEBAS: generar_dataset(20),
}

RED_22 = {
    NUM_NODOS: 22,
    PRUEBAS: generar_dataset(22),
}

RED_23 = {
    NUM_NODOS: 23,
    PRUEBAS: generar_dataset(23),
}

RED_25 = {
    NUM_NODOS: 25,
    PRUEBAS: generar_dataset(25),
}
