"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # The distance of each year's line.
    line_dist = (width-2*GRAPH_MARGIN_SIZE) // len(YEARS)
    # The x-coordinate for each year.
    x = GRAPH_MARGIN_SIZE + year_index*line_dist
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Upper and lower boundary.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # Year's line.
    for i in range(len(YEARS)):
        x_axis = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(GRAPH_MARGIN_SIZE+x_axis, 0, GRAPH_MARGIN_SIZE+x_axis,CANVAS_HEIGHT)
        canvas.create_text(GRAPH_MARGIN_SIZE+x_axis+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    x_axis = []
    y_axis = []
    # Store all X and Y coordinates in list.
    for i in range(len(YEARS)):
        year = str(YEARS[i])
        for name in lookup_names:
            # Check whether the name rank 1~1000 in the year.
            if year in name_data[name]:
                # get x coordinate
                x = get_x_coordinate(CANVAS_WIDTH, i) + GRAPH_MARGIN_SIZE
                x_axis.append(x)
                # get the rank in the year
                rank = name_data[name][year]
                # get y coordinate
                y = GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)*(int(rank)/MAX_RANK)
                y_axis.append(y)
            # The rank is out of 1000.
            else:
                # get x coordinate
                x = get_x_coordinate(CANVAS_WIDTH, i)+ GRAPH_MARGIN_SIZE
                x_axis.append(x)
                # y coordinate is the bottom of Y axis.
                y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                y_axis.append(y)

    # Use X,Y list to draw lines, one name needs to draw 11 lines.
    for i in range(len(lookup_names)):
        new_x_axis = []
        new_y_axis = []
        color_num = i % 4
        # Separate the X,Y coordinates of each name.
        for j in range(len(x_axis)):
            if j % len(lookup_names) == i:
                new_x_axis.append(x_axis[j])
                new_y_axis.append(y_axis[j])
        # Draw lines.
        for k in range(len(YEARS)-1):
            x1 = new_x_axis[k]
            x2 = new_x_axis[k+1]
            y1 = new_y_axis[k]
            y2 = new_y_axis[k+1]
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[color_num])
            if str(YEARS[k]) in name_data[lookup_names[i]]:
                canvas.create_text(x1+TEXT_DX, y1, text=lookup_names[i] + ' ' + name_data[lookup_names[i]][str(YEARS[k])], anchor=tkinter.SW,fill=COLORS[color_num])
            # If rank >1000.
            else:
                canvas.create_text(x1 + TEXT_DX, y1, text=lookup_names[i] + ' *',anchor=tkinter.SW, fill=COLORS[color_num])
        # Last data.
        if str(YEARS[len(YEARS)-1]) in name_data[lookup_names[i]]:
            canvas.create_text(new_x_axis[len(YEARS)-1] + TEXT_DX, new_y_axis[len(YEARS)-1], text=lookup_names[i]+' ' + name_data[lookup_names[i]][str(YEARS[len(YEARS)-1])],anchor=tkinter.SW, fill=COLORS[color_num])
        else:
            canvas.create_text(new_x_axis[len(YEARS) - 1] + TEXT_DX, new_y_axis[len(YEARS) - 1],text=lookup_names[i] + ' *', anchor=tkinter.SW, fill=COLORS[color_num])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
