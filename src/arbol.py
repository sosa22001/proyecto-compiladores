# arbol.py
import pydot
from PIL import Image as PILImage, ImageTk
import tkinter as tk

def generar_arbol(tokens):
    graph = pydot.Dot("arbol_sintactico", graph_type="digraph", rankdir="TB")
    
    # Nodo raíz
    Inicio = pydot.Node("Inicio", shape="ellipse", style="filled", fillcolor="lightblue")
    graph.add_node(Inicio)

    # Nodo para cada tipo de token y su valor
    for tipo, valor in tokens:
        nodo_token = pydot.Node(f"{tipo}", shape="box", style="rounded,filled", fillcolor="lightgrey")
        graph.add_node(nodo_token)
        
        nodo_valor = pydot.Node(f"{valor}", shape="box", style="rounded,filled", fillcolor="lightyellow")
        graph.add_node(nodo_valor)
        
        graph.add_edge(pydot.Edge(nodo_token, nodo_valor))
        graph.add_edge(pydot.Edge(Inicio, nodo_token))

    return graph

def mostrar_arbol(arbol, ventana):
    arbol.write_png("arbol_sintactico.png")
    
    ventana_arbol = tk.Toplevel(ventana)
    ventana_arbol.title("Árbol Sintáctico")
    
    img = PILImage.open("arbol_sintactico.png")
    img = ImageTk.PhotoImage(img)
    
    label_img = tk.Label(ventana_arbol, image=img)
    label_img.image = img
    label_img.pack()
