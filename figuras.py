# Dibuja aleatoriamente polígonos con efecto caleidoscópico.

import turtle
from random import *


# Configuramos la pizarra para la tortuga.

t = turtle
clon = t.clone()
clon.penup()
clon.hideturtle()
clon.speed(0)
t.setup(500, 500)
t.colormode(1)
t.pencolor(0, 0, 0)
t.pensize(2)
t.speed(9)

def rectangulo(px, py, ancho, alto):
    
    for c in range(1, 5):  # c = cuadrante cartesiano (1-4).
    
        # Nos posicionamos en la esquina y con la orientación correspondiente
        # para el rectángulo que vamos a dibujar sin dejar rastro.
        
        t.penup()  # Levantamos el boli.
        x = (-1 if c == 2 or c == 3 else 1) * (px + ancho / 2)
        y = (-1 if c == 3 or c == 4 else 1) * (py + alto / 2)
        t.seth(t.towards(x, y))
        t.forward(t.distance(x, y))
        t.seth(180 if c == 1 or c == 4 else 0)
        t.pendown()  # Bajamos el boli.
        
        # Dibujamos el rectángulo
        
        t.begin_fill()
        t.forward(ancho)
        if c == 1 or c == 3:
            t.left(90)
            t.forward(alto)
            t.left(90)
            t.forward(ancho)
            t.left(90)
        else:
            t.right(90)
            t.forward(alto)
            t.right(90)
            t.forward(ancho)
            t.right(90)
        t.forward(alto)
        t.end_fill()
    

def poligono_regular(px, py, radio, lados):
    
    vertices = []  # Aquí guardaremos los vértices del polígono.
    t.penup()

    for i in range(lados):  # Buscamos y guardamos los vertices.
        clon.goto(px, py)  # Usamos un clon invisible de la tortuga
        clon.seth(360 / lados * (i + 1))  # para que no se vea el movimiento
        clon.forward(radio)  # mientras va buscando los vértices.
        vertices.append(clon.pos())
        
    for c in range(1, 5):  # Dibujamos los poligonos.
        x = (1 if c == 1 or c == 4 else -1) * (px + radio)
        y = (1 if c == 1 or c == 2 else -1) * py
        t.seth(t.towards(x, y))
        t.forward(t.distance(x, y))
        t.pendown()
        t.begin_fill()
        for vertice in vertices:
            x = (1 if c == 1 or c == 4 else -1) * vertice[0]
            y = (1 if c == 1 or c == 2 else -1) * vertice[1]
            t.seth(t.towards(x, y))
            t.forward(t.distance(x, y))
        t.end_fill()
        t.penup()


# Loop principal

while True:
    
    t.fillcolor(random(), random(), random())
    if choice((True, False)):
        rectangulo(
            randint(0, 250), randint(0, 250),
            randint(25, 125), randint(25, 125)
        )
    else:
        poligono_regular(
            randint(0, 250), randint(0, 250),
            randint(13, 63), randint(3, 10)
        )
        
t.done()