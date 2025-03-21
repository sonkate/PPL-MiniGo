// Tran Thanh Son - 2053405
grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
preType = None

def emit(self):
	tk = self.type
	self.preType = tk;
	if tk == self.UNCLOSE_STRING:       
		result = super().emit();
		raise UncloseString(result.text);
	elif tk == self.ILLEGAL_ESCAPE:
		result = super().emit();
		raise IllegalEscape(result.text);
	elif tk == self.ERROR_CHAR:
		result = super().emit();
		raise ErrorToken(result.text); 
	else:
		return super().emit();
}

options{
	language = Python3;
}

program: list_newline? decl+ EOF;

decl:
	(
		var_decl
		| const_decl
		| func_decl
		| method_decl
		| struct_decl
		| interface_decl
	) sm_nl+;
//variables and constant declared
var_decl: VAR ID (all_type | all_type? EQ expr);
const_decl: CONST ID EQ expr;
// functions and method declared (implement)
func_decl:
	FUNC ID LRB parameter_list? RRB all_type? body;
method_decl:
	FUNC LRB ID ID RRB ID LRB parameter_list? RRB all_type? body;
parameter_list: parameter CM parameter_list | parameter;
parameter: list_ID all_type;
list_ID: ID CM list_ID | ID;
// structures and interfaces declared
struct_decl: TYPE struct_type;
interface_decl:
	TYPE ID INTERFACE LCB (NL | interface_method)* RCB;
interface_method: ID LRB parameter_list? RRB all_type? sm_nl;
// expression
expr: expr OR_OP expr1 | expr1;
expr1: expr1 AND_OP expr2 | expr2;
expr2:
	expr2 (EQ_OP | NEQ_OP | LT_OP | LEQ_OP | GT_OP | GEQ_OP) expr3
	| expr3;
expr3: expr3 (ADD_OP | SUB_OP) expr4 | expr4;
expr4: expr4 (MUL_OP | DIV_OP | MOD_OP) expr5 | expr5;
expr5: (NOT_OP | SUB_OP) expr5 | expr6;
expr6: expr6 (LSB expr RSB | DOT_OP (ID | func_call)) | factor;
factor: literal | LRB expr RRB | ID | func_call;
literal:
	INTLIT
	| BINLIT
	| OCTLIT
	| HEXLIT
	| FLOATLIT
	| STRINGLIT
	| boollit
	| NIL
	| arraylit
	| structlit;
// statements
stmt_list: statement stmt_list | statement;
statement:
	(
		var_decl
		| const_decl
		| struct_decl
		| method_decl
		| assign_stmt
		| if_stmt
		| for_stmt
		| break_stmt
		| continue_stmt
		| call_stmt
		| return_stmt
        | body
	) sm_nl+;
// assignment LHS can be array index, dot attribute, ID
assign_stmt: assignment_lhs assign_op expr;
assignment_lhs: assignment_lhs (LSB expr RSB | DOT_OP ID) | ID;
assign_op:
	EQ_ASSIGN_OP
	| ADD_ASSIGN_OP
	| SUB_ASSIGN_OP
	| MUL_ASSIGN_OP
	| DIV_ASSIGN_OP
	| MOD_ASSIGN_OP;

if_stmt:
	IF LRB expr RRB list_newline? body list_elif (
		ELSE list_newline? body
	)?;
list_elif: elif_one list_elif |;
elif_one: ELSE IF LRB expr RRB list_newline? body;

for_stmt: (basic_for | init_for | range_for) list_newline? body;
basic_for: FOR expr;
init_for: FOR (assign_stmt | var_decl) SM expr SM assign_stmt;
range_for: FOR ID CM ID EQ_ASSIGN_OP RANGE expr;

break_stmt: BREAK;
continue_stmt: CONTINUE;
call_stmt: (assignment_lhs DOT_OP |) ID LRB (expr_list |) RRB;
return_stmt: RETURN (expr |);
// array struct interface type
array_type: list_array_index prim_types;

struct_type: ID STRUCT LCB (NL | struct_field_list)* RCB;
struct_field_list:
	struct_field struct_field_list
	| struct_field;
struct_field: ID all_type sm_nl+;
// support
body: LCB stmt_list? RCB;

func_call: ID LRB (expr_list |) RRB;
expr_list: expr expr_tail | expr;
expr_tail: CM expr expr_tail |;

all_type: INT | FLOAT | BOOLEAN | STRING | array_type | ID;
prim_types: INT | FLOAT | BOOLEAN | STRING;

list_array_index: array_index list_array_index | array_index;
array_index: LSB (expr|) RSB;
// Keywords
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
FUNC: 'func';
TYPE: 'type';
STRUCT: 'struct';
INTERFACE: 'interface';
STRING: 'string';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';
CONST: 'const';
VAR: 'var';
CONTINUE: 'continue';
BREAK: 'break';
RANGE: 'range';
NIL: 'nil';
TRUE: 'true';
FALSE: 'false';
//Operators
ADD_OP: '+';
SUB_OP: '-';
MUL_OP: '*';
DIV_OP: '/';
MOD_OP: '%';
EQ_OP: '==';
NEQ_OP: '!=';
LT_OP: '<';
LEQ_OP: '<=';
GT_OP: '>';
GEQ_OP: '>=';
AND_OP: '&&';
OR_OP: '||';
NOT_OP: '!';
EQ_ASSIGN_OP: ':=';
ADD_ASSIGN_OP: '+=';
SUB_ASSIGN_OP: '-=';
MUL_ASSIGN_OP: '*=';
DIV_ASSIGN_OP: '/=';
MOD_ASSIGN_OP: '%=';
EQ: '=';
DOT_OP: '.';

//Seperators
LSB: '[';
RSB: ']';
LRB: '(';
RRB: ')';
LCB: '{';
RCB: '}';
CM: ',';
COL: ':';
QUOTES: '"';
SM: ';';
// SM or NL
sm_nl: SM | NL;
// comments
LINE_CMT: ('//' .*? (NL | EOF)) -> skip;
COMMENT: '/*' (COMMENT | .)*? '*/' -> skip;
//fragments
fragment DIGIT: [0-9];
fragment EXPONENT: [eE] [+-]? DIGIT+;
fragment CHAR: '\\' [\\ntr"] | '\'"' | ~["\\\n];
// literal
BINLIT: '0' [bB][0-1]+;
OCTLIT: '0' [oO][0-7]+;
HEXLIT: '0' [xX][a-fA-F0-9]+;
INTLIT: '0' | [1-9][0-9]*;
FLOATLIT: DIGIT+ ('.' DIGIT*) EXPONENT? | DIGIT+ EXPONENT;
STRINGLIT: QUOTES CHAR* QUOTES {self.text = self.text[1:-1]};
boollit: TRUE | FALSE;
NILLIT: NIL;

// arraylit
itemlist: item CM itemlist | item;
item: array_item | expr;
array_item:
	INTLIT
	| BINLIT
	| OCTLIT
	| HEXLIT
	| FLOATLIT
	| STRINGLIT
	| boollit
	| NIL
	| structlit;
arraylit: list_array_index all_type LCB list_array_element RCB;
list_array_element:
	array_element CM list_array_element
	| array_element;
array_element: itemlist | LCB array_element RCB;
// structlit
structlit: ID LCB list_struct_element? LCB;
list_struct_element:
	list_element CM list_struct_element
	| list_element;
list_element: ID COL expr;
// identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;
// Skipping
NL: '\n'{
    if self.preType in [self.ID, self.INTLIT, self.BINLIT, self.OCTLIT, self.HEXLIT, self.STRINGLIT, self.FLOATLIT,
                        self.TRUE, self.FALSE, self.INT, self.FLOAT, self.STRING, self.BOOLEAN, self.NIL,
                        self.RETURN, self.CONTINUE, self.BREAK,
                        self.RRB, self.RCB, self.RSB]:
        self.text = ";"
        self.type = self.SM
    else:
        self.skip()
};
list_newline: NL+;
WS: [ \t\r]+ -> skip; // skip spaces, tabs
// Errors
UNCLOSE_STRING:
	QUOTES CHAR* ('\n' | EOF) {
        if(self.text[-1]=='\n'):
            raise UncloseString(self.text[:-1])
        raise UncloseString(self.text)
    };
ILLEGAL_ESCAPE:
	QUOTES CHAR* ('\\' ~[rnt"\\]) {raise IllegalEscape(self.text)
    };
ERROR_CHAR: . {raise ErrorToken(self.text)};