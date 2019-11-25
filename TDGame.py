from numpy import *
from TDGUI import *
from Parameters import *


class Morpion(object):
    # initialization of the chessboard
    def __init__(self):
        """
        creation of the chessboard (can be called several times if the players decide to play several times in a row)
        """
        self.creat_board()
        self.creat_players()

    def creat_board(self):
        self.coordonates = Coordonates()    # graphic parameters (lines' thickness etc.)
        self.chessboard = zeros([3, 3, 3])  # the chessboard is empty
        self.player1_grids = []             # visually, player1 doesn't have any chess on the Morpion
        self.player2_grids = []             # same for player2
        self.vacant_grids = ones([3, 3, 3], dtype=bool)     # grids which are still available. At the beginning they are all available
        self.click_position = [1, 1, 1]     # pointer's initial position on the Morpion
        self.click_coordonate = [self.coordonates.left_top[0] + self.coordonates.interval_normal + self.coordonates.interval_proj[0],
                                 self.coordonates.left_top[1] + self.coordonates.interval_normal + self.coordonates.interval_proj[1]]  # position of the pointer on the screen
        self.score_increased = 0  # variable that checks if the score of the winner has already been increased or not

    def creat_players(self):
        # initialisation of all the elements relating to the players
        self.players = [Player(1, 1), Player(2, -1)]
        self.current_player = self.players[0]
        self.winner = self.current_player
        # self.local_player = None
        self.local_player = self.players[1]

    def new_click(self):
        """
        loop to search for an available position in the 3 dimensions to makes the pointer appear on an available
        position on the board by searching for the first vacant position by index
        :return:
        """
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if self.vacant_grids[i][j][k]:
                        self.click_position = [i, j, k]  # the coordinates of the available position are transfered to the pointer
                        self.click_coordonate = [self.coordonates.left_top[0] + (2 - j) * self.coordonates.interval_proj[0] + k * self.coordonates.interval_normal,
                                                 self.coordonates.left_top[1] + i * self.coordonates.interval_normal + j * self.coordonates.interval_proj[1]]  # screen show grid change
                        return

    def set_down_chess(self):
        """
        set down chess, put a chess on the board and do relevant things like judgement of winner and put new chess on the board
        if the player presses the "space" button to set down his/her chess
        :return:
        """
        (x, y, z) = self.click_position
        if not self.vacant_grids[x][y][z]:  # checks if the chosen position is not already taken
            return
        self.chessboard[x][y][z] = self.current_player.player_flag
        self.vacant_grids[x][y][z] = False  # registers that the position on the Morpion is now taken
        self.winner = self.current_player
        self.change_player()
        if not self.isover():
            self.new_click()

    def change_player(self):
        """
        change side of players
        :return:
        """
        if self.current_player.player_flag == 1:
            self.current_player = self.players[1]
            self.player1_grids.append((self.click_coordonate[0], self.click_coordonate[1]))
        else:
            self.current_player = self.players[0]
            self.player2_grids.append((self.click_coordonate[0], self.click_coordonate[1]))

    def isover(self):
        """
        checks if the Morpion is full and there isn't any more space to play
        :return:
        """
        if self.isfull():
            return True
        elif self.iswin():
            return True
        return False

    def isfull(self):
        """
        checks if the Morpion is full and there isn't any more space to play
        :return:
        """
        if self.vacant_grids.any():
            return False
        return True

    def iswin(self):
        """
        checks if there is a winner
        :return:
        """
        layer = self.click_position[0]
        depth = self.click_position[1]
        width = self.click_position[2]

        if self.score_increased == 0:  # this checks if the score of the winner had already been increased
            if abs(self.chessboard[0][depth][width] + self.chessboard[1][depth][width] + self.chessboard[2][depth][width]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            # sum by row
            elif abs(self.chessboard[layer][depth][0] + self.chessboard[layer][depth][1] + self.chessboard[layer][depth][2]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            # sum by depth
            elif abs(self.chessboard[layer][0][width] + self.chessboard[layer][1][width] + self.chessboard[layer][2][width]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True

            # sum by horizontal diagonal on same layer (2)
            elif abs(self.chessboard[layer][0][0] + self.chessboard[layer][1][1] + self.chessboard[layer][2][2]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            elif abs(self.chessboard[layer][0][2] + self.chessboard[layer][1][1] + self.chessboard[layer][2][0]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            # sum by vertical diagonal on same column (width index)("viewed from the side") (2)
            elif abs(self.chessboard[0][0][width] + self.chessboard[1][1][width] + self.chessboard[2][2][width]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            elif abs(self.chessboard[0][2][width] + self.chessboard[1][1][width] + self.chessboard[2][0][width]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            # sum by vertical diagonal on same row (depth index) ("facing us") (2)
            elif abs(self.chessboard[0][depth][0] + self.chessboard[1][depth][1] + self.chessboard[2][depth][2]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            elif abs(self.chessboard[0][depth][2] + self.chessboard[1][depth][1] + self.chessboard[2][depth][0]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True

            # 3D cross sum (doesn't depend on the position of the new chess as it would bring complexity to the algorithm)
            elif abs(self.chessboard[0][0][0] + self.chessboard[1][1][1] + self.chessboard[2][2][2]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            elif abs(self.chessboard[0][0][2] + self.chessboard[1][1][1] + self.chessboard[2][2][0]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            elif abs(self.chessboard[0][2][0] + self.chessboard[1][1][1] + self.chessboard[2][0][2]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            elif abs(self.chessboard[0][2][2] + self.chessboard[1][1][1] + self.chessboard[2][0][0]) == 3:
                self.winner.player_score += 1
                self.score_increased += 1  # This counter tracks that the following instructions are being implemented
                return True
            return False

        else:
            return True

    def move(self, direction):
        """
        once the player has chosen in which position he/she wants to play, the relevant actions have to be taken
        :param direction:
        :return:
        """
        # sets down the chess input
        if direction == pygame.K_SPACE:
            self.set_down_chess()
        # if the direction required is immovable, cancel this instruction
        if direction == pygame.K_e:
            if self.click_position[0] == 0:
                return
            else:
                self.click_position[0] -= 1
                self.click_coordonate[1] -= self.coordonates.interval_normal
        elif direction == pygame.K_d:
            if self.click_position[0] == 2:
                return
            else:
                self.click_position[0] += 1
                self.click_coordonate[1] += self.coordonates.interval_normal
        elif direction == pygame.K_UP:
            if self.click_position[1] == 0:
                return
            else:
                self.click_position[1] -= 1
                self.click_coordonate[0] += self.coordonates.interval_proj[0]
                self.click_coordonate[1] -= self.coordonates.interval_proj[1]
        elif direction == pygame.K_DOWN:
            if self.click_position[1] == 2:
                return
            else:
                self.click_position[1] += 1
                self.click_coordonate[0] -= self.coordonates.interval_proj[0]
                self.click_coordonate[1] += self.coordonates.interval_proj[1]
        elif direction == pygame.K_LEFT:
            if self.click_position[2] == 0:
                return
            else:
                self.click_position[2] -= 1
                self.click_coordonate[0] -= self.coordonates.interval_normal
        elif direction == pygame.K_RIGHT:
            if self.click_position[2] == 2:
                return
            else:
                self.click_position[2] += 1
                self.click_coordonate[0] += self.coordonates.interval_normal


class Player(object):
    def __init__(self, player_number, player_flag):
        self.player_flag = player_flag
        self.player_number = player_number
        self.player_score = 0
