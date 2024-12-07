import tkinter as tk
from tkinter import font

class TreeNode:
    """
    A class representing a node in a decision tree for the game.

    Each node contains the text for a scenario, two options for the user to choose from, 
    an associated image, and points assigned to each option. The node also has references 
    to its left and right child nodes, representing subsequent scenarios based on user choices.
    """

    def __init__(self, text, option_text1, option_text2, image_path, points_left, points_right, left=None, right=None):
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
        # Layer 3 nodes
        l3_1 = TreeNode(
            "During dinner at the hostel, Ryan notices Kai Siang eating plain bread. He admits he forgot his wallet in his dorm.",
            "Forgot your wallet, ah? Let’s share my chicken rice—take some, no need to stress.", "Tough day? Want me to grab something for you? You can pay me back when it’s convenient.",
            "./images/4.png", 1, 0,
        )
        l3_2 = TreeNode(
            "During a quiet evening, Kai Siang asks Ryan what he does for fun at the hostel.",
            "Been meaning to join your basketball games. Think you could teach me a thing or two?", "Not much, lah—just gaming and catching up on shows. You’d probably find it boring.",
            "./images/4.png", 1, 0
        )
        l3_3 = TreeNode(
            "After volleyball, Kai Siang thanks Ryan for helping him clean up the court.",
            "Of course—teammates help each other out. You can count on me anytime.", "No worries, lah—it’s part of the routine. You’d do the same for me.",
            "./images/4.png", 1, 0
        )
        l3_4 = TreeNode(
            "On a free weekend, Kai Siang asks Ryan about his plans. He seems hesitant, as if testing the waters.",
            "Nothing big planned. Want to check out Bugis or just chill at the hostel?", "Not much. You? Got anything exciting planned that I can tag along for?",
            "./images/4.png", 1, 0
        )
        l3_5 = TreeNode(
            "Kai Siang spills Teh C Siew Dai Peng at the canteen and looks horrified, muttering, 'Walao eh..!'",
            "Eh, don’t stress lah. I’ll grab napkins.", "Relax, bro—it’s just a drink. Happens to the best of us.",
            "./images/4.png", 1, 0
        )
        l3_6 = TreeNode(
            "Kai Siang says JJ Lin is performing at the stadium, but tickets are expensive.",
            "Wah, let’s go ah — so rare to see them live!", "Sounds amazing, but maybe we can wait for the next show when it’s less pricey?",
            "./images/4.png", 1, 0
        )
        l3_7 = TreeNode(
            "Kai Siang shares a nostalgic story about his hometown with his parents.",
            "That sounds so fun. I’ve never been to one like that—maybe you can show me someday?", "Wah, nice memory. It’s great that you have moments like that to treasure.",
            "./images/4.png", 1, 0
        )
        l3_8 = TreeNode(
            "Kai Siang is rushing to finish an assignment and looks stressed as the deadline approaches.",
            "Don’t stress—I’ll help you double-check and format so you can submit on time.", "Wah, cutting it close. Focus on the main parts—you’ll get it done.",
            "./images/4.png", 1, 0
        )

        # Layer 2 nodes
        l2_1 = TreeNode(
            " Ryan notices Kai Siang sitting alone at the hostel canteen, scrolling on his phone, his plate of Cai Fan barely touched.",
            "Cai Fan again? You okay? Want some company? I’ve been meaning to chat with you about weekend plans.", "Busy day, huh? How about we can catch up later?",
            "./images/4.png", 1, 0,
            l3_1, l3_2
        )
        l2_2 = TreeNode(
            "During volleyball practice, Kai Siang is not performing well and looks visibly frustrated afterward.",
            "Rough day? Want to practice tomorrow?", "One of those days, huh? You’ve been solid otherwise—don’t let a few misses get to you.",
            "./images/4.png", 1, 0,
            l3_3, l3_4
        )
        l2_3 = TreeNode(
            "Ryan overhears classmates discussing Kai Siang's recent volleyball performance. One of them says, 'He’s okay, but he’s not as naturally talented as the rest of us.'",
            "Natural talent only gets you so far. You know how much effort he puts in—he’s the reason our team has been improving.", "Wah, not fair lah. He’s been working hard and showing up every practice. Give him some credit.",
            "./images/4.png", 1, 0,
            l3_5, l3_6
        )
        l2_4 = TreeNode(
            "After a long week, Kai Siang invites Ryan to a casual basketball game with his friends, saying it’s a great way to unwind.",
            "Sounds like fun! I might not be great, but I’d love to join—you’ll have to coach me though!", "Basketball sounds great, but I’m wiped out this week. I’ll come along and cheer you on, though.",
            "./images/4.png", 1, 0,
            l3_7, l3_8
        )

        # Layer 1 nodes
        l1_1 = TreeNode(
            "Kai Siang admits he’s feeling unwell after a long night of studying. He skipped breakfast because he overslept and looked visibly drained.",
            "Sounds like you need a recharge. How about I grab something light from the canteen for you—porridge maybe?", "Wah, you’ve been pushing yourself. Tonight, rest early—I’ll help you catch up on any notes.",
            "./images/3.png", 1, 0,
            l2_1, l2_2
        )
        l1_2 = TreeNode(
            "During class, Kai Siang leans over and asks Ryan about choosing between the CSD or EPD pillar. He seems conflicted and mentions that he enjoys both areas.",
            "It’s a big decision. Let’s talk tonight—maybe we can list out your strengths and interests together.", "Wah, both are great. I’d say think about which one you’d enjoy waking up for every day—it’s about what feels right.",
            "./images/2.png", 1, 0,
            l2_3, l2_4
        )

        # Layer 0 node
        root = TreeNode(
            "Ryan sees Kai Siang in the library, scribbling notes furiously, his laptop open to a dense slide deck. His shoulders are tense, and he’s muttering, “加油 (Jiāyóu)” under his breath.",
            "Hey, looks like you’ve been at it for a while. Want to take a quick break? Maybe Kopi Peng will help clear your head.", "You okay? You’re working hard—if you need to vent or take a breather, I’m here.",
            "./images/1.png", 1, 0,
            l1_1, l1_2
        )

        return root


    def setup_title_screen(self):
        # Title label
        custom_font = font.Font(family="Times New Roman", size=35, weight="bold", slant="italic")
        self.title_label = tk.Label(self.title_frame, text="Welcome to Dating Simulator", font=custom_font, bg="bisque")
        self.title_label.pack(pady=20)

        # Start button
        start_button = tk.Button(self.title_frame, text="Start Game", font=("Helvetica", 14, "bold"), command=self.start_game, bg="bisque", fg="light salmon")
        start_button.pack(side=tk.LEFT, padx=100, pady=10)

        # Exit button
        exit_button = tk.Button(self.title_frame, text="Exit", font=("Helvetica", 14, "bold"), command=self.exit_game, bg="bisque", fg="light salmon")
        exit_button.pack(side=tk.LEFT, padx=100, pady=10)

        # Start blinking effect
        self.blink()

    def exit_game(self):
        pass

    def blink(self):
        current_color = self.title_label.cget("fg")  # Access `fg` of the label, not the frame
        next_color = "pink" if current_color == "light salmon" else "light salmon"  # Toggle color
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
        image = tk.PhotoImage(file=self.current_node.image_path)
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
        image = tk.PhotoImage(file=self.current_node.image_path)
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
