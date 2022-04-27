from turtle import Screen
from snake import Snake #importamos nuestro archivo snake.py 
from food import Food
import time

#Crea el escenario del evento 
screen = Screen() #Instanciamos el objeto 
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("Snake Game")

screen.tracer(0) #quitamos animación de movimiento

#Crear - Instanciar el objeto serpiente 
snake = Snake()

#Instancio objeto comida
food = Food()

#Movimientos serpiente
screen.listen()
screen.onkey(snake.up,"Up") #accion que se va a ejecuta y tipo de tecla que se va a mover
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Establecer estado del juego
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.2)


    snake.move() #Nos traemos la funcion move del archivo snake.py



#Final
screen.exitonclick()