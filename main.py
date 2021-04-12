import pygame
import random
screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

pygame.font.init()

background = pygame.image.load('background.png')
user = pygame.image.load('user.png')
chicken = pygame.image.load('chicken.png')

user_x = 150
user_y = 520
score = 0

def display_score(score):
    font = pygame.font.SysFont('Comic Sans MS',30)
    score_text = 'Score: '+ str(score)
    text_img = font.render(score_text,True, (0,255,0))
    screen.blit(text_img, [20,10])


def random_offset():
    return -1*random.randint(100, 2000)
chicken_y = [random_offset(),random_offset(),random_offset()]

def update_chicken_position(idx):

    global score
    if chicken_y [idx] > 600:
       chicken_y [idx] = random_offset()
       score = score + 5
       print('score',score)
    else:
       chicken_y [idx] = chicken_y[idx] + 5

def crashed(idx):
    global  score
    global keep_alive
    score = score - 5

    chicken_y [idx] = random_offset()
    if score < 0:
        keep_alive = False

keep_alive = True
clock = pygame.time.Clock()
while keep_alive:
    pygame.event.get()
    keys =  pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and user_x < 300:
        user_x += 10
    elif keys[pygame.K_LEFT] and user_x > 0:
        user_x -= 10



    update_chicken_position(0)
    update_chicken_position(1)
    update_chicken_position(2)

    screen.blit(background, [0,0])
    screen.blit(user, [user_x,user_y])
    screen.blit(chicken, [0,chicken_y[0]])
    screen.blit(chicken, [150,chicken_y[1]])
    screen.blit(chicken, [280,chicken_y[2]])

    if chicken_y[0] > 500 and user_x < 70:
        crashed(0)

    if chicken_y[1] > 500 and user_x > 80 and user_x < 200:
        crashed(1)
    if chicken_y[2] > 500 and user_x > 220:
        crashed(2)


    display_score(score)

    pygame.display.update()
    clock.tick(20)
