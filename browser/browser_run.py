from interpreter.lexer import *
from interpreter.parsing import NonTerminalNode, TerminalNode

from browser.acessarChrome import *
from browser.assistirVideo import *
from browser.acessarConferencia import *
from browser.acessarWhatsappWeb import *
from browser.enviarEmail import *


def browser_run(node):
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
    browser_run(child)

def extract_token(node):
  if isinstance(node, TerminalNode):
    return node.token

  return extract_token(node.children[0])


def process_PROGRAMA_SOL(node):
  times = node.children[1].token
  print('PROGRAM_SOL', times)

def process_EXPLORE(node):
  time = extract_token(node.children[1])
  print('EXPLORE', time)
  acessar_chrome(timeToSeconds(time))

def process_PRESENT(node):
  link = extract_token(node.children[0].children[1])
  time = extract_token(node.children[1])
  print('PRESENT', link, time)
  handle_link_token(link, time)

def process_INTERACT(node):
  link = extract_token(node.children[0].children[1])
  time = extract_token(node.children[1])
  print('INTERACT', link, time)
  handle_link_token(link, time)

def process_CRITIQUE(node):
  link = extract_token(node.children[0].children[1])
  time = extract_token(node.children[1])
  print('CRITIQUE', link, time)
  handle_link_token(link, time)


def handle_link_token(link_token, time_token):
  seconds = timeToSeconds(time_token)

  if link_token.type == TT_LINK_PDF:
    abrir_pdf(get_directory_value(link_token), seconds)
    print(get_directory_value(link_token))
  elif link_token.type == TT_LINK_VIDEO:
    acessar_youtube(get_link_value(link_token), seconds)
  elif link_token.type == TT_LINK_VIDEOCONFERENCIA:
    acessar_videoconferencia(link_token.value, seconds)
  elif link_token.type == TT_LINK_WHATSAPP_WEB:
    acessar_whatsapp_web(seconds)
  elif link_token.type == TT_LINK_EMAIL:
    enviar_email(get_link_value(link_token))


def timeToSeconds(token):
  value = token.value

  if value == '15_min':
    return 900
  elif value == '20_min':
    return 1200
  elif value == '1_hora':
    return 3600
  elif value == '2_dias':
    return 172800
  elif value == '10s':
    return 10
  else:
    return -1

def get_link_value(link_token):
  return link_token.value.replace('"', '').split(':')[1]

def get_directory_value(link_token):
  text = link_token.value.replace('"', '')
  separator = text.find(":")
  return text[separator + 1:]
