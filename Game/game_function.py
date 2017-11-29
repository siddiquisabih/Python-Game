import  sys
import  pygame

def check_event():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()


def update_screen( gameSetting ,screen , ship):
    screen.fill(gameSetting.bg_color)
    ship.blitme()
    pygame.display.flip()
