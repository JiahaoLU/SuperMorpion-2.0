import sys
import pygame
from TDGame import *
from Image import *
import threading
from Client_Game import *
import Client_Instructions
from Keyboard_Convert import *

# collects the keyboard input at any time
def collect_instruction(morpion, isover, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # judges whether the local player is the current player,
        # in order to implement the actions corresponding to the player's keyboard input or not
        if morpion.current_player == morpion.local_player:
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
                print('append event:', into_str(event))
    while len(Client_Instructions.Client_ins_rece) != 0:
        event_str_rece = Client_Instructions.Client_ins_rece.popleft()
        print('pop event:', event_str_rece)
        event_key = into_ins(event_str_rece)    # cleans and excecutes the instructions received from the other player
        print(morpion.current_player.player_flag, morpion.local_player.player_flag)
        if event_key == 'QUIT':
            sys.exit()
        if not isover:
            if event_key == pygame.K_SPACE + 1000:
                morpion.forced_set_down_chess()
            else:
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

def getIP():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    h = s.getsockname()[0]
    s.close()
    return h

def client_game(host = getIP()):
    # to start client info-sender thread
    th_local = threading.Thread(target=client,args=(host,),daemon=True)
    th_local.start()
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
    # monitors the game conditions and keyboard input at any time
    # function count_down_encap initialization
    judgement_for_countdown = False
    local_bombclock = None
    time_left = 30
    while True:
        (judgement_for_countdown,local_bombclock,time_left) = count_down_encap(morpion,judgement_for_countdown,local_bombclock,time_left)
        frame_count, click_on = image_count(frame_count, click_on)  # Blinking pointer
        collect_instruction(morpion, isover, screen)                # Collects the keyboard input at any time
        screen.fill((255, 255, 255))                                # Background of the screen = white
        grids = Grids()                                             # Graphic appearance of the Morpion
        draw_visuals(morpion, click_on, screen, grids, images, time_left)   # Also displays the countdown
        # if the game is over, displays a message about the winner
        # and blocks any further manipulation, except for R (restart the game)
        isover = over_instructions(morpion, screen)
        pygame.display.update()
        clock.tick(10)


def count_down_encap(morpion,judgement_for_countdown,local_bombclock,time_left):
    print('The game is not over')
    if Client_Instructions.Client_player:
        morpion.local_player = morpion.players[0]               # Run initially to give a number to each player
    else:
        morpion.local_player = morpion.players[1]

    # Starts a countdown clock only for the current player (the other one doesn't need to see the time left to play)
    if morpion.local_player == morpion.current_player:
        if not judgement_for_countdown:                         # If last time the loop was used, it wasn't the turn of the local player
            local_bombclock = Bombclock()                       # Initializes the clock with 30 seconds left and starts the countdown
            print('Bombclock initialized')                      # Useful in case of bug
        time_left = local_bombclock.count_down()                # Returns the time left
        print('countdown prompted')                             # Useful in case of bug

        if local_bombclock.count_down() == 0 and not morpion.isover():   # If the time's up, the current player is forced to set down his/her chess
            Client_Instructions.Client_ins_send.append('space_time_up')  # store local_player's instructions to be ready to send
            print('append event:', 'space_time_up')

    return ((morpion.current_player == morpion.local_player),local_bombclock,time_left)# Last time the machine checked, it was the turn of the local player
