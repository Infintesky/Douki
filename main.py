import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font

class TreeNode:
    def __init__(self, text, option_text1, option_text2, image_path, points_left, points_right, left=None, right=None):
        self.text = text                  # Text for current Node
        self.option_text1 = option_text1  # Text for choice 1
        self.option_text2 = option_text2  # Text for choice 2
        self.image_path = image_path      # Image path
        self.points_left = points_left    # Points for choice 1
        self.points_right = points_right  # Points for choice 2
        self.left = left                  # Left child
        self.right = right                # Right child

class DatingSimulator:
    def __init__(self):
        self.current_node = self.create_binary_tree()
        self.attraction_score = 0  # Initialize attraction score

        # Set up Tkinter window
        self.window = tk.Tk()
        self.window.title("Dating Simulator")

        # Create frames
        self.title_frame = tk.Frame(self.window)
        self.game_frame = tk.Frame(self.window)

        self.setup_game_screen()

        self.title_frame.pack()  # Start with the title screen

        self.setup_title_screen()

    def create_binary_tree(self):
        # Leaf nodes (Outcomes)
        outcome1 = TreeNode(
            "You ended up alone, but happy.", 
            None, None, 
            "./images/4.jpg", 0, 0
        )
        outcome2 = TreeNode(
            "You found true love!", 
            None, None, 
            "./images/4.jpg", 0, 0
        )
        outcome3 = TreeNode(
            "You became best friends instead.", 
            None, None, 
            "./images/4.jpg", 0, 0
        )
        outcome4 = TreeNode(
            "You decided to focus on your career.", 
            None, None, 
            "./images/4.jpg", 0, 0
        )

        # Intermediate questions
        q2 = TreeNode(
            "Do you prefer staying in or going out?",
            "Stay in", "Go out",
            "./images/3.jpg", 2, -1,
            outcome1, outcome2
        )
        q3 = TreeNode(
            "Would you compromise on hobbies?",
            "Yes", "No",
            "./images/2.jpg", 1, 2,
            outcome3, outcome4
        )

        # Root question
        root = TreeNode(
            "Do you value looks or personality more?",
            "Looks", "Personality",
            "./images/1.jpg", 3, -2,
            q2, q3
        )

        return root


    def setup_title_screen(self):
        # Title label
        custom_font = font.Font(family="Times New Roman", size=35, weight="bold", slant="italic")
        self.title_label = tk.Label(self.title_frame, text="Welcome to Dating Simulator", font=custom_font, bg="bisque")
        self.title_label.pack(pady=20)

        # Start button
        start_button = tk.Button(self.title_frame, text="Start Game", font=("Helvetica", 14, "bold"), command=self.start_game, bg="bisque", fg="purple")
        start_button.pack(side=tk.LEFT, padx=100, pady=10)

        # Exit button
        exit_button = tk.Button(self.title_frame, text="Exit", font=("Helvetica", 14, "bold"), command=self.exit_game, bg="bisque", fg="purple")
        exit_button.pack(side=tk.LEFT, padx=100, pady=10)

        # Start blinking effect
        self.blink()

    def exit_game(self):
        pass

    def blink(self):
        current_color = self.title_label.cget("fg")  # Access `fg` of the label, not the frame
        next_color = "orange" if current_color == "light salmon" else "light salmon"  # Toggle color
        self.title_label.config(fg=next_color)
        self.title_label.after(200, self.blink)  # Call blink() again after 500ms



    def credits_scene(self):
        pass

    def setup_game_screen(self):
        # Game interface widgets
        self.image_label = tk.Label(self.game_frame)
        self.image_label.pack(pady=10)

        self.text_label = tk.Label(self.game_frame, text="", wraplength=400, font=("Arial", 14))
        self.text_label.pack(pady=20)

        self.choice1_button = tk.Button(self.game_frame, text="", command=self.make_choice1, font=("Arial", 12))
        self.choice1_button.pack(side=tk.LEFT, expand=1, pady=10)

        self.choice2_button = tk.Button(self.game_frame, text="", command=self.make_choice2, font=("Arial", 12))
        self.choice2_button.pack(side=tk.RIGHT, expand=1, pady=10)

    def start_game(self):
        # Transition to the game screen
        self.title_frame.pack_forget()
        self.game_frame.pack()
        self.update_display()

    def make_choice1(self):
        self.attraction_score += self.current_node.points_left
        self.navigate(self.current_node.left)

    def make_choice2(self):
        self.attraction_score += self.current_node.points_right
        self.navigate(self.current_node.right)

    def navigate(self, next_node):
        if next_node:
            self.current_node = next_node
            self.update_display()
        else:
            self.display_outcome()

    def update_display(self):
        # Update the text for the current question
        self.text_label.config(text=self.current_node.text)

        # Update the image for the current node
        image = ImageTk.PhotoImage(Image.open(self.current_node.image_path))
        self.image_label.config(image=image)
        self.image_label.image = image  # Keep reference to avoid garbage collection

        # Check if the current node is a leaf
        if self.current_node.left is None and self.current_node.right is None:
            self.display_outcome()
        else:
            # Update the button text for the choices
            self.choice1_button.config(text=self.current_node.option_text1)
            self.choice2_button.config(text=self.current_node.option_text2)

    def display_outcome(self):
        # Display the final outcome
        self.text_label.config(text=f"{self.current_node.text}\n\nFinal Attraction Score: {self.attraction_score}")
        image = ImageTk.PhotoImage(Image.open(self.current_node.image_path))
        self.image_label.config(image=image)
        self.image_label.image = image  # Keep reference to avoid garbage collection
        self.choice1_button.pack_forget()
        self.choice2_button.pack_forget()

    def run(self):
        self.window.mainloop()





def main():
    # Run the simulator
    simulator = DatingSimulator()
    simulator.run()




if __name__ == "__main__":
    main()
