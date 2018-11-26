import pygame, random
from Game_Lib import *
pygame.init()

GREEN = (20, 255, 140)
GREY = (210, 210 ,210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
      
SCREENWIDTH=500
SCREENHEIGHT=500

spawnCount = 5
sp = spawnCount
pvel = 5
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Dodge the enemy")

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

#creating sprites
playerHero = Hero(RED, 20, 30)
playerHero.rect.x = 200
playerHero.rect.y = 200

# Add the characters to the list of objects
all_sprites_list.add(playerHero)


#Allowing the user to close the window...

clock = pygame.time.Clock()
 
while Running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Running = False
        print(clock)
        if sp == 0: 
                enemy1 = Enemy(PURPLE, 15, 15, random.randrange(-5,5, 1))
                enemy1.rect.x = random.randrange(0, 500, 1)
                enemy1.rect.y = 0
                enemy1.vel
                enemy_list.add(enemy1)
                sp = spawnCount
        sp -= 1
        #Game Logic
        all_sprites_list.update()
        enemy_list.update()

        #Drawing on Screen
        screen.fill(GREEN)
        
        #Drawing all sprites
        all_sprites_list.draw(screen)
        enemy_list.draw(screen)

        #Making the character Move
        if (playerHero.rect.x > 5):
                if pygame.key.get_pressed()[pygame.K_LEFT]:
                        playerHero.moveLeft(pvel)

        if (playerHero.rect.y > 5):
                if pygame.key.get_pressed()[pygame.K_UP]:
                        playerHero.moveUp(pvel)

        if (playerHero.rect.x < 490):
                 if pygame.key.get_pressed()[pygame.K_RIGHT]:
                        playerHero.moveRight(pvel)

        if (playerHero.rect.y < 490):
                if pygame.key.get_pressed()[pygame.K_DOWN]:
                        playerHero.moveDown(pvel)  

        if pygame.key.get_pressed()[pygame.K_a]:
                playerHero.attack
        #Making Enemy Move
        

        #Detect if the hero is hitting the enemy
        if (pygame.sprite.spritecollide(playerHero, enemy_list, False)):
                Running = False

        #print(playerHero.rect.x)
        #Refresh Screen
        pygame.display.flip()
 
        #Number of frames per secong e.g. 60
        clock.tick(60)
 
pygame.quit()
