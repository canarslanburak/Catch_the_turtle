import turtle
import random
import tkinter

screen=turtle.Screen()
screen.bgcolor("DimGray")
screen.setup(1600,1000)
FONT = ('Arial', 30, 'normal')
score=0
zorluk=750
game_over=False
x_axis=list(range(-600,600,10))
y_axis=list(range(-200,400,10))
score_turtle= turtle.Turtle()
count_down_turtle= turtle.Turtle()

def make_score_turtle():
    score_turtle.penup()
    score_turtle.hideturtle()
    score_turtle.color("light blue")
    y=screen.window_height()/2*0.9
    score_turtle.setposition(0,y)
    score_turtle.write("Score: 0", move=False,align="center", font=FONT)

def make_aim_turtle():
    if  game_over == False:

        t=turtle.Turtle()
        t.shapesize(1.25)
        def handle_click(x,y):
            global score
            score += + 1
            score_turtle.clear()
            score_turtle.write(f"Score: {score}", move=False, align="center", font=FONT)
        t.onclick(handle_click)
        t.showturtle()
        t.penup()
        t.shape("turtle")
        t.color("yellow")
        t.setposition(random.choice(x_axis),random.choice(y_axis))
        screen.ontimer(make_aim_turtle,zorluk)
        screen.ontimer(t.hideturtle,int(zorluk*0.8))


def countdown(time):
    global game_over
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    count_down_turtle.penup()
    count_down_turtle.hideturtle()
    count_down_turtle.setposition(0, y - 50)
    count_down_turtle.clear()

    if time > 0:
        count_down_turtle.clear()
        count_down_turtle.write("Time: {}".format(time), move=False, align="center", font=FONT)
        screen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        count_down_turtle.write("Game Over!", align='center', font=FONT)
def start_game():
    turtle.delay(0)
    countdown(15)
    make_aim_turtle()
    make_score_turtle()
start_game()
turtle.mainloop()
