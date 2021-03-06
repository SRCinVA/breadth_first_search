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
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze, stdscr, path=[]):  # "path" is that ideal shortest path
    BLUE = curses.color_pair(1)
    RED = curses.color_pair(2) # we'll make the path red.

    for i, row in enumerate(maze):  # need to iterate through the maze. "Row" for each individual row, with "i" for which row within the 2D array 
        for j, value in enumerate(row):  #'value' is whatever symbol is in the column.
            if (i,j) in path: # if your current item is in the path ...
                stdscr.addstr(i,j*2,"X", RED) # you need these three pieces of info to draw red X on to the screen.
                                        # the multiplication spreads the entire stucture out.
            else:
                stdscr.addstr(i, j*2, value, BLUE)  # thsi will just draw an empty string


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
        row, col = current_pos # this will break down the current position (but how ...)

        # this will draw the maze each time we do a while loop
        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2) # to slow it down so that we can see it in action.
        stdscr.refresh()  # to see what we've written



        # then, let's process all of this node's neighbors:
        if maze[row][col] == end:  # meaning, if the position is equal to an 'X'
            return path # ... because we've succeeded and are finished

        neighbors = find_neighbors(maze, row, col)  # to make sure hte spot is open
        for neighbor in neighbors:
            if neighbor in visited:
                continue # ... so that we don't process it; go to the next one.

            r, c = neighbor  # so we don't confuse row and column as above. 
            if maze[r][c] == "#":  # the character we are using for our borders; I believe "r" and "c" are the components of the tuple.
                continue # don't want to process this one, either so you go to the next one.

            # in every other case, we DO want to process the node, like this:
            new_path = path + [neighbor] # you're just adding the current node to the existing list (you can add lists).
            q.put((neighbor, new_path)) # add both to the queue. 
            visited.add(neighbor) # to make sure we don't process this again.


def find_neighbors(maze, row, col): # ... but we need to make sure that they are legitimate moves
    neighbors = []

# remember: this isn't for the node in question; you're just looking N, S, E, W all around it.

    if row > 0: # to search upward from the node
        neighbors.append((row - 1, col)) # if it's greater than 0, it's at least 1.

    if row + 1 < len(maze): # with this, you look down. If it's equal, then you can't look down any
        neighbors.append((row + 1, col)) 
    
    if col > 0: # to look left
        neighbors.append((row, col - 1)) # like before, this enables the 0th index.

    if col + 1 < len(maze[0]): # to look right, grab the first line to be sure how many elements there are (maze might not be square)
        neighbors.append((row, col + 1))

    return neighbors

def main(stdscr):  #this stands for 'standard output screen'
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)  # to implement a color.
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch() # "get character" from the user input.

wrapper(main) # initializes the curses module and calls main(). This enables us to control the output.
