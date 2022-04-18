### Python Tsoro Game Tree
### Includes DFS, BFS and Djikstra Algorithms 
### Written by Tanaka B. Khondowe
import random as rand

board = [
    [0, 0, 0, 0, 2, 2, 2, 2],
    [0, 0, 0, 0, 2, 2, 2, 2]
]

boardA = len(board[0])
boardB = len(board[1])
hand1 = board[0][rand.randrange(1,7)]
hand2 = board[1][rand.randrange(1,7)] 

print(hand1)
print(hand2)

print("+++++++++++++++++++++++")

i = 0
while i < boardA:
    print(board[0][i])
    i+=1