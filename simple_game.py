import pygame
from random import choice, randint

pygame.init()
pygame.display.set_caption("Simple Game")
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
running = True

#Points
score = int(0)

#Definition os player properties
player_x = screen.get_width() / 2 
player_y = screen.get_height() - 100
player_speed = 5

ball_x = randint(10, int(screen.get_width()-10))
ball_y = 10
ball_velocity = 3
ball_direction = choice(["n", "s", "nl", "no", "sl", "so"])

#Function to verify the limits of the screen and the player
def Limits():
    global player_x, player_y
    #The player will apear in the inverse side
    if player_x > screen.get_width():
        player_x = 0
    elif player_x+100 < 0:
        player_x = screen.get_width()

#Function to verify the ball moviment
def Ball_Moviment():
    global ball_x, ball_y, ball_direction
    if ball_direction == "n":
        ball_y -= ball_velocity
    elif ball_direction == "no":
        ball_x -= ball_velocity
        ball_y -= ball_velocity
    elif ball_direction == "nl":
        ball_x += ball_velocity
        ball_y -= ball_velocity
    elif ball_direction == "s":
        ball_y += ball_velocity
    elif ball_direction == "so":
        ball_x -= ball_velocity
        ball_y += ball_velocity
    elif ball_direction == "sl":
        ball_x += ball_velocity
        ball_y += ball_velocity

    #print(f"Ball: X={ball_x}, Y={ball_y}")    

#Function to verify the ball colision
def Ball_Colision():
    global ball_x, ball_y, ball_direction
    if ball_y >= screen.get_height():
        opt = ["n", "nl", "no"]
        ball_direction = choice(opt) 
    elif ball_y <= 0:
        opt = ["s", "sl", "so"]
        ball_direction = choice(opt)
    elif ball_x >= screen.get_width():
        opt = ["no", "so"]
        ball_direction = choice(opt)
    elif ball_x <= 0:
        opt = ["nl", "sl"]
        ball_direction = choice(opt)

#Funcion to verify the position bettwen the player and the ball
def Position():
    global player_x, player_y, ball_x, ball_y, ball_direction, ball_velocity, score
    if (player_x < ball_x < player_x+100) and (player_y < ball_y < player_y+20):
        opt = ["n", "nl", "no"]
        ball_direction = choice(opt)
        ball_velocity += 0.1
        score += 10
    #Reset the game    
    elif ball_y >= screen.get_height():
        score = 0
        ball_velocity = 3
        player_x = screen.get_width() / 2
        ball_x = randint(10, int(screen.get_width()-10))
        ball_y = 10

#Game loop
while running:
    Limits()
    Ball_Moviment()
    Ball_Colision()
    Position()
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Clear the screen
    screen.fill("black")

    #Draw in the screen
    pygame.draw.circle(screen, "white", (ball_x, ball_y), 10)
    pygame.draw.rect(screen, "red", (player_x, player_y, 100, 20))

    #Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    #Update screen
    Score_Text = font.render(f"Score: {score}", True, "white")
    screen.blit(Score_Text, (10, 10))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
