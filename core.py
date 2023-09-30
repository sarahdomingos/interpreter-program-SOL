#######################################
# CONSTANTS
#######################################

#DIGITS = '0123456789'

#######################################
# ERRORS
#######################################

class Error: # Classe geral de erro
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self): # Função que retorna as informações do erro como uma string
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        return result

class IllegalCharError(Error): 
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

#######################################
# POSITION
#######################################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_command):
        self.idx += 1
        self.col += 1

        if current_command == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#######################################
# TOKENS -> TT significa token type (tipo de token)
#######################################

TT_LOOP		= 'loop'
TT_SEQUENCIA     = 'sequencia'
TT_PRESENT    = 'present'
TT_TEMPO      = 'tempo'
TT_FASES_EPIC      = 'fases_epic'
TT_EXPLORE   = 'explore'
TT_INTERACT   = 'interact'
TT_CRITIQUE = "critique"
TT_NAVEGAR = "navegar"
TT_VER_PDF = "ver_pdf"
TT_VER_VIDEO = "ver_video"
TT_MEETING = "meeting"
TT_WP_WEB = "wp_web"
TT_EMAIL = "email"
TT_NUM_VEZES = "12345"
TT_NUM_TEMPO = ["15min", "20min", "1h", "1d", "2d", "infinito"]
TT_BROWSER = "browser"
TT_LINK_PDF = "link_pdf"
TT_LINK_VIDEO = "link_video"
TT_LINK_MEETING = "link_meeting"
TT_LINK_WP_WEB = "link_wp_web"
TT_LINK_EMAIL = "link_email"

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text # Linha a ser processada
        self.pos = Position(-1, 0, -1, fn, text) # Posição atual na linha
        self.current_command = None # Caractere atual
        self.advance()
    
    def advance(self): # Função que avança para o próximo caractere
        self.pos.advance(self.current_command)
        self.current_command = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens = []

        # Itera sobre os caracteres da linha de código
        while self.current_command != None:
            # Ignora caracteres como espaço e \tab
            if self.current_command in ' \t':
                self.advance()
            elif self.current_command in TT_NUM_VEZES:
                tokens.append(self.make_number())
            elif self.current_command == 'loop': #PAREI POR AQUI, NAO SEI SE TEMOS QUE USAR TODOS OS COMANDOS DA ARVORE OU SE PODE USAR SÓ O NECESSÁRIO
                tokens.append(Token(TT_LOOP))
                self.advance()
            elif self.current_command == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_command == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_command == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_command == '(':
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_command == ')':
                tokens.append(Token(TT_RPAREN))
                self.advance()
            else:
                # Se não encontramos o caractere que estávamos esperando (algum dos possíveis)
                pos_start = self.pos.copy()
                char = self.current_command
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'") # Retorna uma lista vazia, porque vamos retornar nenhum token, e o erro. 

        return tokens, None

    def make_number(self): # Função que "constrói" o número
        num_str = ''
        dot_count = 0

        # Checa se o caractere está na lista de dígitos possíveis, e se possui ponto para fazer a diferenciação entre inteiro e float
        while self.current_command != None and self.current_command in DIGITS + '.':
            if self.current_command == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_command
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

#######################################
# RUN
#######################################

def run(fn, text):
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()

    return tokens, error