grammar Expr;

root : expr EOF;

//expr : MAS expr | NUM;
expr : EOF;

NUM: [0-9]+;
MAS: '-';
WS: [ \t\r\n]+ -> skip;