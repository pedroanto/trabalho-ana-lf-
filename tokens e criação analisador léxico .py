import ply.lex as lex

# Definição dos tokens
tokens = (
    'ID',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
)

# Expressões regulares para tokens simples
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Expressão regular para identificar IDs (identificadores)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

# Expressão regular para identificar números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  # Converte o valor para inteiro
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Tratamento de erros para caracteres ilegais
def t_error(t):
    print(f"Caractere ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# Construção do analisador léxico
lexer = lex.lex()

# Testando o analisador léxico
if __name__ == "__main__":
    # Teste de entrada
    data = '(+ 3 (* 4 2))'

    # Passa a entrada para o lexer
    lexer.input(data)

    # Processa a entrada e imprime os tokens reconhecidos
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
