from lexer import Lexer
from parsing import Parser
from execution import run_tree

program_input = "loop 1 navegador https://videoconferencia 15_min navegador 20_min navegador https://whatsapp 1_hora"

try:
  lexer = Lexer(program_input)
  tokens = lexer.build()

  parser = Parser(tokens)
  parse_tree = parser.build()

  run_tree(parse_tree)
except Exception as e:
  print("Error:", e)
