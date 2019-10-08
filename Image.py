import pygame
from TDGame import *
from Parameters import *


# frame counter and click shining switch
def image_count(frame_count, click_on):
    frame_count += 1
    if frame_count % 5 == 0:  # every 30 frames
        if click_on:  # if it's on
            click_on = False  # turn it off
        elif not click_on:  # if it's off
            click_on = True  # turn it on
    return frame_count, click_on



# Drawing the visuals
def draw_visuals(morpion, imageOn, screen, grids):
    draw_images(morpion, imageOn, screen, grids)
    draw_captions(morpion, imageOn, screen, grids)

# drawing the informations about the players
def draw_captions(morpion, imageOn, screen, grids):
    show_text(screen, (730, 300), 'Player 1 score : {}'.format(morpion.players[0].player_score),
              (0, 0, 18), False, 30)
    show_text(screen, (730, 350), 'Player 2 score : {}'.format(morpion.players[1].player_score),
              (0, 0, 18), False, 30)
    # parameters : (screen, pos, text, color, font_bold=False, font_size=60, font_italic=False)


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
    if imageOn == True:
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


# General function for writing messages on the screen
def show_text(screen, pos, text, color, font_bold=False, font_size=60, font_italic=False):
    # words type and size
    cur_font = pygame.font.SysFont("Times New Roman", font_size)
    # overstriking
    cur_font.set_bold(font_bold)
    # declined
    cur_font.set_italic(font_italic)
    # words content
    text_fmt = cur_font.render(text, 1, color)
    # draw words
    screen.blit(text_fmt, pos)


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

