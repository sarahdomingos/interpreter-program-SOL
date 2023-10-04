# All token types.
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

# Token specification relating token types to its patterns.
PATTERNS = [
    (TT_LOOP,    'loop'),
    (TT_BROWSER, 'navegador'),
    (TT_VEZES,   '[1-5]\\b'),
    (TT_TEMPO,   '(15_min|20_min|1_hora|2_dias|no_limit|10s)'),
    (TT_LINK_PDF,              'pdf:".+\\.pdf"'),
    (TT_LINK_VIDEO,            'video:"[\\w\\s]*"'),
    (TT_LINK_VIDEOCONFERENCIA, 'https:\/\/meet\.google\.com\/[a-z]{3}-[a-z]{4}-[a-z]{3}'),
    (TT_LINK_WHATSAPP_WEB,     'whatsapp'),
    (TT_LINK_EMAIL,            'email:"[a-z0-9\\.-]+@[a-z]+(\.[a-z]{2,})+"'),
]


# Represents a token by receiving its type and value.
class Token:
  def __init__(self, type, value):
    self.type = type
    self.value = value

  def __repr__(self):
    return f'({self.type},{self.value})'
