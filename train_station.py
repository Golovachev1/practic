import pygame, sys
class Train_station:
    def __init__(self):
        self.image = pygame.image.load("Rebricha.png")
        self.rectTsimg = self.image.get_rect()
 
        self.tsY1 = 0
        self.tsX1 = -450
 
        self.tsY2 = self.rectTsimg.height
        self.tsX2 = -450
 
        self.movingUpSpeed = 5

        self.image1 = pygame.image.load("Kor1.png")
        self.rectTsimg1 = self.image1.get_rect()

        self.tsY3 = 0
        self.tsX3 = -450
 
        self.tsY4 = self.rectTsimg1.height
        self.tsX4 = -450

        self.image2 = pygame.image.load("Gilevka.png")
        self.rectTsimg2 = self.image2.get_rect()
 
        self.tsY5 = 0
        self.tsX5 = -450
 
        self.tsY6 = self.rectTsimg2.height
        self.tsX6 = -450

        self.image3 = pygame.image.load("Barnaul.png")
        self.rectTsimg3 = self.image3.get_rect()
 
        self.tsY7 = 210
        self.tsX7 = 655
 
        self.tsY8 = self.rectTsimg3.height
        self.tsX8 = -450

        self.image4 = pygame.image.load("lenki.png")
        self.rectTsimg4 = self.image4.get_rect()
 
        self.tsY9 = 0
        self.tsX9 = -450
 
        self.tsY10 = self.rectTsimg4.height
        self.tsX10 = -450
 
        self.movingUpSpeed = 5

        self.image5 = pygame.image.load("Blagov.png")
        self.rectTsimg5 = self.image5.get_rect()

        self.tsY11 = 0
        self.tsX11 = -450
 
        self.tsY12 = self.rectTsimg5.height
        self.tsX12 = -450

        self.image6 = pygame.image.load("Kulunda.png")
        self.rectTsimg6 = self.image6.get_rect()
 
        self.tsY13 = 0
        self.tsX13 = -450
 
        self.tsY14 = self.rectTsimg6.height
        self.tsX14 = -450
         
    def update(self):
        self.tsY1 += self.movingUpSpeed
        self.tsY2 += self.movingUpSpeed
        if self.tsY1 == self.rectTsimg.height + 1300:
            self.tsY1 = -self.rectTsimg.height - 300
        if self.tsY2 == self.rectTsimg.height + 1300:
            self.tsY2 = -self.rectTsimg.height - 300
            self.tsX2 = 655

        self.tsY3 += self.movingUpSpeed
        self.tsY4 += self.movingUpSpeed
        if self.tsY3 == self.rectTsimg1.height + 2900:
            self.tsY3 = -self.rectTsimg1.height - 300
        if self.tsY4 == self.rectTsimg1.height + 2900:
            self.tsY4 = -self.rectTsimg1.height - 300
            self.tsX4 = 670

        self.tsY5 += self.movingUpSpeed
        self.tsY6 += self.movingUpSpeed
        if self.tsY5 == self.rectTsimg2.height + 4300:
            self.tsY5 = -self.rectTsimg2.height - 300
        if self.tsY6 == self.rectTsimg2.height + 4300:
            self.tsY6 = -self.rectTsimg2.height - 300
            self.tsX6 = 655

        self.tsY7 += self.movingUpSpeed
        self.tsY8 += self.movingUpSpeed
        if self.tsY7 == self.rectTsimg3.height + 100:
            self.tsY7 = -self.rectTsimg3.height + 300
        if self.tsY8 == self.rectTsimg3.height + 100:
            self.tsY8 = -self.rectTsimg3.height + 300

        self.tsY9 += self.movingUpSpeed
        self.tsY10 += self.movingUpSpeed
        if self.tsY9 == self.rectTsimg4.height + 5700:
            self.tsY9 = -self.rectTsimg4.height - 300
        if self.tsY10 == self.rectTsimg4.height + 5700:
            self.tsY10 = -self.rectTsimg4.height - 300
            self.tsX10 = 655

        self.tsY11 += self.movingUpSpeed
        self.tsY12 += self.movingUpSpeed
        if self.tsY11 == self.rectTsimg5.height + 7100:
            self.tsY11 = -self.rectTsimg5.height - 300
        if self.tsY12 == self.rectTsimg5.height + 7100:
            self.tsY12 = -self.rectTsimg5.height - 300
            self.tsX12 = 670

        self.tsY13 += self.movingUpSpeed
        self.tsY14 += self.movingUpSpeed
        if self.tsY13 == self.rectTsimg6.height + 8500:
            self.tsY13 = -self.rectTsimg6.height - 300
        if self.tsY14 == self.rectTsimg6.height + 8500:
            self.tsY14 = -self.rectTsimg6.height - 300
            self.tsX14 = 672
            
             
    def render(self):
         DISPLAYSURF.blit(self.image, (self.tsX1, self.tsY1))
         DISPLAYSURF.blit(self.image, (self.tsX2, self.tsY2))

         DISPLAYSURF.blit(self.image1, (self.tsX3, self.tsY3))
         DISPLAYSURF.blit(self.image1, (self.tsX4, self.tsY4))

         DISPLAYSURF.blit(self.image2, (self.tsX5, self.tsY5))
         DISPLAYSURF.blit(self.image2, (self.tsX6, self.tsY6))

         DISPLAYSURF.blit(self.image3, (self.tsX7, self.tsY7))
         DISPLAYSURF.blit(self.image3, (self.tsX8, self.tsY8))

         DISPLAYSURF.blit(self.image4, (self.tsX9, self.tsY9))
         DISPLAYSURF.blit(self.image4, (self.tsX10, self.tsY10))

         DISPLAYSURF.blit(self.image5, (self.tsX11, self.tsY11))
         DISPLAYSURF.blit(self.image5, (self.tsX12, self.tsY12))

         DISPLAYSURF.blit(self.image6, (self.tsX13, self.tsY13))
         DISPLAYSURF.blit(self.image6, (self.tsX14, self.tsY14))

DISPLAYSURF = pygame.display.set_mode((1000,600))
DISPLAYSURF.fill((61, 12, 2))
