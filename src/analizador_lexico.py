import ply.lex as lex
# Definir los tokens
tokens = (
    'CANTIDAD',
    'ORIGEN',
    'DESTINO',
    'FIN',
)

# Definir las expresiones regulares para cada token
t_CANTIDAD = r'\d+\.?\d+'
t_ORIGEN = r'DólarEstadounidense|LempiraHondureño|Euro'
t_DESTINO = r'LempiraHondureño|DólarEstadounidense|Euro'
t_FIN = r'\bfin\b'

# Ignorar espacios en blanco y saltos de línea
t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character '{t.value[0]}' at position {t.lexpos}")
    t.lexer.skip(1)  # O bien, puedes usar t.lexer.skip(n) para ignorar n caracteres

# Crear el lexer
lexer = lex.lex()

def analizar_lexico(entrada):
    print("Entrada analizador lexico", entrada)
    lexer.input(entrada)
    tokensFinales = []
    cont = 0
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokensFinales.append((tokens[cont], tok.value))
        cont = cont + 1
    return tokensFinales
