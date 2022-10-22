import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 400

monkey = Actor('monkeymain.png')
monkey.pos = 100, 100
banana = Actor('banana main.png')
banana.pos = 500, 300
score = 0
game_over = False

def draw():
    screen.blit('jungle.jpg', (0, 0))
    monkey.draw()
    banana.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10),fontsize = 30)
    if game_over:
        screen.blit('jungle.jpg', (0, 0))
        screen.draw.text("FINAL SCORE: " + str(score), color="black", topleft=(180,200),fontsize = 50)

def place_banana():
    banana.x = randint(20, (WIDTH - 20))
    banana.y = randint(20, (HEIGHT - 20))

def update():
    global score
    if keyboard.right:
        monkey.x += 5
    elif keyboard.left:
        monkey.x -= 5
    elif keyboard.up:
        monkey.y -= 5
    elif keyboard.down:
        monkey.y += 5
    
    # set position when monkey take out of screen
    if monkey.x > 600:
        monkey.x = 0
    elif monkey.x < 0:
        monkey.x = 600
    if monkey.y > 400:
        monkey.y = 0
    elif monkey.y < 0:
        monkey.y = 400
    

    monkey_collected = monkey.colliderect(banana)
    if monkey_collected:
        place_banana()
        score += 1


def time_up():
    global game_over
    game_over = True

clock.schedule(time_up, 30.0) # 30 seconds
place_banana()
pgzrun.go()