from turtle import Screen, Turtle 
import time

#Crea el escenario del evento 
screen = Screen() #Instanciamos el objeto 
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0) #quitamos animación de movimiento


#Creación del cuerpo de la serpiente 

starting_positions = [(0,0),(-20, 0), (-40, 0)] #Almacenando posiciones

segments = []

#Por cada posicion en position se va a ejecutar el recorrido de positions
for position in starting_positions: 
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.penup()
    snake_segment.goto(position)
    segments.append(snake_segment)
    

#Establecer estado del juego
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)


    '''
    for segment in segments:
        segment.forward(20)
        segment[0].left(90)
    '''



    for seg_num in range(len(segments) - 1, 0, - 1): #Quiero que me almacene todas las nuevas posiciones
        new_x = segments[seg_num - 1].xcor() #cor = coordenada x coordenada y
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y) #movimiento segun las coordenadas que tengo, y aquí debo indicarle donde debe hacer el movimiento, por ende necesita saber la posicion de los cuadritos.

    segments[0].forward(20)
    segments[0].left(90)


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

#Final
screen.exitonclick()