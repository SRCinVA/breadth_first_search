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
        for j, value in enumerate(row):  #'value' is whatever symbol is in the column.
            stdscr.addstr(i,j*2,value, BLUE) # you need these three pieces of info to draw on to the screen.
                                        # the multiplication spreads the entire stucture out.

def find_start(maze, start):  # you'll already have dropped that start into the maze manually; this is just to find it.
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j  # tells you where the starting symbol was found.

    return None # if the start is not available.

def find_path(maze, stdscr):
    start = "0"
    end = "X"
    start_pos = find_start(maze, start)

    # now let's set up the queue for how we will keep track of these
    q = queue.Queue() # we want to process the first node in the order it was received (if it were the most recent, you would never get anywhere.)
    q.put((start_pos, [start_pos]))  # put() populates the queue. You pass in the starting position but also a list that concatenates each node that gets added on (I think)

    visited = set() # this what you've already visited (more explanation would have been helpful here.)

    while not q.empty():
        current_pos, path = q.get() # this pulls in the starting point and the path (but why equate current_pos and start_pos?)

def main(stdscr):  #this stands for 'standard output screen'
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # to implement a color.
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh() # to see what we've written
    stdscr.getch() # "get character" from the user input.

wrapper(main) # initializes the curses module and calls main(). This enables us to control the output.
