from interpreter.lexer import *


class NonTerminalNode:
  def __init__(self, name, children):
    self.name = name
    self.children = children


class TerminalNode:
  def __init__(self, token):
    self.token = token


def pre_order(node):
  if isinstance(node, TerminalNode):
    print(node.token)
    return

  # print(node.name)
  for child in node.children:
    pre_order(child)


#
# Syntax analyzer: a recursive top-down implementation.
#
# Note: Problems like ambiguity and left recursion were solved in grammar. See: grammar.txt
#
class Parser:
  def __init__(self, tokens):
    self.tokens = tokens

  def build(self):
    parse_tree = self.PROGRAMA_SOL()
    if not parse_tree:
      raise Exception('cannot build parse tree, invalid syntax!')

    return parse_tree

  # returns True if we can consume the given type in the list of tokens, False otherwise
  def consume(self, type):
    if len(self.tokens) == 0:
      if type == TT_EPSILON:
        return TerminalNode(Token(TT_EPSILON, ''))
      else:
        return None

    if self.tokens[0].type == type:
      return TerminalNode(self.tokens.pop(0))

    return None

  # make a backtracking to the current state if some derivation function fails
  def backtracking(self, functions):
    current_state = self.tokens.copy()

    while functions:
      child = functions.pop(0)()

      if child:
        return child
      else:
        self.tokens = current_state.copy()

    return None

  ## NON-TERMINALS

  def PROGRAMA_SOL(self):
    child_1 = self.consume(TT_LOOP)
    if not child_1:
      return None

    child_2 = self.VEZES()
    if not child_2:
      return None

    child_3 = self.SEQUENCIA()
    if not child_3:
      return None

    return NonTerminalNode('PROGRAMA_SOL', [child_1, child_2, child_3])

  def SEQUENCIA(self):
    child_1 = self.FASES_EPIC()
    if not child_1:
      return None

    child_2 = self.SEQUENCIA_1()
    if not child_2:
      return None

    return NonTerminalNode('SEQUENCIA', [child_1, child_2])

  def FASES_EPIC(self):
    child = self.backtracking([self.EXPLORE, self.PRESENT, self.INTERACT, self.CRITIQUE])
    if not child:
      return None

    return NonTerminalNode('FASES_EPIC', [child])

  def SEQUENCIA_1(self):
    child_1 = self.consume(TT_EPSILON)
    if child_1:
      return NonTerminalNode('SEQUENCIA_1', [child_1])

    child_2 = self.SEQUENCIA()
    if child_2:
      return NonTerminalNode('SEQUENCIA_1', [child_2])

    return None

  def EXPLORE(self):
    child_1 = self.BROWSER()
    if not child_1:
      return None

    child_2 = self.TEMPO()
    if not child_2:
      return None

    return NonTerminalNode('EXPLORE', [child_1, child_2])

  def PRESENT(self):
    child_1 = self.backtracking([self.VISUALIZAR_PDF, self.VISUALIZAR_VIDEO, self.VIDEOCONFERENCIA])
    if not child_1:
      return None

    child_2 = self.TEMPO()
    if not child_2:
      return None

    return NonTerminalNode('PRESENT', [child_1, child_2])

  def INTERACT(self):
    child_1 = self.backtracking([self.WHATSAPP_WEB, self.EMAIL, self.VIDEOCONFERENCIA])
    if not child_1:
      return None

    child_2 = self.TEMPO()
    if not child_2:
      return None

    return NonTerminalNode('INTERACT', [child_1, child_2])

  def CRITIQUE(self):
    child_1 = self.backtracking([self.WHATSAPP_WEB, self.EMAIL, self.VIDEOCONFERENCIA])
    if not child_1:
      return None

    child_2 = self.TEMPO()
    if not child_2:
      return None

    return NonTerminalNode('CRITIQUE', [child_1, child_2])

  def VISUALIZAR_PDF(self):
    child_1 = self.BROWSER()
    if not child_1:
      return None

    child_2 = self.LINK_PDF()
    if not child_2:
      return None

    return NonTerminalNode('VISUALIZAR_PDF', [child_1, child_2])

  def VISUALIZAR_VIDEO(self):
    child_1 = self.BROWSER()
    if not child_1:
      return None

    child_2 = self.LINK_VIDEO()
    if not child_2:
      return None

    return NonTerminalNode('VISUALIZAR_VIDEO', [child_1, child_2])

  def VIDEOCONFERENCIA(self):
    child_1 = self.BROWSER()
    if not child_1:
      return None

    child_2 = self.LINK_VIDEOCONFERENCIA()
    if not child_2:
      return None

    return NonTerminalNode('VIDEOCONFERENCIA', [child_1, child_2])

  def WHATSAPP_WEB(self):
    child_1 = self.BROWSER()
    if not child_1:
      return None

    child_2 = self.LINK_WHATSAPP_WEB()
    if not child_2:
      return None

    return NonTerminalNode('WHATSAPP_WEB', [child_1, child_2])

  def EMAIL(self):
    child_1 = self.BROWSER()
    if not child_1:
      return None

    child_2 = self.LINK_EMAIL()
    if not child_2:
      return None

    return NonTerminalNode('EMAIL', [child_1, child_2])

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
    return self.consume(TT_LINK_EMAIL)
