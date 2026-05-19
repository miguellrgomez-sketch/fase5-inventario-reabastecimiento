"""
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Fundamentos de Programacion
Codigo: 213022
Fase 5 - Evaluacion Final POA

Problema 3: Auditoria de inventario y reabastecimiento
Estudiante: Miguel Angel Gomez Ramos
Grupo: 213022B_2201

Descripcion:
El programa analiza una matriz de inventario con el formato:
[Codigo Articulo, Nombre, Stock Actual, Stock Minimo Requerido].
Para cada articulo calcula la cantidad exacta que debe solicitarse.
"""


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Calcula la cantidad exacta que debe pedirse para un articulo.

    Regla de negocio:
    - Si el stock actual es menor que el stock minimo, se pide la diferencia.
    - Si el stock actual es mayor o igual al stock minimo, no se pide nada.
    """
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0

    return cantidad


def generar_informe_pedidos(inventario):
    """
    Recorre la matriz de inventario y genera una nueva lista con el resultado
    de la cantidad a pedir para cada articulo.
    """
    informe = []

    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        informe.append([codigo, nombre, stock_actual, stock_minimo, cantidad_pedir])

    return informe


def mostrar_informe(informe):
    """
    Muestra en pantalla el informe final de reabastecimiento.
    """
    print("=" * 78)
    print("INFORME DE AUDITORIA DE INVENTARIO Y REABASTECIMIENTO")
    print("=" * 78)
    print(f"{'Codigo':<10}{'Articulo':<22}{'Stock actual':<15}{'Stock minimo':<15}{'Pedir':<10}")
    print("-" * 78)

    for item in informe:
        codigo = item[0]
        nombre = item[1]
        stock_actual = item[2]
        stock_minimo = item[3]
        cantidad_pedir = item[4]

        print(f"{codigo:<10}{nombre:<22}{stock_actual:<15}{stock_minimo:<15}{cantidad_pedir:<10}")

    print("-" * 78)

    articulos_a_pedir = 0
    total_unidades = 0

    for item in informe:
        if item[4] > 0:
            articulos_a_pedir = articulos_a_pedir + 1
            total_unidades = total_unidades + item[4]

    print(f"Articulos que requieren reabastecimiento: {articulos_a_pedir}")
    print(f"Total de unidades a solicitar: {total_unidades}")
    print("=" * 78)


def main():
    """
    Funcion principal del programa.
    Contiene la matriz inicial y llama las funciones necesarias.
    """
    inventario = [
        ["A001", "Teclado", 8, 15],
        ["A002", "Mouse", 20, 10],
        ["A003", "Monitor", 4, 8],
        ["A004", "Memoria USB", 25, 25],
        ["A005", "Disco SSD", 3, 12],
        ["A006", "Cable HDMI", 18, 20]
    ]

    informe = generar_informe_pedidos(inventario)
    mostrar_informe(informe)


if __name__ == "__main__":
    main()
