from tkinter import *
from tkinter import ttk
root = Tk()

import turtle
tao = turtle.Pen()	
#Logo programing language //Search Google
tao.shape('turtle')
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.forward(100)
tao.left(90)
tao.clear
tao.clear()
for i in range(4):#คำสั่งไหนที่มีโคลอนพิมพ์ต่อลงมาได้เลย
    tao.forward(100)
    tao.left(90)

tao.penup()
tao.goto(200,200)
tao.pendown()
for i in range(4):
    tao.forward(100)
    tao.forword(90)
  
tao.penup()
tao.goto(-200,-200)
tao.forword(100)
tao.pendown()
tao.forward(100)
tao.left(135)
tao.forward(100)
tao.clear()



root.mainloop()