import sys

from interpreter.lexer import Lexer
from interpreter.parsing import Parser
from browser.browser_run import browser_run


try:
  program_path = sys.argv[1]
  program_lines = open(program_path, 'r').readlines()

  lexer = Lexer(program_lines)
  tokens = lexer.build()

  parser = Parser(tokens)
  parse_tree = parser.build()

  print(parse_tree)
  # browser_run(parse_tree)
except Exception as e:
  print("Error:", e)
