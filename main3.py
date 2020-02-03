import pygame
start_ticks = pygame.time.get_ticks() #starter tick
seconds = (pygame.time.get_ticks() - start_ticks)  # calculate how many seconds

while True:    # mainloop
    if seconds > 10:    # if more than 10 seconds close the game
        break
    print(start_ticks) # print how many seconds