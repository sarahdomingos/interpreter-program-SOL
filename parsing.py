from lexer import *


#
# Syntax analyzer: a recursive top-down implementation.
#
# Note: Problems like ambiguity and left recursion were solved in grammar. See: grammar.txt
#
class Parser:
  def __init__(self, tokens):
    self.tokens = tokens

  def run(self):
    return self.PROGRAMA_SOL()

  # returns True if we can consume the given type in the list of tokens, False otherwise
  def consume(self, type):
    if len(self.tokens) == 0:
      return type == TT_EPSILON

    if self.tokens[0].type == type:
      self.tokens.pop(0)
      return True

    return False

  # make a backtracking to the current state if some derivation function fails
  def backtracking(self, functions):
    current_state = self.tokens.copy()

    while functions:
      if functions.pop(0)():
        return True
      else:
        self.tokens = current_state.copy()

    return False

  ## NON-TERMINALS

  def PROGRAMA_SOL(self):
    return self.consume(TT_LOOP) and self.VEZES() and self.SEQUENCIA()

  def SEQUENCIA(self):
    return self.FASES_EPIC() and self.SEQUENCIA_1()

  def FASES_EPIC(self):
    return self.backtracking([
      self.EXPLORE,
      self.PRESENT,
      self.INTERACT,
      self.CRITIQUE,
    ])

  def SEQUENCIA_1(self):
    return self.consume(TT_EPSILON) or self.SEQUENCIA()

  def EXPLORE(self):
    return self.BROWSER() and self.TEMPO()

  def PRESENT(self):
    return self.backtracking([
      self.VISUALIZAR_PDF,
      self.VISUALIZAR_VIDEO,
      self.VIDEOCONFERENCIA,
    ]) and self.TEMPO()

  def INTERACT(self):
    return self.backtracking([
      self.WHATSAPP_WEB,
      self.EMAIL,
      self.VIDEOCONFERENCIA,
    ]) and self.TEMPO()

  def CRITIQUE(self):
    return self.backtracking([
      self.WHATSAPP_WEB,
      self.EMAIL,
      self.VIDEOCONFERENCIA,
    ]) and self.TEMPO()

  def VISUALIZAR_PDF(self):
    return self.BROWSER() and self.LINK_PDF()

  def VISUALIZAR_VIDEO(self):
    return self.BROWSER() and self.LINK_VIDEO()

  def VIDEOCONFERENCIA(self):
    return self.BROWSER() and self.LINK_VIDEOCONFERENCIA()

  def WHATSAPP_WEB(self):
    return self.BROWSER() and self.LINK_WHATSAPP_WEB()

  def EMAIL(self):
    return self.BROWSER() and self.LINK_EMAIL()

  ## TERMINALS

  def TEMPO(self):
    return self.consume(TT_TEMPO)

  def VEZES(self):
    return self.consume(TT_VEZES)

  def BROWSER(self):
    return self.consume(TT_BROWSER)

  def LINK_PDF(self):
    return self.consume(TT_LINK_PDF)

  def LINK_VIDEO(self):
    return self.consume(TT_LINK_VIDEO)

  def LINK_VIDEOCONFERENCIA(self):
    return self.consume(TT_LINK_VIDEOCONFERENCIA)

  def LINK_WHATSAPP_WEB(self):
    return self.consume(TT_LINK_WHATSAPP_WEB)

  def LINK_EMAIL(self):
    self.consume(TT_LINK_EMAIL)
