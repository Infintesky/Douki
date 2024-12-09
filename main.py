import tkinter as tk
from tkinter import font

class TreeNode:
    """
    A class representing a node in a decision tree for the game.

    Each node contains the text for a scenario, two options for the user to choose from, 
    an associated image, and points assigned to each option. The node also has references 
    to its left and right child nodes, representing subsequent scenarios based on user choices.
    """

    def __init__(self, text, option_text1, option_text2, image_path, points_left, points_right, left, right):
        """
        Initializes a TreeNode instance.

        Parameters:
        - text (str): The main text displayed at this node.
        - option_text1 (str): The text for the first choice.
        - option_text2 (str): The text for the second choice.
        - image_path (str): The path to the image associated with this node.
        - points_left (int): Points awarded for choosing the first option.
        - points_right (int): Points awarded for choosing the second option.
        - left (TreeNode, optional): The left child node representing the next scenario for option 1.
        - right (TreeNode, optional): The right child node representing the next scenario for option 2.
        """
        self.text = text                  # Text for current Node
        self.option_text1 = option_text1  # Text for choice 1
        self.option_text2 = option_text2  # Text for choice 2
        self.image_path = image_path      # Image path
        self.points_left = points_left    # Points for choice 1
        self.points_right = points_right  # Points for choice 2
        self.left = left                  # Left child
        self.right = right                # Right child


class DatingSimulator(tk.Tk):
    def __init__(self):
        super().__init__()  # Initialize the tk.Tk class

        # Assign self (the Tk instance) to self.window for readability
        self.window = self

        self.current_node = self.create_binary_tree()
        self.attraction_score = 0  # Initialize attraction score

        # Screen size
        self.window.geometry("1024x768")

        # Set up Tkinter window
        self.window.title("Dating Simulator")

        # Create frames
        self.title_frame = tk.Frame(self.window)
        self.game_frame = tk.Frame(self.window)

        self.setup_game_screen()

        self.title_frame.pack()  # Start with the title screen

        self.setup_title_screen()


    def create_binary_tree(self):
        # Layer 4 node (clear node)
        l4_1 = TreeNode(
            "",
            "",
            "",
            "", 0, 0,
            None, None
        )

        # Layer 3 nodes
        l3_1 = TreeNode(
            "During dinner in their room, Ryan notices Kai Siang eating Hello Panda. He admits he's in debt.",
            "You broke ah? You lucky I like you! I pay for you this week.", "I lend you $100! You  next week pay me back but got interest $10 more!",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )
        l3_2 = TreeNode(
            "During a quiet evening, Kai Siang asks Ryan what he does for fun at the hostel.",
            "Been meaning to join your basketball games. Think you could teach me a thing or two?", "Not much, lah—just gaming and catching up on shows. You’d probably find it boring.",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )
        l3_3 = TreeNode(
            "After volleyball, Kai Siang thanks Ryan for helping him clean up the court.",
            "Of course—teammates help each other out. You can count on me anytime.", "No worries, lah—it’s part of the routine. You’d do the same for me.",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )
        l3_4 = TreeNode(
            "On a free weekend, Kai Siang asks Ryan about his plans. He seems hesitant, as if testing the waters.",
            "Nothing big planned. Want to check out Bugis or just chill at the hostel?", "Not much. You? Got anything exciting planned that I can tag along for?",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )
        l3_5 = TreeNode(
            "Kai Siang spills Teh C Siew Dai Peng at the canteen and looks horrified, muttering, 'Walao eh..!'",
            "Eh, don’t stress lah. I’ll grab napkins.", "Relax, bro—it’s just a drink. Happens to the best of us.",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )
        l3_6 = TreeNode(
            "Kai Siang says JJ Lin is performing at the stadium, but tickets are expensive.",
            "Wah, let’s go ah — so rare to see them live!", "Sounds amazing, but maybe we can wait for the next show when it’s less pricey?",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )
        l3_7 = TreeNode(
            "Kai Siang shares a nostalgic story about his hometown with his parents.",
            "That sounds so fun. I’ve never been to one like that—maybe you can show me someday?", "Wah, nice memory. It’s great that you have moments like that to treasure.",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )
        l3_8 = TreeNode(
            "Kai Siang is rushing to finish an assignment and looks stressed as the deadline approaches.",
            "Don’t stress—I’ll help you double-check and format so you can submit on time.", "Wah, cutting it close. Focus on the main parts—you’ll get it done.",
            "./images/4.png", 1, 0,
            l4_1, l4_1
        )

        # Layer 2 nodes
        l2_1 = TreeNode(
            " After that, Ryan notices Kai Siang sitting moodily at his table, scrolling on his phone, stressed.",
            "You okay? Want to talk it out?", "DAMN! Take it easy lil man!",
            "./images/4.png", 1, 0,
            l3_1, l3_2
        )
        l2_2 = TreeNode(
            "While practicing the problem sets for biology, Kai Siang is seems as if he is struggling and looks visibly frustrated afterward.",
            "Want to practice on me right now?", "Want to talk about it?",
            "./images/4.png", 1, 0,
            l3_3, l3_4
        )
        l2_3 = TreeNode(
            "Ryan overhears classmates discussing Kai Siang's recent performance in class. One of them says, 'Why's he so sad?'",
            "Let's go out and destress! We can dress up nicely and go to the arcade and take some photos at the photobooth!!!", "It must be the stress from the finals.",
            "./images/4.png", 1, 0,
            l3_5, l3_6
        )
        l2_4 = TreeNode(
            " After a long week, Kai Siang invites Ryan to play Valorant with him.",
            "Can u coach me? I don't know how to play!", "Sorry I have group meeting 🙁 You have fun though!",
            "./images/4.png", 1, 0,
            l3_7, l3_8
        )

        # Layer 1 nodes
        l1_1 = TreeNode(
            "Kai Siang admits he’s stuck for the Rhino 3D project and he needs all the help he can get especially from his hero Ryan.",
            "Come, let me help you! I already finished it.", "Wah, you’ve been pushing yourself. Tonight, rest early— let me give you a massage! You seem really tense....",
            "./images/3.png", 1, 0,
            l2_1, l2_2
        )
        l1_2 = TreeNode(
            "When studying together in their shared room, Kai Siang leans over and asks Ryan, 'Do you want to choose the CSD or EPD pillar or me! HAHA jokes!'. He seems conflicted as he saw Ryan talking with another girl.",
            "What are you talking about! You will always be my first choice!", "I'm not so sure about us right now...",
            "./images/2.png", 1, 0,
            l2_3, l2_4
        )

        # Layer 0 node
        root = TreeNode(
            "Ryan sees Kai Siang in the room, scribbling notes furiously, his laptop open to a dense slide deck. His shoulders are tense, and he’s muttering, “加油 (Jiāyóu)” under his breath.",
            "Hey, looks like you’ve been at it for a while. Want to take a quick break? Maybe some green te will help clear your head.", "You okay? You’re working hard—if you need to vent or take a breather, I’m here.",
            "./images/1.png", 1, 0,
            l1_1, l1_2
        )

        return root


    def setup_title_screen(self):
        print("setup_title_screen called")  # Debugging

        for widget in self.title_frame.winfo_children():
            widget.destroy()
        self.title_frame.pack_forget()
        self.game_frame.pack_forget()  # Ensure the game frame is not visible

        # Reset and reinitialize the title frame
        self.title_frame = tk.Frame(self.window)  # Create a new title frame
        self.title_frame.pack()
        
        self.update_display()
        # Title label
        custom_font = font.Font(family="Times New Roman", size=35, weight="bold", slant="italic")
        self.title_label = tk.Label(self.title_frame, text="Welcome to Dating Simulator", font=custom_font, bg="bisque")
        self.title_label.pack(pady=20)

        # Start button
        start_button = tk.Button(self.title_frame, text="Start Game", font=("Helvetica", 14, "bold"),
                                 command=self.start_game, bg="bisque", fg="light salmon")
        start_button.pack(side=tk.LEFT, padx=100, pady=10)

        # Exit button
        exit_button = tk.Button(self.title_frame, text="Exit", font=("Helvetica", 14, "bold"), command=self.exit_game,
                                bg="bisque", fg="light salmon")
        exit_button.pack(side=tk.LEFT, padx=100, pady=10)

        # Start blinking effect
        self.blink()


    def exit_game(self):
        # Exit the window
        self.destroy()

    def blink(self):
        current_color = self.title_label.cget("fg")  # Access `fg` of the label, not the frame
        next_color = "pink" if current_color == "light salmon" else "light salmon"  # Toggle color
        self.title_label.config(fg=next_color)
        self.title_label.after(200, self.blink)  # Call blink() again after 500ms

    def credits_scene(self):
    # Clear the display_outcome screen
        for widget in self.game_frame.winfo_children():
            widget.pack_forget()  # Remove all widgets from the game frame
        # Create a full-screen black background
        background_frame = tk.Frame(self.window, bg="black")
        background_frame.place(relx=0, rely=0, relwidth=1, relheight=1)  # Covers the entire window

        # Label to display the credits
        credits_label = tk.Label(
            self.window,
            text="",
            font=("Helvetica", 40, "normal"),  # Use Helvetica
            justify="center",
            wraplength=500,  # Wrap text within a reasonable width
            bg="black",  # Background black
            fg="white"  # Text color white
    )
        # Function to scroll credits
        credits_text = '''










        





Cast

Ryan

Sherylyn

Wei Yang

Kai Siang

Beth

Alvin

Thank you for playing :)
        '''
        credits_label.config(text=credits_text)  # Set initial text
        credits_label.place(relx=0.5, y=self.window.winfo_height(), anchor="n")  # Start from bottom

        # Function to move text upward
        def scroll_text():
            current_y = credits_label.winfo_y()  # Get current Y position
            if current_y + credits_label.winfo_height() > 0:  # If still visible
                credits_label.place(y=current_y - 2)  # Move up by 2 pixels
                credits_label.after(30, scroll_text)  # Repeat after 30ms
            else:
                credits_label.config(text="")  # Clear text once it scrolls out
                show_back_button()  # Show the "Back to Title Screen" button
        
        # Function to show "Back to Title Screen" button
        def show_back_button():
        # Clear all widgets from the `background_frame`
            for widget in background_frame.winfo_children():
                widget.destroy()
            background_frame.destroy()  # Remove the credits background frame

            # Transition back to the title screen
            self.title_frame.pack()  # Make sure the title frame is visible
            self.setup_title_screen()  # Set up the title screen
        

        scroll_text()  # Start scrolling

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
        # Clear the title screen
        for widget in self.title_frame.winfo_children():
            widget.destroy()
        self.title_frame.pack_forget()  # Hide the title frame

        # Clear any residual widgets in the game frame
        for widget in self.game_frame.winfo_children():
            widget.destroy()

        # Reinitialize the game frame
        self.setup_game_screen()
        self.game_frame.pack()

        # Reset the game state
        self.current_node = self.create_binary_tree()  # Reset to the root node
        self.attraction_score = 0  # Reset attraction score
        self.update_display()  # Display the first scenario

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
        image = tk.PhotoImage(file=self.current_node.image_path)
        self.image_label.config(image=image)
        self.image_label.image = image  # Keep reference to avoid garbage collection

        # Check if the current node is a leaf
        if self.current_node.left is None and self.current_node.right is None:
            self.display_outcome()
        else:
            # Update the button text for the choices
            self.choice1_button.config(text=self.current_node.option_text1, wraplength= 400)
            self.choice2_button.config(text=self.current_node.option_text2, wraplength= 400)

    def display_outcome(self):

        if self.attraction_score >= 4 :
            ending_text = "Congratulations! You built a strong connection with Kai Siang. Keep cherishing these moments!"
            image_path = "./images/4.png"

        elif self.attraction_score >= 2:
            ending_text = "Not bad! Kai Siang appreciates your effort, but there's room to grow closer."
            image_path = "./images/4.png"

        elif self.attraction_score >= 1:
            ending_text = "Try again! Kai Siang is just your Hi-Bye freind."
            image_path = "./images/4.png"

        else:
            ending_text = "U NEEEED TO LEAVE!!! U are HATEDDD! ALWAYS HATED!!!!"
            image_path = "./images/4.png"

        # Update display
        self.text_label.config(text=ending_text)
        image = tk.PhotoImage(file=image_path)
        self.image_label.config(image=image)
        self.image_label.image = image  # Avoid garbage collection
        self.choice1_button.pack_forget()
        self.choice2_button.pack_forget()

        # Create a new frame for the "Next" button
        button_frame = tk.Frame(self.game_frame)
        button_frame.pack(pady=20)

        # Add "Next" button to transition to the credits scene
        next_button = tk.Button(button_frame, text="Next", font=("Helvetica", 14, "bold"),
                             command=self.credits_scene, bg="bisque", fg="light salmon")
        next_button.pack(pady=10)
    def run(self):
        self.window.mainloop()

def main():
    # Run the simulator
    simulator = DatingSimulator()
    simulator.run()


if __name__ == "__main__":
    main()
