
# Definition of th dictionary THEMES
THEMES = {"0": {"name": "Default", 0: "", 1: "1", 2: "2", 3: "3", 6: "6", 12: "12", 24: "24", 48: "48", 96: "96", 192: "192", 384: "384", 768: "768", 1536: "1536", 3072: "3072", 6144: "6144", 12288: "12288"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be",
                                                                                                                                                                                                   32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}


# Etape 1: Afficher une grille initiale de jeu

def grid_to_string(game_grid, size):
    '''
    This function transforms the grid, that is in the form of a matrix, into a string
    but now it's updated to consider the size of the tuiles.


    Inputs
    --------
    game_grid: Matrix of a certain size
    size: Size of the Matrix

    Outputs
    --------
    string: A string that corresponds to the input grid

    '''

    string = ""
    # Picking up every line in the matrix
    for line in game_grid:
        # Adding the upper and lower limits
        string = string + "\n"
        for i in range(size):
            string = string + " ==="
        string = string + "\n"
        # Adding bars in the sides creating the tiles
        for m in range(size+1):
            if m < size:
                string = string + "| " + str(line[m]) + " "
            else:
                string = string + "|"
    string = string + "\n"
    # Adding the lowest limit and needed spaces to pass the test
    for s in range(size):
        string = string + " ==="
    string = string[1:] + "\n   "
    return string

# Etape 2: Adapter pour prendre en compte la largeur des tuiles

# We needed this function to have a list of the elements of the grid (Made by Christos and Victor)


def get_all_tiles(game_grid):
    tiles = []
    for i in game_grid:
        i = [0 if x == ' ' else x for x in i]
        tiles.extend(i)
    return tiles

# We need to create a function that determines the longest element of the grid


def long_value(game_grid):
    '''
    This function takes the grid and tracks the size of the longest value, this function still
    works only for integer elements

    Inputs
    --------
    game_grid: Matrix of a certain size

    Outputs
    --------
    max_long: A integer that represents the max size of a element in the given grid

    '''
    max_tile = max(get_all_tiles(game_grid))
    # Transform the integer into a string so we can measure the lenght
    max_in_string = str(max_tile)
    max_long = len(max_in_string)
    return max_long


def grid_to_string_with_size(game_grid, size):
    '''
    This function transforms the grid, that is in the form of a matrix, into a string
    but now it's updated to consider the size of the tuiles.

    COMMENT: This function has not really passed by the fase REFACTOR

    Inputs
    --------
    game_grid: Matrix of a certain size
    n: Size of the Matrix

    Outputs
    --------
    string: A string that corresponds to the input grid

    '''
    max_long = long_value(game_grid)

    string = ""
    for line in game_grid:
        # Adding the upper and lower limits, for this we need to consider the
        # max size of an element in the given grid
        string = string + "\n"
        for i in range(size):

            for t in range(max_long):
                string += "="
            string += "="
        string += "=\n"

        # Adding bars in the sides creating the tiles
        for m in range(size+1):

            if m < size:
                element = line[m]
                long_element = len(str(element))
                diference = max_long - long_element
                string += "|" + str(line[m])
                for k in range(diference):
                    string += " "
            else:
                string += "|"

    string = string + "\n"

    # Adding the lowest limit considering the max size again
    for s in range(size):
        for p in range(max_long):
            string += "="
        string += "="
    string += "="
    # Cutting the first \n and adding one in the end
    string = string[1:] + "\n"
    return string


def grid_to_string_with_size_and_theme(game_grid, DicTheme, size):
    '''
    This function transforms the grid, that is in the form of a matrix, into a string
    but now it's updated to consider the size of the tuiles.


    Inputs
    --------
    game_grid : Matrix of a certain size
    DicTheme : Dictonary correspondent to the theme chosen for the game
    n : Size of the Matrix

    Outputs
    --------
    string: A string that corresponds to the input grid

    '''

    max_long = long_value_with_theme(game_grid, DicTheme)
    grid_with_theme = []
    for line in game_grid:
        line_with_theme = []
        for element in line:
            line_with_theme.append(DicTheme[element])
        grid_with_theme.append(line_with_theme)

    string = ""
    for line in grid_with_theme:
        # Adding the upper and lower limits, for this we need to consider the
        # max size of an element in the given grid
        string = string + "\n"
        for i in range(size):

            for t in range(max_long):
                string += "="
            string += "="
        string += "=\n"

        # Adding bars in the sides creating the tiles
        for m in range(size+1):

            if m < size:
                element = line[m]
                long_element = len(str(element))
                diference = max_long - long_element
                string += "|" + str(line[m])
                for k in range(diference):
                    string += " "
            else:
                string += "|"

    string = string + "\n"

    # Adding the lowest limit considering the max size again
    for s in range(size):
        for p in range(max_long):
            string += "="
        string += "="
    string += "="
    # Cutting the first \n and adding one in the end
    string = string[1:]
    return string


def long_value_with_theme(game_grid, DicTheme):
    '''
    This function takes the grid and tracks the size of the longest value taking by count the theme choosen

    Inputs
    --------
    game_grid : Matrix of a certain size
    DicTheme : Dictonary correspondent to the theme chosen for the game

    Outputs
    --------
    max_long: A integer that represents the max size of a element in the given grid.
    It's useful to know that max_long <= 4 for THEMES["0"], max_long <= 2 for THEMES["1"] and
    max_long <= 1 for THEMES["2"]

    '''

    list_tiles = get_all_tiles(game_grid)
    # Transform the integer into the string correspondent into the Theme so we can measure the lenght
    list_tiles_theme = []
    for element in list_tiles:
        # list of the lenghts of each element
        list_tiles_theme.append(len(DicTheme[element]))
    max_long = max(list_tiles_theme)
    return max_long
