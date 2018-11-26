import pygame
import random

WHITE = (255, 255, 255)

Running = True
class Hero(pygame.sprite.Sprite):
    #This class represents a Hero. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the Hero, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        # Draw the object
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveUp(self, pixels):
        self.rect.y -= pixels

    def moveDown(self, pixels):
        self.rect.y += pixels

    def attack(self):
        pygame.draw.rect(WHITE, )

class Enemy(pygame.sprite.Sprite):
    #This class represents an Enemy. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height, vel):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the Hero, and its x and y position, width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.vel = vel
        # Draw the object
        pygame.draw.rect(self.image, color, [0, 0, width, height])
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x -= self.vel
        self.rect.y -= -4


#Making the starting and end points random
def randomLocation(start):
    chance = random.randint(1,2)
    if (start == True and chance == 1):
        x = random.randrange(0, 500, 1)
        return (x)
    elif (start == True and chance == 2):
        x = random.randrange(0, 500, 499)
        return(x)
    elif (start == False and chance == 1):
        y = random.randrange(0, 500, 499)
        return (y)
    elif (start == False and chance == 1):
        y = random.randrange(0, 500, 1)
        return(y)

