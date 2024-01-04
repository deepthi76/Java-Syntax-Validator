import ply.yacc as yacc
from lexer import tokens, lexer

def p_main(p):
    '''main : Statements'''

def p_Statements(p):
    '''Statements : var_declaration Statements
                  | assignment Statements
                  | expression Statements
                  | initialization Statements
                  | while_loop Statements
                  | if_else_statement Statements 
                  | switch_statement Statements
                  | '''
    pass                  

def p_var_declaration(p):
    '''var_declaration : TYPE list_var SEMI_COLON'''
    print("Valid declaration.")
    pass
    

def p_list_var(p):
    '''list_var : ID
                | ID COMMA list_var
                | '''
    pass

def p_assignment(p):
    '''assignment : ID EQUAL expression SEMI_COLON
                  | ID EQUAL expression COMMA assignment'''
    print("Valid assignment.")
    pass

def p_initialization(p):
    '''initialization : TYPE ID EQUAL expression SEMI_COLON'''
    print("Valid initialization.")
    pass



def p_condition(p):
    '''condition : ID rel ID
                | ID rel NUMBER
                | NUMBER rel ID
                | NUMBER rel NUMBER
                | expression rel expression
                '''
    print("Valid condition.")
    pass  

def p_rel(p):
    '''rel : GOE 
           | LOE 
           | GREAT 
           | LESS 
           | EQ 
           | NEQ
           '''
    pass

def p_expression(p):
    '''expression : expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term
                  | expression MOD term
                  | term'''
    pass
def p_term(p):
    '''term : term TIMES factor
            | term DIVIDE factor
            | term MOD factor
            | factor'''
    pass

def p_factor(p):
    '''factor : NUMBER
              | ID
              | L_PARENTHESIS expression R_PARENTHESIS'''	
    pass	
def p_if_else(p):
    '''if_else_statement : IF L_PARENTHESIS condition R_PARENTHESIS L_CBRACES Statements R_CBRACES ELSE L_CBRACES Statements R_CBRACES
                         | IF L_PARENTHESIS condition R_PARENTHESIS L_CBRACES Statements R_CBRACES'''
    print("Valid if-else statement.")
    pass
                         

def p_while_loop(p):
    'while_loop : WHILE L_PARENTHESIS condition R_PARENTHESIS L_CBRACES Statements R_CBRACES '
    print("Valid while loop.")
    

def p_switch_statement(p):
    '''switch_statement : SWITCH L_PARENTHESIS expression R_PARENTHESIS L_CBRACES case_statements R_CBRACES'''
    print("Valid switch statement.")
    
def p_case_statements(p):
    '''case_statements : CASE expression COLON Statements BREAK SEMI_COLON case_statements
                       | CASE expression COLON Statements BREAK SEMI_COLON  
                       | CASE expression COLON Statements 
                       | CASE expression COLON Statements case_statements
                       | DEFAULT COLON Statements BREAK SEMI_COLON
                       | DEFAULT COLON Statements'''
    pass

def p_error(p):
    print(f"Syntax error at line {p.lineno}, position {p.lexpos}: Unexpected token '{p.value}'")
    #quit()

parser = yacc.yacc()

