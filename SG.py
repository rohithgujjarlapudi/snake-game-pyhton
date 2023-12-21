"snake game using tkinter "
from tkinter import * import random
WIDTH = 500
HEIGHT = 500
SPEED = 200
SPACE_SIZE = 20 BODY_SIZE = 2
SNAKE = "#00FF00"
FOOD = "#FFFFFF" BACKGROUND = "#000000"
class Snake:
CODE IMPLEMENTATION
 def __init__(self):
self.body_size = BODY_SIZE
self.coordinates = [] self.squares = []
for i in range(0, BODY_SIZE): self.coordinates.append([0, 0])
for x, y in self.coordinates:
square = canvas.create_rectangle(
x, y, x + SPACE_SIZE, y + SPACE_SIZE,
 class Food:
fill=SNAKE, tag="snake") self.squares.append(square)
def __init__(self):
x = random.randint(0,
(WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
y = random.randint(0,
(HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE
self.coordinates = [x, y]
canvas.create_oval(x, y, x + SPACE_SIZE, y +
SPACE_SIZE, fill=FOOD, tag="food")
def next_turn(snake, food):
x, y = snake.coordinates[0]
if direction == "up":
y -= SPACE_SIZE
elif direction == "down":
y += SPACE_SIZE
elif direction == "left":
x -= SPACE_SIZE
elif direction == "right":
x += SPACE_SIZE
snake.coordinates.insert(0, (x, y))

 square = canvas.create_rectangle( x, y, x + SPACE_SIZE,
y + SPACE_SIZE, fill=SNAKE)
snake.squares.insert(0, square)
if x == food.coordinates[0] and y == food.coordinates[1]:
global score
score += 1
label.config(text="Points:{}".format(score))
canvas.delete("food")
food = Food()
else:
del snake.coordinates[-1]
canvas.delete(snake.squares[-1])
del snake.squares[-1]
if check_collisions(snake): game_over()
else:

 window.after(SPEED, next_turn, snake, food)
def change_direction(new_direction):
global direction
if new_direction == 'left':
if direction != 'right':
direction = new_direction elif new_direction == 'right':
if direction != 'left':
direction = new_direction
elif new_direction == 'up':
if direction != 'down':
direction = new_direction elif new_direction == 'down':
if direction != 'up':
direction = new_direction
def check_collisions(snake):
x, y = snake.coordinates[0]
if x < 0 or x >= WIDTH: return True
elif y < 0 or y >= HEIGHT: return True
for body_part in snake.coordinates[1:]:
if x == body_part[0] and y == body_part[1]:
return True

 return False
def game_over():
canvas.delete(ALL) canvas.create_text(canvas.winfo_width()/2,
window = Tk() window.title("Snake Game")
score = 0 direction = 'down'
label = Label(window, text="Points:{}".format(score), font=('consolas', 20))
label.pack()
canvas = Canvas(window, bg=BACKGROUND, height=HEIGHT, width=WIDTH)
canvas.pack()
window.update()
canvas.winfo_height()/2, font=('consolas', 70), text="GAME OVER", fill="red", tag="gameover")

window_width = window.winfo_width() window_height = window.winfo_height() screen_width = window.winfo_screenwidth() screen_height = window.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
window.bind('<Left>',
window.bind('<Right>',
window.bind('<Up>',
window.bind('<Down>',
snake = Snake() food = Food()
next_turn(snake, food)
window.mainloop()
lambda event: change_direction('left'))
lambda event: change_direction('right'))
lambda event: change_direction('up'))
lambda event: change_direction('down'))
