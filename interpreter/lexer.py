from interpreter.token import *
import re


# Lexical analyzer: receives a program input and returns a list of tokens.
class Lexer:
  def __init__(self, program_lines):
    self.program_lines = program_lines

  # build a list of tokens
  def build(self):
    tokens = []

    for i, line in enumerate(self.program_lines):

      # skipping lines that start with '//', which are comments
      if line.startswith('//'):
        continue

      while line != '':
        # skipping white spaces, tabs or break lines
        if line[0] in [' ', '\t', '\n']:
          line = line[1:]
          continue

        match_found = False

        # check if we can do some match from token specification
        for pattern in PATTERNS:
          type = pattern[0]
          regex = pattern[1]
          match = re.match(regex, line)

          if match:
            # if matches, create a token and drop the matched part of program line
            tokens.append(Token(type, match.group()))
            line = line[match.end():]
            match_found = True
            break
        
        # if we can't do any match from token specification, raises an error
        if not match_found:
          split_index = re.search('[\s\t\n]|$', line).start()
          invalid_token = line[:split_index]

          raise Exception(f'token not recognized at line {i + 1} - "{invalid_token}")')

    return tokens
