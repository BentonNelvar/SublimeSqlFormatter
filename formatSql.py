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

def p_statement_list(p):
    'statement_list : statement'
    p[0] = p[1]

def p_statement_select(p):
    "statement : SELECT select_list FROM table_reference ';'"
    p[0] = 'SELECT\t\t' + p[2] + '\n\tFROM\t' + p[4] + ';'

def p_select_list(p):
    "select_list : '*'"
    p[0] = p[1] 

def p_table_reference(p):
    'table_reference : TEXT'
    p[0] = p[1]

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
