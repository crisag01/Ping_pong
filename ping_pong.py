## Librerias
import turtle
import tkinter as tk
from tkinter import simpledialog


## Ventana de jugadores
wn1 = tk.Tk()
wn1.geometry("410x160")
font1 = ('Times', 30, 'normal')
wn1.title("Bienvenid@, esperamos te diviertas")
jugador1 =  simpledialog.askstring("Input", "Nombre Jugador 1", parent=wn1)
jugador2 =  simpledialog.askstring("Input", "Nombre Jugador 2", parent=wn1)
l1 = tk.Label(wn1,font=font1, text="Bienvenid@ " + jugador1)
l2 = tk.Label(wn1,font=font1, text="Bienvenid@ " + jugador2)
l1.grid(row=0, column=0, padx=10, pady=20)
l2.grid(row=1, column=0, padx=10, pady=20)
print(wn1)


## Ventana de juego
wn = turtle.Screen()
wn.title("Pong by @Crisag")
wn.bgcolor("white")
wn.setup(width=800, height=600)
wn.tracer(0)


## Puntaje
score_1 = 0
score_2 = 0


## Paleta A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.shapesize(stretch_wid=9, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

## Paleta B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.shapesize(stretch_wid=9, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

## Pelota
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0 , 0)
ball.dx = 5
ball.dy = -5


## Texto de Puntaje
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("{}:{} {}:{}".format(jugador1, score_1,jugador2, score_2), align="center", font=("Courier", 24, "normal"))

## Texto UNAM
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("black")
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)
pen2.write("UNAM", align="center", font=("Courier", 80, "normal"))


## Funciones de las paletas (Arriba y Abajo)
def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)
    
def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)
    
## Enlace con el teclado
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.listen()
wn.onkeypress(paddle_a_down, "s")
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.listen()
wn.onkeypress(paddle_b_down, "Down")

## Main game loop
while True:
    wn.update()
    
    ## Movimiento de la pelota
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    ## Resticciones en los bordes
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("{}:{} {}:{}".format(jugador1, score_1, jugador2, score_2), align="center", font=("Courier", 24, "normal"))
        
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("{}:{} {}:{}".format(jugador1, score_1, jugador2, score_2), align="center", font=("Courier", 24, "normal"))
        
    ## Choque de la pelota con las paletas
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 90 and ball.ycor() > paddle_b.ycor() -90):
        ball.setx(340)
        ball.dx *= -1
        
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 90 and ball.ycor() > paddle_a.ycor() -90):
        ball.setx(-340)
        ball.dx *= -1
    