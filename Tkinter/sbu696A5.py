'''
name: Elliot Bu
username: sbu696
ID number: 813663655
Description: This program is to read the files and process.
    Procession: The program will read the color dictionary from the text file and fill it into the pattern file.
    The program will form the pixel art and present it in GUI.
'''

from tkinter import *
def main():
    size = 30
    start_left = size * 2
    start_down = size * 2
    pattern_filename, palette_filename = get_filenames()
    pattern_list = process_file(pattern_filename)
    colours_list = process_file(palette_filename)
    colours_dictionary = create_colour_dictionary(colours_list)

    number_of_rows = len(pattern_list)	
    number_of_columns = len(pattern_list[0])
    canvas_width = size * number_of_columns +size * 4
    canvas_height = number_of_rows * size + size * 4
    
    window = Tk() 
    window.title("A5 by Elliot Bu") 
    geometry_string = str(canvas_width)+"x"+str(canvas_height)+"+10+20"
    window.geometry(geometry_string)
    a_canvas = Canvas(window)
    a_canvas.config(background="white")
    a_canvas.pack(fill=BOTH, expand = True)
    draw_pattern(a_canvas, colours_dictionary, pattern_list, size, start_left, start_down)

def get_filenames():
    input_name = input("Enter a name: ")
    first_filename = input_name + ".txt"
    second_filename = input_name + "_palette.txt"
    return first_filename,second_filename

def process_file(filename):
    output_file = open(filename, 'r')
    string = output_file.read()
    strings = string.split()
    output_file.close()
    return strings

def create_colour_dictionary(colours_list):
    new_dict = {}
    for word in colours_list:
        if word[0] == "#":
            new_dict["#"] = word[2:]
        elif word[0] == "$":
            new_dict["$"] = word[2:]
        elif word[0] == "%":
            new_dict["%"] = word[2:]
        elif word[0] == "&":
            new_dict["&"] = word[2:]
        elif word[0] == "@":
            new_dict["@"] = word[2:]
    return new_dict     

def draw_pattern(a_canvas, colours_dictionary, pattern_list, size, start_x, start_y):     
    for column in range(len(pattern_list)):
        y = start_y + size * column
        for row in range(len(pattern_list[column])):
            x = start_x + size * row
            single_code = pattern_list[column][row]
            colour = colours_dictionary[single_code]
            a_canvas.create_rectangle(x,y, x+size, y+size, fill = colour)
    
main()
