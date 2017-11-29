import  pygame
from Settings import  Setting
from Ship import Ship
import  game_function as gf

def runGame():

    # Initialize game and create a screen object.

    pygame.init()

    gameSetting = Setting()

    screen = pygame.display.set_mode((gameSetting.screen_width , gameSetting.screen_height))


    pygame.display.set_caption("Alien Invasion")

    ship = Ship( gameSetting,screen)

    # Start the main loop for the game.

    while True:

    # Watch for keyboard and mouse events.

     gf.check_event(ship)
     ship.update()
     gf.update_screen(gameSetting , screen , ship)





runGame()