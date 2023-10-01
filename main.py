from lexer import Lexer
from parsing import Parser

text = "loop 1 navegador https://videoconferencia 15_min navegador 20_min navegador https://whatsapp 1_hora"
lexer = Lexer(text)
tokens = lexer.build()

parser = Parser(tokens)
print(parser.run())