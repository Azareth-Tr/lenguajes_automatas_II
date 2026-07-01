# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,33,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,
        0,1,0,1,1,1,1,1,2,1,2,5,2,20,8,2,10,2,12,2,23,9,2,1,2,1,2,1,3,4,
        3,28,8,3,11,3,12,3,29,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,2,3,0,10,
        10,13,13,34,34,3,0,9,10,13,13,32,32,34,0,1,1,0,0,0,0,3,1,0,0,0,0,
        5,1,0,0,0,0,7,1,0,0,0,1,9,1,0,0,0,3,15,1,0,0,0,5,17,1,0,0,0,7,27,
        1,0,0,0,9,10,5,112,0,0,10,11,5,114,0,0,11,12,5,105,0,0,12,13,5,110,
        0,0,13,14,5,116,0,0,14,2,1,0,0,0,15,16,5,59,0,0,16,4,1,0,0,0,17,
        21,5,34,0,0,18,20,8,0,0,0,19,18,1,0,0,0,20,23,1,0,0,0,21,19,1,0,
        0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,21,1,0,0,0,24,25,5,34,0,0,25,
        6,1,0,0,0,26,28,7,1,0,0,27,26,1,0,0,0,28,29,1,0,0,0,29,27,1,0,0,
        0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,6,3,0,0,32,8,1,0,0,0,3,0,21,
        29,1,6,0,0
    ]

class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PRINT = 1
    PUNTO_COMA = 2
    CADENA = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'print'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "PRINT", "PUNTO_COMA", "CADENA", "WS" ]

    ruleNames = [ "PRINT", "PUNTO_COMA", "CADENA", "WS" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


