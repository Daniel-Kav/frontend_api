from django.shortcuts import render

# Create your views here.


board  = [""] * 9

def check_winner(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal wins
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical wins
        [0, 4, 8], [2, 4, 6],             # Diagonal wins
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] and board[condition[2]] and board[condition[0]] != [""]:
            return board[condition[0]]
        return None
