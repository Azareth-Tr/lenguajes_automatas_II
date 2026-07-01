grammar Expr;

root : expr EOF;

//expr : MAS expr | NUM;
expr : EOF;

PRINT : 'print';
PUNTO_COMA : ';';
CADENA: '"' ~["\r\n]* '"';
WS: [ \t\r\n]+ -> skip;