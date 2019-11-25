Rules of game:
1.this game is constructed in 3D chessboard of 3*3*3, if three pieces of the same color line up, one round will
    be over, and the winner can get 1 point.
2. upstairs: 'e'
   downstairs:'d'
   left on the same stage:'←'
   right on the same stage:'→'
   up on the same stage:'↑'
   down on the same stage:'↓'
   place the piece on board:'space'
   a new round:'r'
   quit the game:'Esc'
3. 10 seconds limit a turn. if time is up, the piece will be forcely put down on the chessboard at the current position.
    (if the current place is occupied, a new vacant place will be found automatically to set down your piece forcely);


the morpion game should be launched on two computers by following steps:
1. run 'pip install pygame' in Terminal of python on both computers;
2. on computer1 launch "Server_launch.py", note down the IP adress from the window and click 'OK', wait until on
    computer1 the game window pops up;
3. launch "Client_launch.py" on computer 2;
4. on computer2 type in username and the aiming IP adress gotten from computer1, click 'OK' to enter the game.
    If the game can't start, please return back to step 3 and check the IP that you type in is correct;
5. play game on two computers under instructions on the bottom-right corner.
6. when one round is over, it's the one losing the game who types 'r' to start a new game;
7. type 'Esc' to quit the game;
