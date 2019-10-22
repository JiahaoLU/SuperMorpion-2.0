import sys
from pygame import *
from TDGame import *
from Image import *
import threading
from Client_Game import *
import Client_Instructions

# collects the keyboard input at any time
def collect_instruction(morpion, isover, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # judges whether the local player is the current player, in order to validate or cancel this press on keyboard
        if morpion.current_player == morpion.local_player:
            show_text(screen, (100, 10), 'It is your turn!', (227, 29, 18), False, 50)
            if event.type == pygame.KEYDOWN:
                # if the game is not over, it has to go on
                if not isover:
                    morpion.move(event.key)
                # if the game is over, and the players want to go for another round
                elif event.key == pygame.K_r:   # predefined pygame function to check is the player presses R
                        # to start another round, the infos AND the visuals of the morpion need to be cleaned
                    morpion.create_board()
            event_str_send = into_str(event)
            if event_str_send != None:
                Client_Instructions.Client_ins_send.append(into_str(event)) # store local_player's instructions to be ready to send
                print('append event:',into_str(event))
    while len(Client_Instructions.Client_ins_rece) != 0:
        event_str_rece = Client_Instructions.Client_ins_rece.popleft()
        print('pop event:',event_str_rece)
        event_key = into_ins(event_str_rece)# clean and excecute received instructions from the other player
        print(morpion.current_player.player_flag, morpion.local_player.player_flag)
        if event_key == 'QUIT':
            sys.exit()
        # elif morpion.current_player.player_flag == morpion.local_player.player_flag:
            # judge whether local player is current player, in order to validate or cancel this press on keyboard
            # if the game is not over, it has to go on
        if not isover:
            morpion.move(event_key)
            print('event_key works:', event_key)
        # if the game is over, and the players want to go for another round
        elif event_key == pygame.K_r:   # predefined pygame function to check is the player presses R
                # to start another round, the infos AND the visuals of the morpion need to be cleaned
            morpion.create_board()

# judges whether the game is over, shows the winner's infos
def over_instructions(morpion, screen):
    isover = morpion.isover()           # function that returns True if there is a winner or if the Morpion is full
    if isover:
        if morpion.iswin():
            show_text(screen, (100, 10),
                      'Player {} wins!'.format(str(morpion.winner.player_number)) + ' ',
                      (227, 29, 18), False, 50)
            winner_number = str(morpion.winner.player_number)     # fetches the information we want to display on the screen
            winner_score = morpion.winner.player_score
            show_text(screen, (100, 50),
                      'Player {0} new score : {1}'.format(winner_number, winner_score)
                      + ' ', (227, 29, 18), False, 50)
            show_text(screen, (150, 90), 'press R to try again...', (0, 0, 22), False, 30)
        else:
            show_text(screen, (100, 10), 'draw', (227, 29, 18), False, 100)
            show_text(screen, (150, 30), 'press R to try again...', (0, 0, 22), False, 30)
    return isover

def main():
    # parameters for initialisation
    pygame.init()                   # Usual initialization of all the pygame modules
    images = load_images()
    coordonates = Coordonates()     # Initialization of the global graphic parameters (class defined in Parameters.py)
    screen_size = (coordonates.screen_X, coordonates.screen_Y)  # Fetches back the dimensions of the screen that are /
                                                                # ... defined by default in the Coordonates class
    screen = pygame.display.set_mode(screen_size)               # Uses the pygame function to initialize the screen /
                                                                # ... with the dimensions given above
    pygame.display.set_caption('Morpion')                       # Text to display as the name of the window
    clock = pygame.time.Clock()     # Time used for the blinking pointer
    frame_count = 0                 # Function that makes the pointer blink
    click_on = False                # Starts with the pointer being not visible
    isover = False                  # the game is not over yet
    morpion = Morpion()             # initialization of the chessboard (class in TDGame)
    morpion.score_increased = 0     # variable that checks if the score of the winner has already been increased or not
    th_local = threading.Thread(target=client,args=(),daemon=True)
    th_local.start()
    counter_click = 0

    # monitors the game conditions and keyboard input at any time
    while True:
        print('The game is not over')
        if Client_Instructions.Client_player == True:
            morpion.local_player = morpion.players[0]
        else:
            morpion.local_player = morpion.players[1]
        frame_count, click_on = image_count(frame_count, click_on) # Blinking pointer
        grids = Grids()                                            # Graphic appearance of the Morpion
        collect_instruction(morpion, isover, screen)     # Collects the keyboard input at any time
        screen.fill((255, 255, 255))                    # Background of the screen = white
        draw_visuals(morpion, click_on, screen, grids, images)
        # if the game is over, displays a message about the winner
        # and blocks any further manipulation, except for R (restart the game)
        isover = over_instructions(morpion, screen)
        pygame.display.update()
        clock.tick(10)

if __name__ == '__main__':
    main()



##############
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
