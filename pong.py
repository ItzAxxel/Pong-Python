import turtle

#Ventana
wn = turtle.Screen()
wn.title("Pong Axel")
wn.bgcolor("Black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#JugadorA
jugadorA = turtle.Turtle()
jugadorA.speed(0)
jugadorA.shape("square")
jugadorA.color("pink")
jugadorA.penup()
jugadorA.goto(-350,0)
jugadorA.shapesize(stretch_wid=5, stretch_len=  1)

#JugadorB 
jugadorB = turtle.Turtle()
jugadorB.speed(0)
jugadorB.shape("square")
jugadorB.color("pink")
jugadorB.penup()
jugadorB.goto(350,0)
jugadorB.shapesize(stretch_wid=5, stretch_len=  1)

#Pelota 
pelota = turtle.Turtle()
pelota.speed(-1)
pelota.shape("circle")
pelota.color("white")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 3
pelota.dy = 3


#Linea Division
division = turtle.Turtle()
division.color("white")
division.goto(0,400)
division.goto(0,-400)

#Funciones
def jugadorA_up():
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)


def jugadorA_down():
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)


def jugadorB_up():
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)


def jugadorB_down():
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)


#Teclado
wn.listen()
wn.onkeypress(jugadorA_up, "w")
wn.onkeypress(jugadorA_down, "s")
wn.onkeypress(jugadorB_up, "Up")
wn.onkeypress(jugadorB_down, "Down")


while True:
    wn.update()

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

#Bordes
    if pelota.ycor() > 290:
        pelota.dy *= -1
    if pelota.ycor() < -290:
        pelota.dy *= -1

#Bordes derecha/izquierda
    if pelota.xcor() > 390:
        pelota.goto(0,0)
        pelota.dx *= -1
    if pelota.xcor() < -390:
        pelota.goto(0,0)
        pelota.dx *= -1

    if (pelota.xcor() > 340 and pelota.xcor() < 350)