from pieces import *
import sys

class Board:
    board = [[0,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None]]
    def __init__(self):
        self.placePieces()
        

    def placePieces(self):
        self.board[0][0] = Rook("Black",self.board,("A",1))
        self.board[0][7] = Rook("Black",self.board,("A",8))
        self.board[7][0] = Rook("White",self.board,("H",1))
        self.board[7][7] = Rook("White",self.board,("H",8))
        
        self.board[0][1] = Knight("Black",self.board,("A",2))
        self.board[0][6] = Knight("Black",self.board,("A",7))
        self.board[7][1] = Knight("White",self.board,("H",2))
        self.board[7][6] = Knight("White",self.board,("H",7))
        
        self.board[0][2] = Bishop("Black",self.board,("A",3))
        self.board[0][5] = Bishop("Black",self.board,("A",6))
        self.board[7][2] = Bishop("White",self.board,("H",3))
        self.board[7][5] = Bishop("White",self.board,("H",6))
        
        self.board[0][3] = Queen("Black",self.board,("A",4))
        self.board[7][3] = Queen("White",self.board,("H",4))
        
        self.board[0][4] = King("Black",self.board,("A",5))
        self.board[7][4] = King("White",self.board,("H",5))
        
        for i in range(8):
            self.board[1][i] = Pawn("Black",self.board,("B",i+1))
            self.board[6][i] = Pawn("White",self.board,("G",i+1))
                
        

    def setPiece(self, position, piece):
        self.board[ord(position[0])-65][int(position[1])-1] = piece 

    def getPiece(self, position):
        if isinstance(self.board[ord(position[0])-65][int(position[1])-1], Piece):
            return self.board[ord(position[0])-65][int(position[1])-1]
        return None

    def makeMove(self, startPosition, endPosition, player):
        if isinstance(self.board[ord(startPosition[0])-65][int(startPosition[1])-1], Piece):
            if self.board[ord(startPosition[0])-65][int(startPosition[1])-1]._color == player:
                if self.board[ord(startPosition[0])-65][int(startPosition[1])-1].checkMove(endPosition):
                    self.board[ord(endPosition[0])-65][int(endPosition[1])-1] = self.board[ord(startPosition[0])-65][int(startPosition[1])-1]
                    
                    self.board[ord(startPosition[0])-65][int(startPosition[1])-1] = None
                    self.board[ord(endPosition[0])-65][int(endPosition[1])-1]._position = (endPosition[0],int(endPosition[1]))
                    return True
                
                print("You can't go there")
                return False
            print("That is not your piece")
            return False                    
        print("There is no piece on that position")
        return False

    def displayBoard(self):
        print("    (1) (2) (3) (4) (5) (6) (7) (8)")
        sys.stdout.write("(A)")
        for i in range(8):
            if self.board[0][i] != None:
                if self.board[0][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[0][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[0][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
            
        print("")
        sys.stdout.write("(B)")
        for i in range(8):
            if self.board[1][i] != None:
                if self.board[1][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[1][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[1][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
        print("")
        sys.stdout.write("(C)")
        for i in range(8):
            if self.board[2][i] != None:
                if self.board[2][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[2][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[2][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
        print("")
        sys.stdout.write("(D)")
        for i in range(8):
            if self.board[3][i] != None:
                if self.board[3][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[3][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[3][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
        print("")
        sys.stdout.write("(E)")
        for i in range(8):
            if self.board[4][i] != None:
                if self.board[4][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[4][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[4][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
        print("")
        sys.stdout.write("(F)")
        for i in range(8):
            if self.board[5][i] != None:
                if self.board[5][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[5][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[5][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
        print("")
        sys.stdout.write("(G)")
        for i in range(8):
            if self.board[6][i] != None:
                if self.board[6][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[6][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[6][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
        print("")
        sys.stdout.write("(H)")
        for i in range(8):
            if self.board[7][i] != None:
                if self.board[7][i]._color == "White":
                    sys.stdout.write("[" + whiteIcons[self.board[7][i].getName()] + " ]")
                else:
                    sys.stdout.write("[" + blackIcons[self.board[7][i].getName()] + " ]")
            else:
                sys.stdout.write("[  ]")
        print("")