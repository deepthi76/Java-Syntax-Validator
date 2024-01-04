import ply.lex as lex

tokens = (
    'ID', 'NUMBER', 'SEMI_COLON', 'COMMA', 
    'L_CBRACES', 'R_CBRACES','L_PARENTHESIS', 'R_PARENTHESIS', 
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MOD',
    'GOE', 'LOE', 'GREAT', 'LESS', 'EQ', 'NEQ','TYPE', 'EQUAL',
    'WHILE', 'IF','ELSE','SWITCH','CASE','DEFAULT','BREAK','COLON',
)

precedence = (
    ('left', 'GOE', 'LOE', 'GREAT', 'LESS', 'EQ', 'NEQ'),
)

t_SEMI_COLON = r'\;'
t_COMMA = r'\,'
t_L_CBRACES = r'\{'
t_R_CBRACES = r'\}'
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MOD = r'%'
t_GOE = r'\>\='
t_LOE = r'\<\='
t_GREAT = r'\>'
t_LESS = r'\<'
t_EQ = r'\=\='
t_NEQ = r'\!\='
t_EQUAL = r'\='
t_COLON = r':'

# Keywords
t_WHILE = r'while'
t_IF = r'if'
t_ELSE = r'else'
t_SWITCH= r'switch'
t_CASE =r'case'
t_DEFAULT= r'default'
t_BREAK =r'break'



# Reserved words
reserved = {
    'if':'IF',
    'else':'ELSE',
    'while':'WHILE',
    'switch':'SWITCH',
    'case':'CASE',
    'break':'BREAK',
    'default':'DEFAULT',
    'int': 'TYPE',
    'float': 'TYPE',
    'char': 'TYPE',
    'double':'TYPE',
    'long'  : 'TYPE',
    'short' : 'TYPE',
    'bool'  : 'TYPE',
}

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Ignored characters
t_ignore = ' \t\n'
t_ignore_NEWLINE = r'\n'


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

