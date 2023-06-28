import pygame, sys
class Train:
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("poezd.png")
        self.rectTsimg3 = self.image.get_rect()
 
        self.pY7 = 210
        self.pX7 = 575
 
        self.pY8 = self.rectTsimg3.height
        self.pX8 = -450

        self.image1 = pygame.image.load("poezd1.png")
        self.rectPimg = self.image1.get_rect()
 
        self.pY1 = 0
        self.pX1 = -150
 
        self.pY2 = self.rectPimg.height
        self.pX2 = -150
 
        self.movingUpSpeed = 10

        self.image2 = pygame.image.load("poezd1.png")
        self.rectPimg1 = self.image2.get_rect()
 
        self.pY3 = 0
        self.pX3 = -150
 
        self.pY4 = self.rectPimg1.height
        self.pX4 = -150

        self.image3 = pygame.image.load("poezd1.png")
        self.rectPimg2 = self.image3.get_rect()
 
        self.pY5 = 0
        self.pX5 = -150
 
        self.pY6 = self.rectPimg2.height
        self.pX6 = -150

         
    def update(self):
        self.pY1 += self.movingUpSpeed
        self.pY2 += self.movingUpSpeed
        if self.pY1 == self.rectPimg.height + 1900:
            self.pY1 = -self.rectPimg.height - 300
        if self.pY2 == self.rectPimg.height + 1900:
            self.pY2 = -self.rectPimg.height - 300
            self.pX2 = 395

        self.pY3 += self.movingUpSpeed
        self.pY4 += self.movingUpSpeed
        if self.pY3 == self.rectPimg1.height + 7200:
            self.pY3 = -self.rectPimg1.height - 300
        if self.pY4 == self.rectPimg1.height + 7200:
            self.pY4 = -self.rectPimg1.height - 300
            self.pX4 = 395

        self.pY5 += self.movingUpSpeed
        self.pY6 += self.movingUpSpeed
        if self.pY5 == self.rectPimg2.height + 10800:
            self.pY5 = -self.rectPimg2.height - 300
        if self.pY6 == self.rectPimg2.height + 10800:
            self.pY6 = -self.rectPimg2.height - 300
            self.pX6 = 395
            
             
    def render(self):
         DISPLAYSURF.blit(self.image1, (self.pX1, self.pY1))
         DISPLAYSURF.blit(self.image1, (self.pX2, self.pY2))
         DISPLAYSURF.blit(self.image2, (self.pX3, self.pY3))
         DISPLAYSURF.blit(self.image2, (self.pX4, self.pY4))
         DISPLAYSURF.blit(self.image3, (self.pX5, self.pY5))
         DISPLAYSURF.blit(self.image3, (self.pX6, self.pY6))
         DISPLAYSURF.blit(self.image, (self.pX7, self.pY7))
         DISPLAYSURF.blit(self.image, (self.pX8, self.pY8))

DISPLAYSURF = pygame.display.set_mode((1000,600))
DISPLAYSURF.fill((61, 12, 2))

