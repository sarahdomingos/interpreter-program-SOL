from interpreter.lexer import Lexer
from interpreter.parsing import Parser
from interpreter.run_tree import run_tree
import PySimpleGUI as sg
from interpreter.lexerInterfaceInput import LexerInterface

sg.theme('DarkAmber')

layout = [
    [sg.Text("Digite um exemplo para executar:")],
    [sg.InputText(key="program_input")],
    [sg.Button("Executar")]
]

window = sg.Window("Programa_SOL Interpreter", layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == "Executar":
        program_input = values["program_input"]

        if program_input:
            try:
                lexer = LexerInterface(program_input)
                tokens = lexer.build()
                
                if not tokens:
                    break

                parser = Parser(tokens)
                parse_tree = parser.build()

                run_tree(parse_tree)
            except Exception as e:
                sg.popup_error(f"Erro: {e}")

window.close()
