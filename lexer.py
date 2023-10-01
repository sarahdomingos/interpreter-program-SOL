import re


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


PATTERNS = [
    (TT_LOOP,    'loop'),
    (TT_BROWSER, 'navegador'),
    (TT_TEMPO,   '(15_min|20_min|1_hora|2_dias|no_limit)'),
    (TT_VEZES,   '[1-5]'),
    (TT_LINK_PDF,              'https://pdf'),
    (TT_LINK_VIDEOCONFERENCIA, 'https://videoconferencia'),
    (TT_LINK_VIDEO,            'https://video'),
    (TT_LINK_WHATSAPP_WEB,     'https://whatsapp'),
    (TT_LINK_EMAIL,            'https://email'),
]


class Token:
  def __init__(self, type, value):
    self.type = type
    self.value = value

  def __repr__(self):
    return f'({self.type},{self.value})'

class Lexer:
  def __init__(self, text):
    self.text = text

  def build(self):
    tokens = []
    input = self.text

    while input != '':
      if input[0] in [' ', '\t']:
        input = input[1:]
        continue

      match_found = False

      for pattern in PATTERNS:
        type = pattern[0]
        regex = pattern[1]
        match = re.match(regex, input)
        
        if match:
          tokens.append(Token(type, match.group()))
          input = input[match.end():]
          match_found = True
          break
      
      if not match_found:
        raise Exception('token not recognized!')

    return tokens
