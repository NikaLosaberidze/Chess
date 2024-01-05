blackIcons = {"Pawn" : "♙", "Rook" : "♖", "Knight" : "♘", "Bishop" : "♗", "King" : "♔", "Queen" : "♕" }
whiteIcons = {"Pawn" : "♟", "Rook" : "♜", "Knight" : "♞", "Bishop" : "♝", "King" : "♚", "Queen" : "♛" }



validLettersNumbers = ['A','B','C','D','E','F','G','H',1,2,3,4,5,6,7,8]

class Piece:

    def __init__(self, color, board, position):
        if color != "White" and color != "Black":
            raise ValueError
        self._color = color 
        self.__board = board
        self._position = position

    def checkMove(self, dest):
        return False

    def move(self, dest):
        return False
        
    def getName(self):
        return self.__class__.__name__

    def getIcon(self):
        return None

    @property
    def color(self):
        return self._color
        
    def board(self):
        return self.__board
    
    @property
    def position(self):
        return self.position
    
    @position.setter
    def position(self, new_pos):
        if new_pos[0] not in validLettersNumbers:   
            return None
        self.position = new_pos


class Knight(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.__board = board
        self._color = color
        self._position = position
        

    def checkMove(self, dest):
        curr = self._position
        if curr[0] == dest[0] and int(curr[1]) == int(dest[1]):
            return False
        if dest[0] not in validLettersNumbers or int(dest[1]) not in validLettersNumbers:
            return False
        
        if abs(ord(curr[0])-ord(dest[0])) == 2 and abs(int(curr[1]) - int(dest[1])) == 1:
            if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                    return False
                return True
            return True
        
        elif abs(ord(curr[0])-ord(dest[0])) == 1 and abs(int(curr[1]) - int(dest[1])) == 2:
            if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                    return False
                return True
            return True
        
        return False
        

    def move(self, dest):
        if self.checkMove(dest):
            self._position = dest
            self.__board[ord(dest[0])-65][int(dest[1])-1] = self
            return True
        else:
            return False

    def getName(self):
        return "Knight"
    
    def getIcon(self):
        if self._color == "White":
            return whiteIcons["Knight"]
        else:
            return blackIcons["Knight"]

class Rook(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.__board = board
        self._color = color
        self._position = position
        
    def checkMove(self, dest):
        curr = self._position
        if curr[0] == dest[0] and int(curr[1]) == int(dest[1]):
            return False
        if dest[0] not in validLettersNumbers or int(dest[1]) not in validLettersNumbers:
            return False
        
        if curr[0] == dest[0] or int(curr[1]) == int(dest[1]): # rook movement -> either char is same or number
            if curr[0] == dest[0]:
                for i in range(int(curr[1]),int(dest[1])-1):
                    if isinstance(self.__board[ord(dest[0])-65][i], Piece): # something is in the way 
                        return False
                for i in range(int(dest[1]), int(curr[1])-1): # for - vice verca, in case it goes backwards
                    if isinstance(self.__board[ord(dest[0])-65][i], Piece):
                        return False
                    
                if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece): # if programme made to this, it means that we are checking destination square 
                    if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                        return False
                    else:
                        return True
                else:
                    return True
                     
            else:  # case when number is the same
                for i in range(ord(curr[0])-65+1,ord(dest[0])-65):   
                    if isinstance(self.__board[i][int(dest[1])-1], Piece): 
                        return False
                for i in range(ord(dest[0])-65+1, ord(curr[0])-65): # for - vice verca, in case it goes backwards
                    if isinstance(self.__board[i][int(dest[1])-1], Piece):
                        return False
                    
                if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                     if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                         return False
                     else:
                         return True
                else:
                    return True
            
        return False
        
    def move(self, dest):
        if self.checkMove(dest):
            self._position = dest
            self.__board[ord(dest[0])-65][int(dest[1])-1] = self
            return True
        else:
            return False

    def getName(self):
        return "Rook"
    
    def getIcon(self):
        if self._color == "White":
            return whiteIcons["Rook"]
        else:
            return blackIcons["Rook"]
        
class Bishop(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.__board = board
        self._color = color
        self._position = position

    def checkMove(self, dest):
        curr = self._position
        if curr[0] == dest[0] and int(curr[1]) == int(dest[1]):
            return False
        if dest[0] not in validLettersNumbers or int(dest[1]) not in validLettersNumbers:
            return False
        
        if abs(ord(dest[0])-ord(curr[0])) == abs(int(dest[1])-int(curr[1])):
            if ord(dest[0])-ord(curr[0]) > 0:
                for i in range(0,int(dest[1])-int(curr[1])-1):
                    if isinstance(self.__board[ord(curr[0])-65+i+1][int(curr[1])+i], Piece):
                        return False
                    
                for i in range(0,int(curr[1])-int(dest[1])-1):
                    if isinstance(self.__board[ord(curr[0])-65+i+1][int(curr[1])-i-2], Piece):
                        return False
                    
                if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                    if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                        return False
                    return True
                else:
                    return True
                          
            else:
                for i in range(0,int(dest[1])-int(curr[1])-1):
                    if isinstance(self.__board[ord(curr[0])-65-i-1][int(curr[1])+i], Piece):
                        return False
                    
                for i in range(0,int(curr[1])-int(dest[1])-1):
                    if isinstance(self.__board[ord(curr[0])-65-i-1][int(curr[1])-i-2], Piece): #curr[0] - 65 - i + int(dest[1])
                        return False
                    
                if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                    if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                        return False
                    return True
                else:
                    return True
        return False
                
    
    def move(self, dest):
        if self.checkMove(dest):
            self._position = dest
            self.__board[ord(dest[0])-65][int(dest[1])-1] = self
            return True
        else:
            return False

    def getName(self):
        return "Bishop"
    
    def getIcon(self):
        if self._color == "White":
            return whiteIcons["Bishop"]
        else:
            return blackIcons["Bishop"]
        
class Queen(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.__board = board
        self._color = color
        self._position = position

    def checkMove(self, dest):
        bishop = Bishop(self._color,self.__board,self._position)
        rook = Rook(self._color,self.__board,self._position)
        
        return bishop.checkMove(dest) or rook.checkMove(dest)
    
    def move(self, dest):
        if self.checkMove(dest):
            self._position = dest
            self.__board[ord(dest[0])-65][int(dest[1])-1] = self
            return True 
        else:
            return False

    def getName(self):
        return "Queen"
    
    def getIcon(self):
        if self._color == "White":
            return whiteIcons["Queen"]
        else:
            return blackIcons["Queen"]

class King(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.__board = board
        self._color = color
        self._position = position

    def checkMove(self, dest):
        curr = self._position
        if dest[0] not in validLettersNumbers or int(dest[1]) not in validLettersNumbers:
            return False
        if curr[0] == dest[0] and int(curr[1]) == int(dest[1]):
            return False
        
        if (abs(ord(dest[0])-ord(curr[0]) == 1) or dest[0] == curr[0]) and (abs(int(dest[1])-int(curr[1])) == 1 or int(dest[1]) == int(curr[1])):
            if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                    return False
                return True
            return True
        
        return False
    
    def move(self, dest):
        if self.checkMove(dest):
            self._position = dest
            self.__board[ord(dest[0])-65][int(dest[1])-1] = self 
            return True       
        else:
            return False
    
    def getName(self):
        return "King"
    
    def getIcon(self):
        if self._color == "White":
            return whiteIcons["King"]
        else:
            return blackIcons["King"]

class Pawn(Piece):
    def __init__(self, color, board, position):
        super().__init__(color, board, position)
        self.__board = board
        self._color = color
        self._position = position
        
    def checkMove(self, dest):
        curr = self._position
        if curr[0] == dest[0] and int(curr[1]) == int(dest[1]):
            return False
        if dest[0] not in validLettersNumbers or int(dest[1]) not in validLettersNumbers:
            return False
        
        if abs(ord(dest[0])-ord(curr[0])) == 1 and abs(int(dest[1]) - int(curr[1])) == 1: # killing with pawn
            if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                if self.__board[ord(dest[0])-65][int(dest[1])-1]._color == self._color:
                    return False
                else:
                    return True
            return False
        
        if curr[0] == 'G' or curr[0] == 'B': # If pawn hasn't moved
            if (abs(ord(dest[0])-ord(curr[0])) == 1 or abs(ord(dest[0]) - ord(curr[0])) == 2) and int(curr[1]) == int(dest[1]):
                if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                    return False
                return True
            return False
        if abs(ord(dest[0])-ord(curr[0])) == 1 and int(curr[1]) == int(dest[1]):
            if isinstance(self.__board[ord(dest[0])-65][int(dest[1])-1], Piece):
                return False
            return True
                    
    def move(self, dest):
        if self.checkMove(dest):
            self._position = dest
            self.__board[ord(dest[0])-65][int(dest[1])-1] = self 
            
            return True
        else:
            return False

    def getName(self):
        return "Pawn"
    
    def getIcon(self):
        if self._color == "White":
            return whiteIcons["Pawn"]
        else:
            return blackIcons["Pawn"]