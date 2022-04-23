###### Python Tsoro Game Tree ######
###### Includes DFS, BFS and Djikstra Algorithms ######  
###### Written by Tanaka Khondowe ######

###### the graph structure ######
'''
Each node is a play where the branches represents all holes except the destination hole.


'''

import pygraphviz
import random as rand

class Tsoro:
    def __init__(self, board_size, stones_per_hole) -> None:
        self.board_size = board_size
        self.board = [0]*board_size
        self.stones_per_hole = stones_per_hole
        self.curr_hole = 0
        self.dest_hole = 0
        self.hand = 0
        self.count = 0

    def init_board(self) -> list:
        occupied_holes = int(self.board_size/2)
        while occupied_holes < self.board_size:
            self.board[occupied_holes] = 2
            occupied_holes+=1
        return self.board

    def print_graph(self):
        pass

    def choose_hand(self) -> int:
        #random strategy
        self.curr_hole = rand.randrange(1, self.board_size-1)
        if (self.board[self.curr_hole] == 0):
            while (self.board[self.curr_hole] == 0):
                self.curr_hole = rand.randrange(1, self.board_size)
        self.hand = self.board[self.curr_hole]
        return self.hand

    def loop_back(self):
        if (self.curr_hole == self.board_size):
            self.curr_hole = self.dest_hole
    
    def play_hand(self):
        while (self.hand > 0):
            self.curr_hole+=1
            self.loop_back()
            self.board[self.curr_hole] += 1
            self.hand-=1

    def carry_over(self):
        if (self.board[self.curr_hole] > 1 & self.curr_hole != self.dest_hole):
            self.hand = self.board[self.curr_hole]
            print("Playing again...")
            print("New hand", self.hand)
            print("Current hole", self.curr_hole)
            self.board[self.curr_hole] = 0 
            self.play_hand()
            print("Current hole", self.curr_hole)
    
    def play_round(self):
        print("ROUND: ", self.count)
        self.count+=1
        self.hand = self.choose_hand()
        print("Current hole", self.curr_hole)
        print("Hand = ", self.hand)
        self.board[self.curr_hole] = 0
        while (self.hand > 0):
            self.play_hand()
        print("Current hole", self.curr_hole)
        self.carry_over()
        return self.board

tsoro = Tsoro(8, 2)
board = tsoro.init_board()
print(len(board))
while (board[0] < len(board)):
    print(tsoro.play_round())

