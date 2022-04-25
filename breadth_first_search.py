import curses  #allows for greater control of the terminal 
from curses import wrapper
import queue
import time

maze = [

    ["#", "#", "#", "#", "#", "0", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#"]
]

def main(stdscr):  #this stands for 'standard output screen'
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # to implement a color.
    blue_and_black = curses.color_pair(1) # the color pair you created.


    stdscr.clear()
    stdscr.addstr(0,0,"hello world!", blue_and_black) # to pass the position and the text to etner 
    stdscr.refresh() # to see what we've written
    stdscr.getch() # "get character" from the user input.

wrapper(main) # initializes the curses module and calls main(). This enables us to control the output.