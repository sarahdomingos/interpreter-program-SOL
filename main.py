from interpreter.lexer import Lexer
from interpreter.parsing import Parser
from interpreter.run_tree import run_tree


# program_input = 'loop 1 navegador pdf:"/home/allan/Documents/file.pdf" 15_min navegador video:"selena gomez" 1_hora navegador videoconferencia no_limit navegador whatsapp 2_dias navegador email:"allancslima@gmail.com" 20_min'
program_input = 'loop 1 navegador video:"como fazer um pudim" 15_min'

try:
  lexer = Lexer(program_input)
  tokens = lexer.build()

  parser = Parser(tokens)
  parse_tree = parser.build()

  run_tree(parse_tree)
except Exception as e:
  print("Error:", e)
