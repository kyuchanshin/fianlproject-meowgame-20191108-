import pygame
import random
from pygame.rect import *
from pygame import mixer

pygame.init()
pygame.display.set_caption("final DDR")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
WAIT_TIME = 400

mixer.init()

def playMeowSound():
    mixer.Sound("리듬게임/meow.mp3").play()

def playPerfectSound():
    mixer.Sound("리듬게임/perfect.mp3").play()


background = pygame.image.load("리듬게임/back.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

mixer.music.load("리듬게임/catsong.mp3")
mixer.music.play(-1)  

def resultProcess(direction):
    global isColl, score, DrawResult, result_ticks

    if isColl and CollDirection.direction == direction:
        score += 10
        CollDirection.y = -1
        DrawResult = 1
        playPerfectSound()
    else:
        DrawResult = 2
    result_ticks = pygame.time.get_ticks()

def eventProcess():
    global isActive, score, chance
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isActive = False
            if chance > 0:
                if event.key == pygame.K_UP: 
                    resultProcess(0)
                    playMeowSound()  
                if event.key == pygame.K_LEFT: 
                    resultProcess(1)
                    playMeowSound()
                if event.key == pygame.K_DOWN:  
                    resultProcess(2)
                    playMeowSound()
                if event.key == pygame.K_RIGHT:  
                    resultProcess(3)
                    playMeowSound()
            else:
                if event.key == pygame.K_SPACE:
                    score = 0
                    chance = chance_MAX
                    for direc in Directions:
                        direc.y = -1

class Direction(object):
    def __init__(self, direction, initial_x):
        self.pos = None
        self.direction = direction
        self.image = pygame.image.load(f"리듬게임/paw.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rotated_image = pygame.transform.rotate(self.image, 0)
        self.y = -1
        self.x = initial_x
        self.wait_time = random.randint(0, WAIT_TIME) 

    def rotate(self, direction=0):
        self.direction = direction
        self.rotated_image = pygame.transform.rotate(
            self.image, 90*self.direction)

    def draw(self):
        if self.wait_time > 0:
            #print(self.wait_time)
            self.wait_time -= 1

        else:
            self.y += 1
            self.pos = screen.blit(self.rotated_image, (self.x, self.y))
        
    def checkPos(self):
        if self.y >= SCREEN_HEIGHT:
            print(self.y)
            return True
        else:
            return False

def drawIcon():
    global chance

    if chance <= 0:
        return

    for direc in Directions:
        if direc.wait_time == 0 and direc.y == -1:
            direc.y = 0
            direc.rotate(direction=random.randint(0, 3))

        direc.draw()
        if direc.checkPos():
            direc.y = -1
            direc.wait_time = random.randint(0, WAIT_TIME) 
            chance -= 1


targetArea = Rect(0, SCREEN_HEIGHT//4 + 350, SCREEN_WIDTH//1.1 + 73, 60)

def draw_targetArea():
    global isColl, CollDirection
    isColl = False
    for direc in Directions:
        if direc.y == -1:
            continue
        if direc.pos and direc.pos.colliderect(targetArea):
            isColl = True
            CollDirection = direc
            pygame.draw.rect(screen, (255, 255, 0), targetArea)
            break
    pygame.draw.rect(screen, (153, 204, 255), targetArea, 5)


def setText():
    global score, chance
    mFont = pygame.font.SysFont("gulim", 40)

    mtext = mFont.render(f'score : {score}', True, 'black')
    screen.blit(mtext, (10, 10, 0, 0))

    mtext = mFont.render(f'chance : {chance}', True, 'red')
    screen.blit(mtext, (10, 42, 0, 0))

    if chance <= 0:
        mFont = pygame.font.SysFont("gulim", 50)
        mtext = mFont.render(f'Game over!! Press Spacebar to restart', True, 'red')
        tRec = mtext.get_rect()
        tRec.centerx = SCREEN_WIDTH/2
        tRec.centery = SCREEN_HEIGHT/2 - 40
        screen.blit(mtext, tRec)

def drawResult():
    global DrawResult, result_ticks
    if result_ticks > 0:
        elapsed_time = (pygame.time.get_ticks() - result_ticks)
        if elapsed_time > 400:
            result_ticks = 0
            DrawResult = 0
    screen.blit(resultImg[DrawResult], resultImgRec)
    
    if DrawResult == 1:  
        mFont = pygame.font.SysFont("gulim", 60)
        mtext = mFont.render(f'perfect!!', True, 'blue')
        tRec = mtext.get_rect()
        tRec.centerx = SCREEN_WIDTH/2
        tRec.centery = SCREEN_HEIGHT/3 - 230
        screen.blit(mtext, tRec)
    
    if DrawResult == 2: 
        mFont = pygame.font.SysFont("gulim", 60)
        mtext = mFont.render(f'terrible~~', True, 'red')
        tRec = mtext.get_rect()
        tRec.centerx = SCREEN_WIDTH/2
        tRec.centery = SCREEN_HEIGHT/3 - 230
        screen.blit(mtext, tRec)

isActive = True
chance_MAX = 10
score = 0
chance = chance_MAX
isColl = False
CollDirection = 0
DrawResult, result_ticks = 0,0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
Directions = [Direction(0, SCREEN_WIDTH//5), Direction(1, SCREEN_WIDTH//4), Direction(2, 3*SCREEN_WIDTH//4), Direction(3, SCREEN_WIDTH//2)]

resultFileNames = ["리듬게임/sososo.png", "리듬게임/perfect.png", "리듬게임/terrible.png"]
resultImg = []
for i, name in enumerate(resultFileNames):
    resultImg.append(pygame.image.load(name))
    resultImg[i] = pygame.transform.scale(resultImg[i], (150, 75))

resultImgRec = resultImg[0].get_rect()
resultImgRec.centerx = SCREEN_WIDTH/2
resultImgRec.centery = targetArea.centery + 110

while(isActive):
    screen.blit(background, (0, 0))
    
    eventProcess()
    draw_targetArea()
    drawIcon()
    setText()
    drawResult()
    pygame.display.update()
    clock.tick(250)
