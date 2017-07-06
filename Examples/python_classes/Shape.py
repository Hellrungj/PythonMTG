import turtle
import random
import sys

class Shape():
    def __init__(self):
        pass
    
class Rec():
    def __init__(self, H=1, L=1):
        self.height = random.randint(1,H) 
        self.lenght = random.randint(1,L)
        self.color = [0,0,0] #RGB value
        self.turtle = turtle.Turtle()
        self.window = turtle.Screen()
        
    def create_rec(self, color = (1,20,255), pos=(0,0)):
        self.turtle.setpos(pos)
        self.turtle.color(color)
        self.draw()
        
    def draw(self):
        for index in range(2):
            self.turtle.forward(self.lenght)
            self.turtle.right(90)
            self.turtle.forward(self.height)
            self.turtle.right(90)
        self.window.exitonclick()
    
        
def main():
    One = Rec(2,3)
    One.create_rec((1,23,255),(2,2))
    
    
main()