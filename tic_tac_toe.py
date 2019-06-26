# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:00:37 2019

@author: Nischal Dave
"""
from random import choice
import os

class TicTacToe:
    
    def __init__(self):
        self._game_on = True
        self._players = ['X', 'O']
        self._a, self._b = [str(i) for i in range(1, 10)], [' ' for i in range(9)]        
    
    def _draw_board(self):
        print('Available   TIC-TAC-TOE\n'+
           '  moves\n\n  '+
              self._a[6]+'|'+self._a[7]+'|'+self._a[8]+'        '+self._b[6]+'|'+self._b[7]+'|'+self._b[8]+'\n  '+
              '-----        -----\n  '+
              self._a[3]+'|'+self._a[4]+'|'+self._a[5]+'        '+self._b[3]+'|'+self._b[4]+'|'+self._b[5]+'\n  '+
              '-----        -----\n  '+
              self._a[0]+'|'+self._a[1]+'|'+self._a[2]+'        '+self._b[0]+'|'+self._b[1]+'|'+self._b[2]+'\n')
        
    def clear(self): os.system( 'cls' )
    
    def _space_check(self, position): return self._b[position-1] == ' '
    
    def _player_won(self, mark):
        return any(self._b[a] ==  self._b[b] ==  self._b[c] == mark for a, b, c in ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 4, 8)))
    
    def _make_changes(self, position, toggle):
        self._a[position-1] = ' '
        self._b[position-1] = self._players[toggle]
        
    def _move(self, toggle):
        position = 0
        while 1 > position or position > 9 or not self._space_check(position):
            try: position = int(input("Player {} make a move: ".format(toggle + 1)))
            except: print("Please try again!")
        return position
    
        
    def _random_choice(self): return choice((0, 1))
    
    def _board_is_full(self): return all(i == ' ' for i in self._a)
    
    def _replay(self): return input("Do you want to play again: y or n? ") == 'y'
    
    def execute(self):
        while True:
            print("\nWELCOME TO TIC-TAC-TOE!\n\nPlayer 1 is X\nPlayer 2 is O\n\n")
            toggle = self._random_choice()
            print("For this round Player {} will go first!\n".format(toggle + 1))        
            while self._game_on:
                self._draw_board()
                position = self._move(toggle)
                self._make_changes(position, toggle)
                player_won = self._player_won(self._players[toggle])
                if player_won or self._board_is_full(): 
                    self._draw_board()
                    if player_won: print("Congratulations! Player {} wins!".format(toggle + 1))
                    else: print("Game is a draw!")
                    self._game_on = False
                else:
                    toggle = 1 - toggle
                    self.clear()
            if not self._replay(): break
            self.__init__()
            
if __name__ == "__main__":
    TicTacToe().execute()