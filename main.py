from lexer import Lexer
from parsing import Parser


program_input = "loop 1 navegador https://videoconferencia 15_min navegador 20_min navegador https://whatsapp 1_hora"

try:
  lexer = Lexer(program_input)
  tokens = lexer.build()

  parser = Parser(tokens)
  print(parser.run())
except Exception as e:
  print("Error:", e)
