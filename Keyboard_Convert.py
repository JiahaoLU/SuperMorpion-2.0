import pygame
def into_str(event): # convert event type into string in order to send instructions to server
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_e:
            return 'e'
        elif event.key == pygame.K_d:
            return 'd'
        elif event.key == pygame.K_UP:
            return 'up'
        elif event.key == pygame.K_DOWN:
            return 'down'
        elif event.key == pygame.K_LEFT:
            return 'left'
        elif event.key == pygame.K_RIGHT:
            return 'right'
        elif event.key == pygame.K_SPACE:
            return 'space'
        elif event.key == pygame.K_r:
            return 'r'
    elif event.type == pygame.QUIT:
        return 'QUIT'
    # else:
    #     return

def into_ins(str): # convert event type into string in order to send instructions to server
    if str == 'e':
        return pygame.K_e
    elif str == 'd':
        return pygame.K_d
    elif str == 'up':
        return pygame.K_UP
    elif str == 'down':
        a = pygame.K_DOWN
    elif str == 'left':
        return pygame.K_LEFT
    elif str == 'right':
        return pygame.K_RIGHT
    elif str == 'space':
        return pygame.K_SPACE
    elif str == 'r':
        return pygame.K_r
    elif str == 'QUIT':
        return 'QUIT'
    # else:
    #     return
