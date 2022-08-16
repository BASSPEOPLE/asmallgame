import pygame
import random
import os

FPS=60

WIDTH=500
HEIGHT=600

WHITE=(255,255,255)
GREEN=(0,255,0)
RED = (255,0,0)
YELLOW=(255,255,0)
BLACK=(0,0,0)

#遊戲初始化and 創建視窗
pygame.init()   
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("學習製作遊戲")
Clock=pygame.time.Clock() #FPS

ghost_img = pygame.image.load(os.path.join("asmallgame","img","ghost1.jpg")) .convert()
player_img = pygame.image.load(os.path.join("asmallgame","img","player.png")) .convert()
background_img = pygame.image.load(os.path.join("asmallgame","img","background.png")) .convert()
player4_img = pygame.image.load(os.path.join("asmallgame","img","player4.png")) .convert()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player4_img,(30,40)) 
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom =  600
        self.speed = 5

    def update(self) :
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed
        if key_pressed[pygame.K_UP]:
            self.rect.y -= self.speed

        if self.rect.right >  WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0  
        if self.rect.bottom >  HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0 

        
        
        


all_sprites=pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running=True

#遊戲迴圈
while running:
    Clock.tick(FPS)
    # 取得輸入 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        

        

    #更新
    all_sprites.update()

    #畫面顯示
    screen.fill(BLACK)
    screen.blit(background_img,(0,0))
    all_sprites.draw(screen)
    
    pygame.display.update()
    

pygame.quit()   