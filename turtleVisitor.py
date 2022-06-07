# Generated from turtle.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .turtleParser import turtleParser
else:
    from turtleParser import turtleParser

# This class defines a complete generic visitor for a parse tree produced by turtleParser.

from turtle import *
from random import randint
import turtle
turty = turtle.Turtle()
turto = turtle.Turtle()


class turtleVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by turtleParser#start.
    def visitStart(self, ctx:turtleParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawlineExpr.
    def visitDrawlineExpr(self, ctx:turtleParser.DrawlineExprContext):
     target_x = int(ctx.x_cord.text)
     target_y = int(ctx.y_cord.text)
     cur_pos = turty.pos()
     bgcolor('black')
     x = 1
     y = 75
     turty.home()
     turty.penup()
     turty.speed(10)
     turty.goto(target_x, target_y)
     turty.pendown()
     if target_y >= cur_pos[0]:
        while x < 250:
          r = randint(0, 255)
          g = randint(0, 255)
          b = randint(0, 255)
         
           
          turty.shape("turtle")
          turty.pendown()
          turty.speed(5000)
          colormode(255)
          turty.pensize(y)
          turty.pencolor(r,g,b)
          turty.forward(40 + x)
          turty.right(90.99)
          x = x+1
          y = y-0.3
     else:
         while x < 300:
          r = randint(0, 255)
          g = randint(0, 255)
          b = randint(0, 255)
          turty.shape("turtle")
          turty.pendown()
          turty.speed(5000)
          colormode(255)
          turty.pensize(y)
          turty.pencolor(r,g,b)
          turty.forward(20 + x)
          turty.right(90.91)
          x = x+1
          y = y-0.3

         turty.penup() 
         turty.home()
         return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#printlineExpr.
    def visitPrintlineExpr(self, ctx:turtleParser.PrintlineExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by turtleParser#drawExpr.
    def visitDrawExpr(self, ctx:turtleParser.DrawExprContext):
     target_x = int(ctx.x_cord.text)
     target_y = int(ctx.y_cord.text)
     cur_pos = turty.pos()
     x = 1
     turto.goto(target_x, target_y)
     if target_x > cur_pos[0]:
       while x < 2:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        turto.shape("turtle")
        turto.penup()
        turto.forward(target_y * 5)
        turto.pendown()
        r = 60
        turto.color(r,g,b)
        turto.begin_fill()
        turto.circle(r)
        turto.end_fill()
        x = x+1
       else:
        while x < 2:
         r = randint(0, 180)
         g = randint(180, 220)
         b = randint(200, 255)
         colormode(255)
         turto.shape("turtle")
         turto.penup()
         turto.forward(target_y * 5)
         turto.pendown()
         turto.color(r,g,b)
         r=90
         turto.begin_fill()
         turto.circle(r)
         turto.end_fill()
         x = x+1
       
    
      
     if target_y < cur_pos[0]:
        while x < 2:
         r = randint(0, 255)
         g = randint(0, 255)
         b = randint(0, 255)
         colormode(255)
         turto.shape("turtle")
         turto.penup()
         turto.forward(target_y * 5)
         turto.pendown()
         r = 60
         turto.color(r,g,b)
         turto.begin_fill()
         turto.circle(r)
         turto.end_fill()
         x = x+1
     else:
       while x < 2:
         r = randint(225, 250)
         g = randint(1, 175)
         b = randint(140, 255)
         colormode(255)
         turto.shape("turtle")
         turto.penup()
         turto.forward(target_y * 5)
         turto.pendown()
         turto.color(r,g,b)
         r=90
         turto.begin_fill()
         turto.circle(r)
         turto.end_fill()
         x = x+1
       

     return self.visitChildren(ctx)



    # Visit a parse tree produced by turtleParser#HomeExpr.
    def visitHomeExpr(self, ctx:turtleParser.HomeExprContext):
     target_x = int(ctx.x_cord.text)
     target_y = int(ctx.y_cord.text)
     cur_pos = turty.pos()
     turto.penup()
     turty.penup()
     turty.setpos(0,0)
     turto.setpos(0,0)
     turto.penup()
     turty.pendown()
     return self.visitChildren(ctx) 

del turtleParser
