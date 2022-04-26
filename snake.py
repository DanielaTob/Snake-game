from turtle import Screen, Turtle 

#Crea el escenario del evento 
screen = Screen() #Instanciamos el objeto 
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")



#Creación del cuerpo de la serpiente 

positions = [(0,0),(-20, 0), (-40, 0)]

#Por cada posicion en position se va a ejecutar el recorrido de positions
for position in positions: 
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.goto(position)


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