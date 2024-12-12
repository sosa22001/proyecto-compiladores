import ply.yacc as yacc
from analizador_lexico import tokens

# Reglas de la gramática
def p_instruccion(p):
    '''instruccion : CANTIDAD ORIGEN DESTINO FIN'''
    p[0] = [("Cantidad", float(p[1])), ("Origen", p[2]), ("Destino", p[3]), ("Fin", p[4])]

def p_error(p):
    print("Error sintáctico: Entrada inválida.")

# Crear el parser
parser = yacc.yacc(debug=True)  # Habilitar depuración para generar el informe de estados

# Función para analizar sintácticamente
def analizar_sintactico(entrada):
    return parser.parse(entrada)
