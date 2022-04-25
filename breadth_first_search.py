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

def print_maze(maze, stdscr, path=[]):  # "path" is that ideal shortest path
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2) # we'll make the path red.

    for i, row in enumerate(maze):  # need to iterate through the maze. "Row" for each individual row, with "i" for which row within the 2D array 
        for j, value in enumerate:
            pass

def main(stdscr):  #this stands for 'standard output screen'
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # to implement a color.
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)


    # stdscr.clear()
    # stdscr.addstr(5,5,"hello world!", blue_and_black) # to pass the position and the text to etner 
    # stdscr.refresh() # to see what we've written
    # stdscr.getch() # "get character" from the user input.

wrapper(main) # initializes the curses module and calls main(). This enables us to control the output.
