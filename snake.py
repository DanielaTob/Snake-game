from turtle import Turtle
from venv import create 

#Creación del cuerpo de la serpiente 
STARTING_POSITION = [(0,0),(-20, 0), (-40, 0)] #Almacenando posiciones

#Clase con sus caracteristicas
class Snake:

    def __init__(self): #Funcion constructor SELF:sirve para llamar atributos dentro de la misma clase. 
        self.segments = [] #Atributo
        self.create_snake() #Metodo


    def create_snake(self):
        for position in STARTING_POSITION: #Por cada posicion en position se va a ejecutar el recorrido de positions
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    
    def move(self):
        #Movimiento de la serpiente 
        for seg_num in range(len(self.segments) - 1, 0, - 1): #Quiero que me almacene todas las nuevas posiciones
            new_x = self.segments[seg_num - 1].xcor() #cor = coordenada x coordenada y
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y) #movimiento segun las coordenadas que tengo, y aquí debo indicarle donde debe hacer el movimiento, por ende necesita saber la posicion de los cuadritos.

        self.segments[0].forward(20)
        #segments[0].left(90)


    '''
    snake_segment = Turtle("square") 
    snake_segment.color("white")

    snake_segment2 = Turtle("square")
    snake_segment2.color("white")
    snake_segment2.goto(-20, 0)

    snake_segment3 = Turtle("square")
    snake_segment3.color("white")
    snake_segment3.goto(-40, 0)

    '''

