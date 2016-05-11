import re

keywords = {
    'select': 'SELECT',
    'as': 'AS',
    'from': 'FROM'
}

tokens = ['TEXT'] + list( keywords.values() )

literals = [ '.' , ',' , ';' , '*' ]

def t_TEXT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = keywords.get(t.value.lower(),'TEXT')
    return t

# def t_NUMBER(t):
#     r'\d+'
#     try:
#         t.value = int(t.value)
#     except ValueError:
#         print("Integer value too large %d", t.value)
#         t.value = 0
#     return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_eof(t):
    return None

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    

