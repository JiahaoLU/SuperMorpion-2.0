from collections import deque
# the buffer stockage of instructions received from one client and sent to another
Client_ins_rece = deque()
Client_ins_send = deque()

# the flag showing if the player is the current one or not
Client_player = False
