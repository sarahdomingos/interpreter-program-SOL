import re


#
# All token types.
#
TT_EPSILON = 'EPSILON'
TT_LOOP    = 'LOOP'
TT_VEZES   = 'VEZES'
TT_BROWSER = 'BROWSER'
TT_TEMPO   = 'TEMPO'
TT_LINK_PDF              = 'LINK_PDF'
TT_LINK_VIDEO            = 'LINK_VIDEO'
TT_LINK_VIDEOCONFERENCIA = 'LINK_VIDEOCONFERENCIA'
TT_LINK_WHATSAPP_WEB     = 'LINK_WHATSAPP_WEB'
TT_LINK_EMAIL            = 'LINK_EMAIL'


#
# Token specification relating token types to its patterns.
#
PATTERNS = [
    (TT_LOOP,    'loop'),
    (TT_BROWSER, 'navegador'),
    (TT_VEZES,   '[1-5]\\b'),
    (TT_TEMPO,   '(15_min|20_min|1_hora|2_dias|no_limit)'),
    (TT_LINK_PDF,              'pdf:".+\\.pdf"'),
    (TT_LINK_VIDEO,            'video:"[\\w\\s]*"'),
    (TT_LINK_VIDEOCONFERENCIA, 'videoconferencia'),
    (TT_LINK_WHATSAPP_WEB,     'whatsapp'),
    (TT_LINK_EMAIL,            'email:"[a-z0-9\\.-]+@[a-z]+(\.[a-z]{2,})+"'),
]


#
# Represents a token by receiving its type and value.
#
class Token:
  def __init__(self, type, value):
    self.type = type
    self.value = value

  def __repr__(self):
    return f'({self.type},{self.value})'


#
# Lexical analyzer: receives a program input and returns a list of tokens.
#
class Lexer:
  def __init__(self, text):
    self.text = text

  def build(self):
    tokens = []
    input = self.text

    while input != '':

      # skipping white spaces or tabs
      if input[0] in [' ', '\t']:
        input = input[1:]
        continue

      match_found = False

      # check if we can do some match from token specification
      for pattern in PATTERNS:
        type = pattern[0]
        regex = pattern[1]
        match = re.match(regex, input)
        
        if match:
          # if matches, create a token and drop the matched part of program input
          tokens.append(Token(type, match.group()))
          input = input[match.end():]
          match_found = True
          break
      
      # if we can't do any match from token specification, raises an error
      if not match_found:
        raise Exception(f'token not recognized ("{input}")')

    return tokens
