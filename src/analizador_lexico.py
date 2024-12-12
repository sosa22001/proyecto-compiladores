import re

def analizar_lexico(entrada):
    print("entrada", entrada)
    # Patrón modificado para manejar separadores por coma
    patron = r"(?P<Cantidad>\d+\.\d+),\s*(?P<Origen>DólarEstadounidense|LempiraHondureño|Euro),\s*(?P<Destino>LempiraHondureño|DólarEstadounidense|Euro)"
    match = re.match(patron, entrada)
    if not match:
        raise ValueError("Error sintáctico: El formato de entrada no coincide con la estructura esperada")
    
    # Retorna los tokens como pares (nombre, valor)
    tokens = [(key, value) for key, value in match.groupdict().items()]
    return tokens

