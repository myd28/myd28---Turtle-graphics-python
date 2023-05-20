# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete listener for a parse tree produced by turtleParser.
class turtleListener(ParseTreeListener):

    # Enter a parse tree produced by turtleParser#start.
    def enterStart(self, ctx:turtleParser.StartContext):
        pass

    # Exit a parse tree produced by turtleParser#start.
    def exitStart(self, ctx:turtleParser.StartContext):
        pass


    # Enter a parse tree produced by turtleParser#drawlineExpr.
    def enterDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        pass

    # Exit a parse tree produced by turtleParser#drawlineExpr.
    def exitDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        pass


    # Enter a parse tree produced by turtleParser#drawCircleG02.
    def enterDrawCircleG02(self, ctx:turtleParser.DrawCircleG02Context):
        pass

    # Exit a parse tree produced by turtleParser#drawCircleG02.
    def exitDrawCircleG02(self, ctx:turtleParser.DrawCircleG02Context):
        pass


    # Enter a parse tree produced by turtleParser#drawCircleG03.
    def enterDrawCircleG03(self, ctx:turtleParser.DrawCircleG03Context):
        pass

    # Exit a parse tree produced by turtleParser#drawCircleG03.
    def exitDrawCircleG03(self, ctx:turtleParser.DrawCircleG03Context):
        pass


    # Enter a parse tree produced by turtleParser#positioningG91.
    def enterPositioningG91(self, ctx:turtleParser.PositioningG91Context):
        pass

    # Exit a parse tree produced by turtleParser#positioningG91.
    def exitPositioningG91(self, ctx:turtleParser.PositioningG91Context):
        pass


    # Enter a parse tree produced by turtleParser#printlineExpr.
    def enterPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        pass

    # Exit a parse tree produced by turtleParser#printlineExpr.
    def exitPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        pass



del turtleParser