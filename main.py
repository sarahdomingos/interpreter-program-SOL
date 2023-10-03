from interpreter.lexer import Lexer
from interpreter.parsing import Parser
from interpreter.run_tree import run_tree


try:
  program = open('program.sol', 'r').readlines()

  lexer = Lexer(program)
  tokens = lexer.build()

  parser = Parser(tokens)
  parse_tree = parser.build()

  run_tree(parse_tree)
except Exception as e:
  print("Error:", e)
