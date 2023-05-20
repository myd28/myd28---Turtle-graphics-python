# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete generic visitor for a parse tree produced by turtleParser.
import turtle 
tutu= turtle.Turtle()
#clone= turtle.Turtle()
class turtleVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        target_x= int(ctx.x_cord.text)
        target_y= int(ctx.y_cord.text)
        cur_pos= tutu.pos()

        tutu.shape('turtle')
        tutu.color("blue")
        #tutu.circle(50)
        
       
        
        if target_x > cur_pos[0]:
            tutu.right (target_x - cur_pos[0])
        else:
            tutu.left (cur_pos[0] - target_x) 
       
        if target_y > cur_pos[1]:
            tutu.forward( target_y - cur_pos[1]) 
        else: 
            tutu.backward (cur_pos[1] - target_y) 
       
        print(cur_pos)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawCircleG02.
    def visitDrawCircleG02(self, ctx:turtleParser.DrawCircleG02Context):
        target_x= int(ctx.x_cord.text)
        target_y= int(ctx.y_cord.text)
        target_i= int(ctx.i_cord.text)
        cur_pos= tutu.pos()
        
        tutu.shape('turtle')
        tutu.color("blue")
        
        #clone.shape('triangle')
        #clone.setheading(270)
        
        tutu.circle(target_x, target_y, target_i) 
        #tutu.setheading(270) 
        print(cur_pos)
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawCircleG03.
    def visitDrawCircleG03(self, ctx:turtleParser.DrawCircleG03Context):
        target_x= int(ctx.x_cord.text)
        target_y= int(ctx.y_cord.text)
        target_i= int(ctx.i_cord.text)
        cur_pos= tutu.pos()
        
        tutu.shape('turtle')
        tutu.color("blue")
        
        tutu.setheading(180)
        tutu.circle(target_x, target_y, target_i) 
         
        print(cur_pos)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#positioningG91.
    def visitPositioningG91(self, ctx:turtleParser.PositioningG91Context):
        target_x= int(ctx.x_cord.text)
        target_y= int(ctx.y_cord.text)
        cur_pos= tutu.pos()
        
        tutu.shape('turtle')
        tutu.color("blue")
        
        tutu.penup() 
        tutu.goto(target_x, target_y) 
            
        tutu.pendown()
        
        print (cur_pos) 
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        return self.visitChildren(ctx)



del turtleParser