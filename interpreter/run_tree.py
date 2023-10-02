from parsing import NonTerminalNode, TerminalNode


def run_tree(node):
  if isinstance(node, TerminalNode):
    return

  name = node.name

  if name == 'PROGRAMA_SOL':
    process_PROGRAMA_SOL(node)
  elif name == 'EXPLORE':
    process_EXPLORE(node)
  elif name == 'PRESENT':
    process_PRESENT(node)
  elif name == 'INTERACT':
    process_INTERACT(node)
  elif name == 'CRITIQUE':
    process_CRITIQUE(node)

  for child in node.children:
    run_tree(child)


def process_PROGRAMA_SOL(node):
  times = node.children[1].token
  print('PROGRAM_SOL', times)

def process_EXPLORE(node):
  time = extract_token(node.children[1])
  print('EXPLORE', time)

def process_PRESENT(node):
  link = extract_token(node.children[0].children[1])
  time = extract_token(node.children[1])
  print('PRESENT', link, time)

def process_INTERACT(node):
  link = extract_token(node.children[0].children[1])
  time = extract_token(node.children[1])
  print('INTERACT', link, time)

def process_CRITIQUE(node):
  link = extract_token(node.children[0].children[1])
  time = extract_token(node.children[1])
  print('CRITIQUE', link, time)


def extract_token(node):
  if isinstance(node, TerminalNode):
    return node.token

  return extract_token(node.children[0])
