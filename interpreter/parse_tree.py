#
# Represents a non terminal in a tree, which's a subtree.
#
class NonTerminalNode:
  def __init__(self, name, children):
    self.name = name
    self.children = children

  def __repr__(self):
    strings = []
    pre_order(self, 1, strings)
    return '\n'.join(strings)

#
# Represents a terminal, which's a leaf node.
#
class TerminalNode:
  def __init__(self, token):
    self.token = token


#
# Traverse the tree in pre order filling the strings list.
#
def pre_order(node, depth, strings):
  if isinstance(node, TerminalNode):
    strings.append(f'{"-" * depth} {node.token}')
    return

  strings.append(f'{"-" * depth} {node.name}')

  for child in node.children:
    pre_order(child, depth + 1, strings)
