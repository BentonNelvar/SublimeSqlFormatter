from ply import *
import FormatSqlLexer
from FormatSqlLexer import tokens

# import FormatSqlLexer
# from FormatSqlLexer import tokens

lexer = lex.lex(module=FormatSqlLexer)

# precedence = (
#     ('left','PLUS','MINUS'),
#     ('left','TIMES','DIVIDE'),
#     ('right','UMINUS'),
#     )

def p_input(p):
    '''input : statement_list'''
    p[0] = p[1]

def p_statement_list_recur(p):
    '''statement_list : statement_list statement'''
    if p[1] != '':
        p[0] = p[1] + '\n\n' + p[2]
    else:
        p[0] = p[2]

def p_statement_list_empty(p):
    '''statement_list : empty'''
    p[0] = p[1]

def p_statement_select(p):
    "statement : SELECT select_list FROM table_reference ';'"
    p[0] = 'SELECT\t\t' + p[2] + '\n\tFROM\t' + p[4] + ';'

def p_select_list(p):
    '''select_list : '*'
                   | select_list_x select_item'''
    p[0] = ''.join(p[1:])

def p_select_list_x_recur(p):
    "select_list_x : select_list_x select_item ','"
    p[0] = p[1] + p[2] + ',\n\t\t\t'

def p_select_list_x_empty(p):
    "select_list_x : empty"
    p[0] = p[1]

def p_select_item(p):
    '''select_item : TEXT
                   | TEXT alias
                   | TEXT '.' TEXT
                   | TEXT '.' '*'
                   | TEXT '.' TEXT alias'''
    p[0] = ''.join(p[1:])

def p_table_reference_name(p):
    '''table_reference : TEXT
                       | TEXT alias'''
    p[0] = ''.join(p[1:])

def p_alias(p):
    '''alias : empty TEXT
             | AS TEXT'''
    p[0] = ' AS ' + p[2]

def p_empty(p):
    'empty : '
    p[0] = ''

def p_error(p):
    if p:
        print( 'On line ' + str(p.lineno) + ': Invalid token ' + p.value )

# def p_select_expr(t):
#     '''select_expr : NAME
#                    | NAME ALIAS
#                    | NAME AS ALIAS'''

# def p_table_reference(t):
#     '''table_reference : NAME
#                        | NAME ALIAS
#                        | NAME AS ALIAS'''


parser = yacc.yacc()

class FormatSql(object):

    def format( self , input ):
        return parser.parse( input )
