import pygame
from TDGame import *
from Parameters import *

# Overall function for drawing all the visuals
def draw_visuals(morpion, imageOn, screen, grids, images, time_left):
    draw_images(morpion, imageOn, screen, grids)
    draw_captions(morpion, screen, images, time_left)


# General function for writing messages on the screen
def show_text(screen, pos, text, color, font_bold=False, font_size=55, font_italic=False):
    # words type and size
    cur_font = pygame.font.SysFont("Calibri", font_size)
    # overstriking
    cur_font.set_bold(font_bold)
    # declined
    cur_font.set_italic(font_italic)
    # words content
    text_fmt = cur_font.render(text, 1, color)
    # draw words
    screen.blit(text_fmt, pos)

# Loading of the images used to show to the player which key of his/her keyboard to use in order to play
def load_images():
    dimensions_keys_pictures = [20, 20]
    k_left_original = pygame.image.load("Left.png")
    k_left = pygame.transform.scale(k_left_original, dimensions_keys_pictures)
    k_right_original = pygame.image.load("Right.png")
    k_right = pygame.transform.scale(k_right_original, dimensions_keys_pictures)
    k_up_original = pygame.image.load("Up.png")
    k_up = pygame.transform.scale(k_up_original, dimensions_keys_pictures)
    k_down_original = pygame.image.load("Down.png")
    k_down = pygame.transform.scale(k_down_original, dimensions_keys_pictures)
    k_e_original = pygame.image.load("E.png")
    k_e = pygame.transform.scale(k_e_original, dimensions_keys_pictures)
    k_d_original = pygame.image.load("D.png")
    k_d = pygame.transform.scale(k_d_original, dimensions_keys_pictures)
    print("images loaded")
    return k_left, k_right, k_up, k_down, k_e, k_d, dimensions_keys_pictures


# drawing the informations about the players
def draw_captions(morpion, screen, images, time_left):

    # dynamic caption informing the player when it is his turn
    if morpion.local_player == morpion.current_player:
        if not morpion.isover():
            show_text(screen, (100, 10), 'It is your turn!', (227, 29, 18), False, 50)

        # Bombclock (countdown) display
        # Display of the time left for the player to play
        position_caption = [645, 20]
        position_numbers = list(position_caption)
        position_numbers[1] += 20

        if time_left >= 0 :
            show_text(screen, position_caption, "Play before the time is over", (227, 29, 18), False, 30)
            show_text(screen, position_numbers, str(int(time_left)), (227, 29, 18), False, 30)
        else :
            show_text(screen, position_caption, "Time's up", (227, 29, 18), False, 30)

    # caption for the scores
    caption_top_left_position = [745, 300]
    second_player_caption_position = list(caption_top_left_position)
    second_player_caption_position[1] += 50

    show_text(screen, caption_top_left_position, '   Player 1 score: {}'.format(morpion.players[0].player_score),
              (0, 0, 18), False, 30)
    show_text(screen, second_player_caption_position, '   Player 2 score: {}'.format(morpion.players[1].player_score),
              (0, 0, 18), False, 30)

    # informs each player of his/her color
    circle_radius = 9
    pygame.draw.circle(screen, (255, 0, 0), caption_top_left_position, circle_radius)
    pygame.draw.circle(screen, (0, 255, 0), second_player_caption_position, circle_radius)

    # caption "how to play"
    instruction1_top_left_position = [620, 630]
    show_text(screen, instruction1_top_left_position, 'To move, please use:',
              (0, 0, 18), False, 20)

    # pictures to show which keys of the keyboard to use to move on the screen
    k_left, k_right, k_up, k_down, k_e, k_d, dimensions_keys_pictures = images

    # position of the pictures
    k_left_position = [770, 625]
    k_down_position = list(k_left_position)
    k_down_position[0] += dimensions_keys_pictures[0]
    k_up_position = list(k_left_position)
    k_up_position[0] += dimensions_keys_pictures[0]
    k_up_position[1] -= dimensions_keys_pictures[1]
    k_right_position = list(k_left_position)
    k_right_position[0] += 2*dimensions_keys_pictures[0]
    k_e_position = list(k_left_position)
    k_e_position[0] += 4*dimensions_keys_pictures[0]
    k_d_position = list(k_left_position)
    k_d_position[0] += 5*dimensions_keys_pictures[0]

    # display of the pictures
    screen.blit(k_left, k_left_position)
    screen.blit(k_down, k_down_position)
    screen.blit(k_up, k_up_position)
    screen.blit(k_right, k_right_position)
    screen.blit(k_e, k_e_position)
    screen.blit(k_d, k_d_position)

    # caption for the space bar instruction
    instruction2_top_left_position = list(instruction1_top_left_position)
    instruction2_top_left_position[1] += 40
    show_text(screen, instruction2_top_left_position, 'To place a pawn, please use the space bar',
              (0, 0, 18), False, 20)
    # parameters : (screen, pos, text, color, font_bold=False, font_size=60, font_italic=False)



# frame counter and click shining switch
def image_count(frame_count, click_on):
    frame_count += 1
    if frame_count % 5 == 0:  # every 30 frames
        if click_on:  # if it's on
            click_on = False  # turn it off
        elif not click_on:  # if it's off
            click_on = True  # turn it on
    return frame_count, click_on

# Drawing of the visual 3D frame of the Morpion
def draw_images(morpion, imageOn, screen, grids):
    grids.grid_len = 60
    # reload player1 grids into different layers
    for rect in morpion.player1_grids :
        if rect[0] in (morpion.coordonates.left_top[0] + 2 * morpion.coordonates.interval_proj[0],
                       morpion.coordonates.left_top[0] + 2 * morpion.coordonates.interval_proj[
                           0] + morpion.coordonates.interval_normal,
                       morpion.coordonates.left_top[0] + 2 * morpion.coordonates.interval_proj[
                           0] + 2 * morpion.coordonates.interval_normal) :
            grids.layer2.append((rect, 1))
        elif rect[0] in (morpion.coordonates.left_top[0] + morpion.coordonates.interval_proj[0],
                         morpion.coordonates.left_top[0] + morpion.coordonates.interval_proj[
                             0] + + morpion.coordonates.interval_normal,
                         morpion.coordonates.left_top[0] + morpion.coordonates.interval_proj[
                             0] + 2 * + morpion.coordonates.interval_normal) :
            grids.layer4.append((rect, 1))
        else :
            grids.layer6.append((rect, 1))

    # reload player2 grids into different layers
    for rect in morpion.player2_grids:
        if rect[0] in (morpion.coordonates.left_top[0] + 2 * morpion.coordonates.interval_proj[0],
                       morpion.coordonates.left_top[0] + 2 * morpion.coordonates.interval_proj[
                           0] + morpion.coordonates.interval_normal
                       , morpion.coordonates.left_top[0] + 2 * morpion.coordonates.interval_proj[
            0] + 2 * morpion.coordonates.interval_normal):
            grids.layer2.append((rect, 2))
        elif rect[0] in (morpion.coordonates.left_top[0] + morpion.coordonates.interval_proj[0],
                         morpion.coordonates.left_top[0] + morpion.coordonates.interval_proj[
                             0] + + morpion.coordonates.interval_normal,
                         morpion.coordonates.left_top[0] + morpion.coordonates.interval_proj[
                             0] + 2 * + morpion.coordonates.interval_normal):
            grids.layer4.append((rect, 2))
        else :
            grids.layer6.append((rect, 2))

    # reload click into different layers
    rect_click = pygame.Rect(morpion.click_coordonate[0] - grids.grid_len / 2,
                             morpion.click_coordonate[1] - grids.grid_len / 2, grids.grid_len, grids.grid_len)
    if imageOn:
        if morpion.click_position[1] == 0:
            grids.layer2.append(rect_click)
        elif morpion.click_position[1] == 1:
            grids.layer4.append(rect_click)
        else :
            grids.layer6.append(rect_click)

    # draws the pictures by layers
    # layer1 contains the back side [:,0,:] and a certain length of y direction
    for rect in grids.layer1:
        pygame.draw.rect(screen, (100, 0, 0), rect, 0)

    # layer2 contains chesses and click at the back side [:,0,:]
    for rect in grids.layer2:
        if rect[1] == 1:
            pygame.draw.circle(screen, (255, 0, 0), rect[0], int(grids.grid_len / 2))
        elif rect[1] == 2:
            pygame.draw.circle(screen, (0, 255, 0), rect[0], int(grids.grid_len / 2))
        else :
            pygame.draw.rect(screen, (0, 0, 255), [morpion.click_coordonate[0] - grids.grid_len / 2,
                                                   morpion.click_coordonate[1] - grids.grid_len / 2, grids.grid_len,
                                                   grids.grid_len], 0)

    # layer3 contains the middle side [:,1,:] and a certain length of y direction
    for rect in grids.layer3:
        pygame.draw.rect(screen, (100, 0, 0), rect, 0)

    # layer4 contains chesses and click at the back side [:,0,:]
    for rect in grids.layer4:
        if rect[1] == 1:
            pygame.draw.circle(screen, (255, 0, 0), rect[0], int(grids.grid_len / 2))
        elif rect[1] == 2:
            pygame.draw.circle(screen, (0, 255, 0), rect[0], int(grids.grid_len / 2))
        else:
            pygame.draw.rect(screen, (0, 0, 255), [morpion.click_coordonate[0] - grids.grid_len / 2,
                                                     morpion.click_coordonate[1] - grids.grid_len / 2, grids.grid_len,
                                                     grids.grid_len], 0)

    # layer5 contains the midium side [:,2,:]
    for rect in grids.layer5:
        pygame.draw.rect(screen, (100, 0, 0), rect, 0)

    # layer6 contains chesses and click at the back side [:,0,:]
    for rect in grids.layer6:
        if rect[1] == 1:
            pygame.draw.circle(screen, (255, 0, 0), rect[0], int(grids.grid_len / 2))
        elif rect[1] == 2:
            pygame.draw.circle(screen, (0, 255, 0), rect[0], int(grids.grid_len / 2))
        else:
            pygame.draw.rect(screen, (0, 0, 255), [morpion.click_coordonate[0] - grids.grid_len / 2,
                                                     morpion.click_coordonate[1] - grids.grid_len / 2, grids.grid_len,
                                                     grids.grid_len], 0)





# initializes the drawings of the grids based on different layers
class Grids(object):
    def __init__(self):
        self.coordonates = Coordonates()
        self.left_top = self.coordonates.left_top
        self.interval_normal = self.coordonates.interval_normal
        self.interval_proj = self.coordonates.interval_proj
        self.thickness = self.coordonates.thickness
        self.rows = []
        self.verticals = []
        self.layer1 = []
        self.layer2 = []
        self.layer3 = []
        self.layer4 = []
        self.layer5 = []
        self.layer6 = []
        for i in range(3):
            for j in range(3):
                self.rows.append(pygame.Rect(self.left_top[0] + (2 - i) * self.interval_proj[0],
                                             self.left_top[1] + i * self.interval_proj[1] + j * self.interval_normal,
                                             2 * self.interval_normal + self.thickness, self.thickness))
                self.verticals.append(
                    pygame.Rect(self.left_top[0] + (2 - i) * self.interval_proj[0] + j * self.interval_normal,
                                self.left_top[1] + i * self.interval_proj[1],
                                self.thickness, 2 * self.interval_normal + self.thickness))

                for k in range(80):
                    Rect = pygame.Rect(self.left_top[0] + 2 * self.interval_proj[0] + j * self.interval_normal - k *
                                       self.interval_proj[0] / 40,
                                       self.left_top[1] + i * self.interval_normal + k * self.interval_proj[1] / 40,
                                       self.thickness, self.thickness)
                    if k < 6:
                        self.layer1.append(Rect)
                    elif k < 46:
                        self.layer3.append(Rect)
                    else:
                        self.layer5.append(Rect)

        for k in range(3):
            self.layer1.append(self.rows[k])
            self.layer3.append(self.rows[3 + k])
            self.layer5.append(self.rows[6 + k])
            self.layer1.append(self.verticals[k])
            self.layer3.append(self.verticals[3 + k])
            self.layer5.append(self.verticals[6 + k])

