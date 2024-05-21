from ply import lex

# Lista de tokens
tokens = (
    'ID', 'TIPO', 'NUM_INT', 'NUM_DEC', 'TEXTO',
    'SEMICOLON', 'DOT', 'COMMA', 
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'MODULO', 
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'OROR', 'ANDAND', 'NOT', 'GREATER', 'LESS', 'GREATEREQUAL', 'LESSEQUAL', 'NOTEQUAL', 'EQUAL',
    'PLUSEQUAL', 'MINUSEQUAL', 'TIMESEQUAL', 'DIVEQUAL', 'MODEQUAL', 'ANDANDEQUAL', 'OROREQUAL',
    'COMMENT', 'MULTICOMMENT'
    'DOTDOTDOT', 
)

# Regras para cada token
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_COMMA = r','
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOTDOTDOT = r'\.\.\.'
t_OROR = r'\|\|'
t_ANDAND = r'&&'
t_NOT = r'!'
t_GREATER = r'>'
t_LESS = r'<'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_NOTEQUAL = r'!='
t_EQUAL = r'=='
t_MODULO = r'%'
t_DOT = r'.'
t_PLUSEQUAL = r'\+='
t_MINUSEQUAL = r'-='
t_TIMESEQUAL = r'\*='
t_DIVEQUAL = r'/='
t_MODEQUAL = r'%='
t_ANDANDEQUAL = r'&&='
t_OROREQUAL = r'\|\|='

#regra pros tipos
def t_TIPO(t):
    r'int|float|double|char|boolean|'
    t.value = str(t.value)
    return t

#regra pra numeros do tipo float
def t_NUM_DEC(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
#regra pra numeros do tipo inteiro
def t_NUM_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

#regra pra id
def t_ID(t):
    r'[a-zA-z_][a-zA-Z0-9_]*'
    t.value = str(t.value)
    return t

# Expressao regular para comentarios/texto em linha
def t_COMMENT(t):
    r'//.*'
    return t
# Expressao regular para comentarios/texto multi-linhas
def t_MULTICOMMENT(t):
    r'/\*[\s\S]*?\*/'
    return t

def t_TEXTO(t):
    r'\"[^\"]*\"'
    t.value = t.value[1:-1]  # Remover as aspas da string
    return t

t_ignore = ' \t\n' # ignora caracter em branco

# ERROS
def t_error(t):
    print(f"Caractere indesejado na linha : {t.value[0]}")
    t.lexer.skip(1)

#criando o analisador lexico
lexico = lex.lex()