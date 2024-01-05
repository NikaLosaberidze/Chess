from board import Board
from pieces import *

class Chess:
    def __init__(self):
        self.board = Board()
        self.currentPlayer = "White"

    def swapPlayers(self):
        if self.currentPlayer == "White":
            self.currentPlayer = "Black"
        else:
            self.currentPlayer = "White"
    
    def isStringValidMove(self, moveStr):
        if len(moveStr) != 5:
            return False
        lst = [*moveStr]
        if lst[0] not in validLettersNumbers or (ord(lst[1])-48) not in validLettersNumbers or lst[3] not in validLettersNumbers or (ord(lst[4])-48) not in validLettersNumbers:
            return False
        if lst[2] != " ":
            return False
        return True
            

    def play(self):
        while True:
            self.board.displayBoard()
            if self.currentPlayer == "White":
                print("Its White's turn")
            else:
                print("Its Black's turn")
            
            while True:
                inp = input()
                if inp == "EXIT":
                    return
                if not self.isStringValidMove(inp):
                    continue
                start = inp.split(" ")[0]
                end = inp.split(" ")[1]
                if isinstance(self.board.board[ord(end[0])-65][int(end[1])-1], Piece):
                    if self.board.board[ord(end[0])-65][int(end[1])-1].getName() == "King":
                        if not self.board.makeMove(start,end,self.currentPlayer):
                            continue
                        else:
                            print(self.currentPlayer +" IS WINNER!")
                            return
                    
                if not self.board.makeMove(start,end,self.currentPlayer):
                    continue
                for i in range(8):
                    if isinstance(self.board.board[0][i], Pawn):
                        if self.board.board[0][i]._color == "White":
                            while True:
                                print("To which piece do you want to promote your pawn. Queen,Rook,Bishop or Knight")
                                answer = input()
                                if answer not in whiteIcons:
                                    continue
                                else:
                                    if answer == "Queen":
                                        self.board.board[0][i] = Queen("White",self.board,("A",i+1))
                                    elif answer == "Rook":
                                        self.board.board[0][i] = Rook("White",self.board,("A",i+1))
                                    elif answer == "Bishop":
                                        self.board.board[0][i] = Bishop("White",self.board,("A",i+1))
                                    else:
                                        self.board.board[0][i] = Knight("White",self.board,("A",i+1))
                                    break
                                
                        else:
                            continue
                    elif isinstance(self.board.board[7][i], Pawn):
                        if self.board.board[7][i]._color == "Black":
                            while True:
                                print("To which piece do you want to promote your pawn. Queen,Rook,Bishop or Knight")
                                answer = input()
                                if answer not in blackIcons:
                                    continue
                                else:
                                    if answer == "Queen":
                                        self.board.board[7][i] = Queen("Black",self.board,("H",i+1))
                                    elif answer == "Rook":
                                        self.board.board[7][i] = Rook("Black",self.board,("H",i+1))
                                    elif answer == "Bishop":
                                        self.board.board[7][i] = Bishop("Black",self.board,("H",i+1))
                                    else:
                                        self.board.board[7][i] = Knight("Black",self.board,("H",i+1))
                                    break
                
                    
                    
                self.swapPlayers()
                break
                
            

if __name__ == "__main__":
    game = Chess()
    game.play() 