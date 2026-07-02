
#Importa ANTLR para funciones 
from antlr4 import *
from ExprLexer import ExprLexer
import sys

# libreria para leer archivos
#Lo que obtiene es la entrada, analiza el texto y lo separa en tokens

input_stream = FileStream(sys.argv[1])

lexer = ExprLexer(input_stream) # en vez de leer la terminal, lee el archivo que le pasas como argumento al script
# toma los tokens que produjo el lexer y los guarda en un flujo/lista

tokens = CommonTokenStream(lexer)
tokens.fill()

print(tokens)

for token in tokens.tokens:
    print("Texto: ", token.text)
    print("Tipo: ", token.type)
    print("Línea: ", token.line)
    print("Columna: ", token.column)
    nombre_token = lexer.symbolicNames[token.type]
    #te da el nombre del tipo de token que es, por ejemplo NUM, MAS, etc

    print("Nombre del token: ", nombre_token)
    print("___________________")