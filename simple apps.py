print("X,O GAME:");
print("game is missing the draw games.")

class GAME:
    number_of_players = 2;
    row_number1 = 0;
    row_number2 = 0;
    str_player1Symbol = "/";
    str_player2Symbol = "+";
    element_number1 = 0;
    element_number2 = 0;
    string_board = "";
    rowNumber1 = [-1 , -1 , -1];
    rowNumber2 = [-1 , -1 , -1];
    rowNumber3 = [-1 , -1 , -1];
    def __init__(self):
        self.string_board = """***
***
***""";
        
    def checkWinner(self):
        value_to_be_returned = 0;
        if(self.rowNumber1[0] == 0 and self.rowNumber2[0] == 0 and self.rowNumber3[0] == 0):
            print("player 1 winsss at cond 1");
            value_to_be_returned = 1;
        elif (self.rowNumber1[0] == 0 and self.rowNumber1[1] == 0 and self.rowNumber1[2] == 0):
            print("player 1 winsss at cond 2");
            value_to_be_returned = 1;
        elif (self.rowNumber2[0] == 0 and self.rowNumber2[1] == 0 and self.rowNumber2[2] == 0):
            print("player 1 winsss at cond 3");
            value_to_be_returned = 1;
        elif (self.rowNumber3[0] == 0 and self.rowNumber3[1] == 0 and self.rowNumber3[2] == 0):
            print("player 1 winsss at cond 4");
            value_to_be_returned = 1;
        elif(self.rowNumber1[1] == 0 and self.rowNumber2[1] == 0 and self.rowNumber3[1] == 0):
            print("player 1 winsss at cond 5");
            value_to_be_returned = 1;
        elif(self.rowNumber1[2] == 0 and self.rowNumber2[2] == 0 and self.rowNumber3[2] == 0):
            print("player 1 winsss at cond 6");
            value_to_be_returned = 1;
        elif(self.rowNumber1[0] == 0 and self.rowNumber2[1] == 0 and self.rowNumber3[2] == 0):
            print("player 1 winsss at cond 7");
            value_to_be_returned = 1;
        elif(self.rowNumber1[2] == 0 and self.rowNumber2[1] == 0 and self.rowNumber3[0] == 0):
            print("player 1 winsss at cond 8");
            value_to_be_returned = 1;
        if value_to_be_returned == 1:
            return value_to_be_returned;

        if(self.rowNumber1[0] == 1 and self.rowNumber2[0] == 1 and self.rowNumber3[0] == 1):
            print("player 2 winsss at cond 1");
            value_to_be_returned = 2;
        elif (self.rowNumber1[0] == 1 and self.rowNumber1[1] == 1 and self.rowNumber1[2] == 1):
            print("player 2 winsss at cond 2");
            value_to_be_returned = 2;
        elif (self.rowNumber2[0] == 1 and self.rowNumber2[1] == 1 and self.rowNumber2[2] == 1):
            print("player 2 winsss at cond 3");
            value_to_be_returned = 2;
        elif (self.rowNumber3[0] == 1 and self.rowNumber3[1] == 1 and self.rowNumber3[2] == 1):
            print("player 2 winsss at cond 4");
            value_to_be_returned = 2;
        elif(self.rowNumber1[1] == 1 and self.rowNumber2[1] == 1 and self.rowNumber3[1] == 1):
            print("player 2 winsss at cond 5");
            value_to_be_returned = 2;
        elif(self.rowNumber1[2] == 1 and self.rowNumber2[2] == 1 and self.rowNumber3[2] == 1):
            print("player 2 winsss at cond 6");
            value_to_be_returned = 2;
        elif(self.rowNumber1[0] == 1 and self.rowNumber2[1] == 1 and self.rowNumber3[2] == 1):
            print("player 2 winsss at cond 7");
            value_to_be_returned = 2;
        elif(self.rowNumber1[2] == 1 and self.rowNumber2[1] == 1 and self.rowNumber3[0] == 1):
            print("player 2 winsss at cond 8");
            value_to_be_returned = 2;
        return value_to_be_returned;
    def updateBoard(self):
        string_tool = "";
        if self.row_number1 == 1:
            if self.element_number1 == 1:
                string_tool = self.str_player1Symbol+self.string_board[1:];
            elif self.element_number1 == 2:
                string_tool = self.string_board[0]+self.str_player1Symbol+self.string_board[2:];
            elif self.element_number1 == 3:
                string_tool = self.string_board[0:2]+self.str_player1Symbol+self.string_board[3:];
        elif self.row_number1 == 2:
            if self.element_number1 == 1:
                string_tool = self.string_board[0:4]+self.str_player1Symbol+self.string_board[5:];
            elif self.element_number1 == 2:
                string_tool = self.string_board[0:5]+self.str_player1Symbol+self.string_board[6:];
            elif self.element_number1 == 3:
                string_tool = self.string_board[0:6]+self.str_player1Symbol+self.string_board[7:];
        elif self.row_number1 == 3:
            if self.element_number1 == 1:
                string_tool = self.string_board[0:8]+self.str_player1Symbol+self.string_board[9:];
            elif self.element_number1 == 2:
                string_tool = self.string_board[0:9]+self.str_player1Symbol+self.string_board[10:];
            elif self.element_number1 == 3:
                string_tool = self.string_board[0:10]+self.str_player1Symbol;
        self.string_board = string_tool;
        if self.row_number2 == 1:
            if self.element_number2 == 1:
                string_tool = self.str_player2Symbol+self.string_board[1:];
            elif self.element_number2 == 2:
                string_tool = self.string_board[0]+self.str_player2Symbol+self.string_board[2:];
            elif self.element_number2 == 3:
                string_tool = self.string_board[0:2]+self.str_player2Symbol+self.string_board[3:];
        elif self.row_number2 == 2:
            if self.element_number2 == 1:
                string_tool = self.string_board[0:4]+self.str_player2Symbol+self.string_board[5:];
            elif self.element_number2 == 2:
                string_tool = self.string_board[0:5]+self.str_player2Symbol+self.string_board[6:];
            elif self.element_number2 == 3:
                string_tool = self.string_board[0:6]+self.str_player2Symbol+self.string_board[7:];
        elif self.row_number2 == 3:
            if self.element_number2 == 1:
                string_tool = self.string_board[0:8]+self.str_player2Symbol+self.string_board[9:];
            elif self.element_number2 == 2:
                string_tool = self.string_board[0:9]+self.str_player2Symbol+self.string_board[10:];
            elif self.element_number2 == 3:
                string_tool = self.string_board[0:10]+self.str_player2Symbol;
        self.string_board = string_tool;
    def PrintBoard(self):
        print(self.string_board);
    def takeInputs(self):
        right_input = False;
        while right_input == False:
            string_input_player1 = input("enter row number you want to play 1 at : ");
            self.row_number1 = int(string_input_player1);
            string_input_player1 = input("enter element you want to play 1 at : ");
            self.element_number1 = int(string_input_player1);
            if self.row_number1 == 1 and self.rowNumber1[self.element_number1-1] == -1:
                self.rowNumber1[self.element_number1-1] = 0;
                right_input = True;
            elif self.row_number1 == 2 and self.rowNumber2[self.element_number1-1] == -1:
                self.rowNumber2[self.element_number1-1] = 0;
                right_input = True;
            elif self.row_number1 == 3 and self.rowNumber3[self.element_number1-1] == -1:
                self.rowNumber3[self.element_number1-1] = 0;
                right_input = True;
            else:
                right_input = False;
        right_input = False;
        while right_input == False:
            string_input_player2 = input("enter row number you want to play 2 at : ");
            self.row_number2 = int(string_input_player2);
            string_input_player2 = input("enter element you want to play 2 at : ");
            self.element_number2 = int(string_input_player2);
            if self.row_number2 == 1 and self.rowNumber1[self.element_number2-1] == -1:
                self.rowNumber1[self.element_number2-1] = 1;
                right_input = True;
            elif self.row_number2 == 2 and self.rowNumber2[self.element_number2-1] == -1:
                self.rowNumber2[self.element_number2-1] = 1;
                right_input = True;
            elif self.row_number2 == 3 and self.rowNumber3[self.element_number2-1] == -1:
                self.rowNumber3[self.element_number2-1] = 1;
                right_input = True;
            else:
                right_input = False;
    def Main_Game_loop(self):
        winner = 0;
        print(self.string_board);
        while winner == 0:
            self.takeInputs();
            self.updateBoard();
            winner = self.checkWinner();
            if(winner == 1):
                print("player 1 winnes");
                
            elif winner == 2:
                print("player 2 winnes");
            string = input("do you want to print the board : ");
            intger = int(string);
            if(intger == 1):
                self.PrintBoard();        
print("GAME MISSING THE DRAWN MODE");
obj = GAME();
obj.Main_Game_loop();


    
