from interpreter.lexer import Lexer
from interpreter.parsing import Parser
from interpreter.run_tree import run_tree
from PySimpleGUI import PySimpleGUI as sg

try:
  program = open('program.sol', 'r').readlines()
  #print(type(program))
  #program = list('navegador 10s')
  lexer = Lexer(program)
  tokens = lexer.build()

  parser = Parser(tokens)
  parse_tree = parser.build()

  run_tree(parse_tree)
except Exception as e:
  print("Error:", e)
