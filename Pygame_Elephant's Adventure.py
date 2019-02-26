import pygame
import time
import random

pygame.init()

# R,G,B - SomeColors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)



#SettingFrame
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Elephant's adventure")

#LoadingImages
skyImg = pygame.image.load("./image/background.jpg")
skyImg = pygame.transform.scale(skyImg, (display_width, display_height))
playerImg = pygame.image.load("./image/cute_man.png")
playerImg = pygame.transform.scale(playerImg, (80, 80))
stoneImgsrc = pygame.image.load("./image/stone.png")
stoneImg = pygame.transform.scale(stoneImgsrc, (50, 50))
stone2Img = pygame.transform.scale(stoneImgsrc, (75, 75))
coinImg = pygame.image.load("./image/coin.png")
coinImg = pygame.transform.scale(coinImg, (50, 50))

#SettingClock
clock = pygame.time.Clock()

#PlayerClassParameters
playerparms = [playerImg, 20, 377, 450, 50, 50, 1.1]


# BackgroundClass
class Background:
    def __init__(self, bg_img, bg_x, bg_y):
        self.bg_x = bg_x
        self.bg_y = bg_y
        gameDisplay.blit(bg_img, (bg_x, bg_y))

# PlayerClass
class Player:
    def __init__(self,p_img,speedIn,player_x,player_y,hitbox_x,hitbox_y,speedmultiplier):
        self.speed = speedIn
        self.player_x = player_x
        self.player_y = player_y
        self.p_img = p_img
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y
        self.speedmult = speedmultiplier


# GameObjectsClass
class Gameobject:
    def __init__(self, b_image, speed, coord_x, coord_y, hitbox_x, hitbox_y):
        self.b_image = b_image
        self.speed = speed
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y

# ScoreFunction
def scorecounter(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score:" + str(count), True, black)
    gameDisplay.blit(text, (0, 0))

# CrashFunction
def text_objects(text, font):
    textsurface = font.render(text, True, red)
    return textsurface, textsurface.get_rect()

# MessageDisplay
def message_display(text):
    largeText = pygame.font.Font(None, 46)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


#MainGame
def game_loop():
#CreatingObjects
    player = Player(playerparms[0],playerparms[1],playerparms[2],playerparms[3],playerparms[4],playerparms[5],playerparms[6])
    coin = Gameobject(coinImg, 5, random.randrange(0, display_width - 50),-600,50,50)
    stone1 = Gameobject(stoneImg, 3, random.randrange(0, display_width - 50),-600,40,40)
    stone2 = Gameobject(stone2Img, 6, random.randrange(0, display_width - 75),-1000,65,65)
#Constants
    x_change = 0
    score = 0

    gameexit = False
#GameLoop
    while not gameexit:

#Background
        bg = Background(skyImg, 0, 0)

# Objects
        gameDisplay.blit(coin.b_image, (coin.coord_x, coin.coord_y))
        gameDisplay.blit(stone1.b_image, (stone1.coord_x, stone1.coord_y))
        gameDisplay.blit(stone2.b_image, (stone2.coord_x, stone2.coord_y))

#Player
        gameDisplay.blit(player.p_img, (player.player_x,player.player_y))

#Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.player_x > 0:
                    x_change = player.speed * -1 + -1 * player.speedmult * score
                elif event.key == pygame.K_RIGHT and player.player_x < display_width - 45:
                    x_change = player.speed + player.speedmult * score
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        player.player_x += x_change

        # print(event)

# ObjectSpeeds
        coin.coord_y += coin.speed
        stone1.coord_y += stone1.speed + 1.2 * score
        stone2.coord_y += stone1.speed + 1.2 * score


# Boundaries
        if player.player_x > display_width - player.hitbox_x or player.player_x < 0:
            x_change = 0

# RecallingObjects

        if coin.coord_y > display_height:
            coin.coord_y = -10
            coin.coord_x = random.randrange(0, display_width - 50)
        if stone1.coord_y > display_height - 10:
            stone1.coord_y = -10
            stone1.coord_x = random.randrange(0, display_width - 50)
        if stone2.coord_y > display_height:
            stone2.coord_y = -410
            stone2.coord_x = random.randrange(0, display_width - 75)


# Score
        scorecounter(score)

# Collisons
    # stone1
        if player.player_y < stone1.coord_y + stone1.hitbox_y and player.player_y > stone1.coord_y or player.player_y + player.hitbox_y > stone1.coord_y and player.player_y + player.hitbox_y < stone1.coord_y + stone1.hitbox_y:
            if player.player_x > stone1.coord_x and player.player_x < stone1.coord_x + stone1.hitbox_x or player.player_x + player.hitbox_x > stone1.coord_x and player.player_x + player.hitbox_x < stone1.coord_x + stone1.hitbox_x:
                message_display("YOU LOSE!")

    # stone2
        if player.player_y < stone2.coord_y + stone2.hitbox_y and player.player_y > stone2.coord_y or player.player_y + player.hitbox_y > stone2.coord_y and player.player_y + player.hitbox_y < stone2.coord_y + stone2.hitbox_y:
            if player.player_x > stone2.coord_x and player.player_x < stone2.coord_x + stone2.hitbox_x or player.player_x + player.hitbox_x > stone2.coord_x and player.player_x + player.hitbox_x < stone2.coord_x + stone2.hitbox_x:
                message_display("YOU LOSE!")

    # coin
        if player.player_y < coin.coord_y + coin.hitbox_y and player.player_y > coin.coord_y or player.player_y + player.hitbox_y > coin.coord_y and player.player_y + player.hitbox_y < coin.coord_y + coin.hitbox_y:
            if player.player_x > coin.coord_x and player.player_x < coin.coord_x + coin.hitbox_x or player.player_x + player.hitbox_x > coin.coord_x and player.player_x + player.hitbox_x < coin.coord_x + coin.hitbox_x:
                coin.coord_y = -10
                coin.coord_x = random.randrange(0, display_width - 50)
                score += 1
                print(score)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.QUIT()
quit()