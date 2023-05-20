# Generated from turtle.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("\36\4\2\t\2\4\3\t\3\3\2\3\2\5\2\t\n\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\34\n\3\3\3\2\2\4\2\4\2\2\2 \2\b\3\2\2\2\4\33\3\2\2")
        buf.write("\2\6\t\5\4\3\2\7\t\3\2\2\2\b\6\3\2\2\2\b\7\3\2\2\2\t\3")
        buf.write("\3\2\2\2\n\13\7\3\2\2\13\f\7\b\2\2\f\34\7\b\2\2\r\16\7")
        buf.write("\4\2\2\16\17\7\b\2\2\17\20\7\b\2\2\20\34\7\b\2\2\21\22")
        buf.write("\7\5\2\2\22\23\7\b\2\2\23\24\7\b\2\2\24\34\7\b\2\2\25")
        buf.write("\26\7\6\2\2\26\27\7\b\2\2\27\34\7\b\2\2\30\31\7\7\2\2")
        buf.write("\31\32\7\b\2\2\32\34\7\b\2\2\33\n\3\2\2\2\33\r\3\2\2\2")
        buf.write("\33\21\3\2\2\2\33\25\3\2\2\2\33\30\3\2\2\2\34\5\3\2\2")
        buf.write("\2\4\b\33")
        return buf.getvalue()


class turtleParser ( Parser ):

    grammarFileName = "turtle.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'G01'", "'G02'", "'G03'", "'G91'", "'print'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_start = 0
    RULE_expr = 1

    ruleNames =  [ "start", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NUMBER=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(turtleParser.ExprContext,0)


        def getRuleIndex(self):
            return turtleParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = turtleParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        try:
            self.state = 6
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [turtleParser.T__0, turtleParser.T__1, turtleParser.T__2, turtleParser.T__3, turtleParser.T__4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 4
                self.expr()
                pass
            elif token in [turtleParser.EOF]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return turtleParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PositioningG91Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(turtleParser.NUMBER)
            else:
                return self.getToken(turtleParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPositioningG91" ):
                listener.enterPositioningG91(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPositioningG91" ):
                listener.exitPositioningG91(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositioningG91" ):
                return visitor.visitPositioningG91(self)
            else:
                return visitor.visitChildren(self)


    class DrawCircleG02Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.i_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(turtleParser.NUMBER)
            else:
                return self.getToken(turtleParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawCircleG02" ):
                listener.enterDrawCircleG02(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawCircleG02" ):
                listener.exitDrawCircleG02(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawCircleG02" ):
                return visitor.visitDrawCircleG02(self)
            else:
                return visitor.visitChildren(self)


    class DrawCircleG03Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.i_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(turtleParser.NUMBER)
            else:
                return self.getToken(turtleParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawCircleG03" ):
                listener.enterDrawCircleG03(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawCircleG03" ):
                listener.exitDrawCircleG03(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawCircleG03" ):
                return visitor.visitDrawCircleG03(self)
            else:
                return visitor.visitChildren(self)


    class PrintlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(turtleParser.NUMBER)
            else:
                return self.getToken(turtleParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintlineExpr" ):
                listener.enterPrintlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintlineExpr" ):
                listener.exitPrintlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintlineExpr" ):
                return visitor.visitPrintlineExpr(self)
            else:
                return visitor.visitChildren(self)


    class DrawlineExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a turtleParser.ExprContext
            super().__init__(parser)
            self.x_cord = None # Token
            self.y_cord = None # Token
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(turtleParser.NUMBER)
            else:
                return self.getToken(turtleParser.NUMBER, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDrawlineExpr" ):
                listener.enterDrawlineExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDrawlineExpr" ):
                listener.exitDrawlineExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDrawlineExpr" ):
                return visitor.visitDrawlineExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = turtleParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [turtleParser.T__0]:
                localctx = turtleParser.DrawlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.match(turtleParser.T__0)
                self.state = 9
                localctx.x_cord = self.match(turtleParser.NUMBER)
                self.state = 10
                localctx.y_cord = self.match(turtleParser.NUMBER)
                pass
            elif token in [turtleParser.T__1]:
                localctx = turtleParser.DrawCircleG02Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.match(turtleParser.T__1)
                self.state = 12
                localctx.x_cord = self.match(turtleParser.NUMBER)
                self.state = 13
                localctx.y_cord = self.match(turtleParser.NUMBER)
                self.state = 14
                localctx.i_cord = self.match(turtleParser.NUMBER)
                pass
            elif token in [turtleParser.T__2]:
                localctx = turtleParser.DrawCircleG03Context(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 15
                self.match(turtleParser.T__2)
                self.state = 16
                localctx.x_cord = self.match(turtleParser.NUMBER)
                self.state = 17
                localctx.y_cord = self.match(turtleParser.NUMBER)
                self.state = 18
                localctx.i_cord = self.match(turtleParser.NUMBER)
                pass
            elif token in [turtleParser.T__3]:
                localctx = turtleParser.PositioningG91Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 19
                self.match(turtleParser.T__3)
                self.state = 20
                localctx.x_cord = self.match(turtleParser.NUMBER)
                self.state = 21
                localctx.y_cord = self.match(turtleParser.NUMBER)
                pass
            elif token in [turtleParser.T__4]:
                localctx = turtleParser.PrintlineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 22
                self.match(turtleParser.T__4)
                self.state = 23
                localctx.x_cord = self.match(turtleParser.NUMBER)
                self.state = 24
                localctx.y_cord = self.match(turtleParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





