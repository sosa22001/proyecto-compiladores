import pydot
from IPython.display import Image, display

# Función para analizar la sintaxis (validar estructura esperada de los tokens)
def analizar_sintaxis(tokens):
    """
    Analiza la sintaxis de los tokens generados.
    :param tokens: Lista de tuplas con formato (tipo, valor)
    :return: Booleano indicando si la sintaxis es válida.
    """
    estructura_esperada = ["Cantidad", "Origen", "Destino"]
    tipos_tokens = [tipo for tipo, _ in tokens]

    if tipos_tokens == estructura_esperada:
        return True
    else:
        print(f"Error sintáctico: Se esperaba la estructura {estructura_esperada}, pero se obtuvo {tipos_tokens}")
        return False

# Función para generar el árbol sintáctico
def generar_arbol(tokens):
    """
    Genera un árbol sintáctico a partir de los tokens.
    :param tokens: Lista de tuplas con formato (tipo, valor)
    :return: Objeto de gráfico Pydot
    """
    graph = pydot.Dot("arbol_sintactico", graph_type="digraph", rankdir="TB")
    inicio = pydot.Node("Inicio", shape="circle", style="filled", fillcolor="lightblue")
    graph.add_node(inicio)

    for i, (tipo, valor) in enumerate(tokens):
        nodo = pydot.Node(f"{tipo}: {valor}", shape="box", style="rounded,filled", fillcolor="lightgrey")
        graph.add_node(nodo)
        graph.add_edge(pydot.Edge(inicio, nodo))
    
    return graph

# Función para mostrar el árbol visualmente
def mostrar_arbol(arbol):
    """
    Muestra el árbol generado como imagen PNG.
    :param arbol: Objeto de gráfico Pydot
    """
    arbol.write_png("arbol.png")
    display(Image(filename="arbol.png"))
