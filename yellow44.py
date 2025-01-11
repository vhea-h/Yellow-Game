# Python recreation of Bart Bonte's Yellow: Level 44

import tkinter as tk

dir = "hori"

class YellowButton:
    def __init__(self, parent, row, col, grid_ref, width = 10, height = 5):
        self.row = row
        self.col = col
        self.grid_ref = grid_ref

        self.is_yellow = False
        self.colour_state = "black"

        self.button = tk.Button(
            parent, 
            bg=self.colour_state,
            width=width,
            height=height,
            command=self.game_move
        )
        self.button.grid(row = row, column = col)
    
    # Change and update button colour states
    def change_colour(self):
        if self.is_yellow:
            self.colour_state = "black"
            self.button.config(bg=self.colour_state)
            self.is_yellow = False
        elif self.is_yellow == False:
            self.colour_state = "yellow"
            self.button.config(bg=self.colour_state)
            self.is_yellow = True
        else:
            print ("COLOUR STATE ERROR")

    def change_right_grid(self):
        # Check if there is a button to the right of the current one
        if self.col + 1 < len(self.grid_ref[self.row]):  # Check if the column index is within the row's length
            target_button = self.grid_ref[self.row][self.col + 1]
            if (target_button != None): target_button.change_colour() 

    def change_left_grid(self):
    # Change the colour of the button to the left of the current one
        if self.col > 0:  # Check if there is a button to the right
            target_button = self.grid_ref[self.row][self.col - 1]  
            if (target_button != None): target_button.change_colour()  

    def change_below_grid(self):
    # Change the colour of the button to the right of the current one
        if self.row + 1 < 6:  # Check if there is a button below
            target_button = self.grid_ref[self.row + 1][self.col]  
            if (target_button != None): target_button.change_colour()  

    def change_above_grid(self):
    # Change the colour of the button to the right of the current one
        if self.row > 0:  # Check if there is a button above
            target_button = self.grid_ref[self.row - 1][self.col]  
            if (target_button != None): target_button.change_colour()   

    def game_move(self):
        global dir
        if dir == "hori":
            self.change_left_grid()
            self.change_right_grid()
            dir = "verti"
        
        elif dir == "verti":
            self.change_below_grid()
            self.change_above_grid()
            dir = "hori"

        else:
            print ("DIRECTIONAL ERROR")

    # Returns the indices of the button as a tuple 
    def get_indices(self):
        return self.row, self.col
    
    # Returns whether the button is yellow
    def check_yellow(self):
        return self.is_yellow
    
    def place_in_grid(self):
        self.button.grid(row = self.row, column=self.col)

def create_yellow_game():
    grid = []
    # Create the main application window
    root = tk.Tk()
    root.title("5x6 Grid with Yellow Corners")

    # Add a label at the top of the window
    title_label = tk.Label(root, text="Make the Screen Yellow!", font=("Arial", 16), bg="lightgray")
    title_label.pack(side="top", fill="x")  # Place it at the top and make it span the width of the window

    # Create a frame for the grid with some padding
    grid_frame = tk.Frame(root, bg="yellow", padx=20, pady=20)
    grid_frame.pack(expand=True)  # Center the frame in the window

    # Create a 5x6 grid of YellowButton instances
    for row in range(6):  # 6 rows
        grid_row = []
        for col in range(5):  #5 columns
            # Skip the corners (top-left, top-right, bottom-left, bottom-right)
            if (row == 0 and col == 0) or (row == 0 and col == 4) or (row == 5 and col == 0) or (row == 5 and col == 4):
                # Create a yellow square for corners
                yellow_square = tk.Label(grid_frame, bg="yellow", width=10, height=5)
                yellow_square.grid(row=row, column=col)
                grid_row.append(None)
            else:
                button = YellowButton(grid_frame, row, col, grid)
                grid_row.append(button)
                button.place_in_grid()
        grid.append(grid_row)


    root.mainloop()


if __name__ == "__main__":
    create_yellow_game()
