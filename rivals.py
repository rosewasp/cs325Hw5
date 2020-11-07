# Author: Abhash Sharma
# Fall 2020 CS325
# Hw 5, 5

# citation (handling files): https://www.tutorialspoint.com/How-to-read-a-file-from-command-line-using-Python

import sys

def get_clear_line(file_name):
    """processes a text file, clears that line, and returns the number on that line"""
    return file_name.readline().strip()

with open(sys.argv[1], 'r') as infile:
    # g is where we start building a graph
    g = {}

    # n has total number of fighters
    n = get_clear_line(infile)

    # stops processing file when end of file is reached
    if n == "":
        infile.close()
    # convert n to int
    n = int(n)

    # add all the fighters as dictionary keys
    for i in range(n):
        # on the outset make every vertex a good guy
        # also make every vertex unseen/not-processed (0:unseen, 1:seen)
        g[infile.readline().rstrip()] = ['gg', 0]

    # process rivalries/edges
    r = int(infile.readline().strip())

    # iterate through all the rivalries
    for j in range(r):
        fighter_a, fighter_b = map(str, infile.readline().strip().split())

        # when two rivals have been seen
        if g[fighter_a][1] == 1 and g[fighter_b][1] == 1:
            # and they have they are in the same team
            if g[fighter_a][0] == g[fighter_b][0]:
                print("Impossible")
                sys.exit()
        # when one of the rival has not been seen
        else:
            # two rivals can't be in the same team
            if g[fighter_a][0] == g[fighter_b][0]:
                if g[fighter_a][0] == 'gg':
                    if g[fighter_b][1] == 0:
                        g[fighter_b][0] = 'bg'
                        g[fighter_a][1] = 1
                        g[fighter_b][1] = 1
                    elif g[fighter_b][1] == 1:
                        if g[fighter_b][0] == 'gg':
                            g[fighter_a][0] = 'bg'
                            g[fighter_a][1] = 1
                        elif g[fighter_b][0] == 'bg':
                            [fighter_a][0] = 'gg'
                            g[fighter_a][1] = 1
                elif g[fighter_a][0] == 'bg':
                    if g[fighter_b][1] == 0:
                        g[fighter_b][0] = 'gg'
                        g[fighter_a][1] = 1
                        g[fighter_b][1] = 1
                    elif g[fighter_b][1] == 1:
                        if g[fighter_b][0] == 'bg':
                            g[fighter_a][0] = 'gg'
                            g[fighter_a][1] = 1
                        elif g[fighter_b][0] == 'gg':
                            [fighter_a][0] = 'bg'
                            g[fighter_a][1] = 1
            # when two rivals are already in separate team
            # leave them be, just marked them seen
            else:
                g[fighter_a][1] = 1
                g[fighter_b][1] = 1

    # when possible to divide all fighters as rivals
    print("Yes Possible")
    print("Babyfaces:", *[k for (k, v) in g.items() if v[0] == "gg"])
    print("Heels:", *[k for (k, v) in g.items() if v[0] == "bg"])
    sys.exit()