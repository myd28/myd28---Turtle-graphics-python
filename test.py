import turtle 
tutu= turtle.Turtle()

class turtleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
        target_x= float(ctx.x_cord.text)
        target_y= float(ctx.y_cord.text)
        #target_f= float(ctx.f_rate.text) 
        cur_pos= tutu.pos()
        
        tutu.shape('turtle')
        tutu.color("green")
        #tutu.circle(50) 
        
        print(cur_pos)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawcircle. G02 
    def visitDrawcircleG02(self, ctx:turtleParser.DrawcircleContext):
        target_x= float(ctx.x_cord.text)
        target_y= float(ctx.y_cord.text)
        target_i= float(ctx.i_cord.text) 
        target_j= float (ctx.j_cord.text)
        cur_pos= tutu.pos()
        
        print(cur_pos) 
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        return self.visitChildren(ctx)



del turtleParser
