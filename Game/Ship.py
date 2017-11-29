import  pygame

class Ship():
    def __init__(self , setting , screen ):

            #initialize the screen
        self.screen  = screen
        self.setting = setting

        # load the ship image and get its rect

        self.image = pygame.image.load("Images/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_Left = False



    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.center +=self.setting.ship_speed_factor

        if self.moving_Left and self.rect.left > 0:
            self.center -=self.setting.ship_speed_factor

        self.rect.centerx = self.center


    def blitme(self):
     """Draw the ship at its current location."""
     self.screen.blit(self.image, self.rect)