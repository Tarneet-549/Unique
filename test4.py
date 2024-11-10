import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class QuizGame:
    def _init_(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("500x500")
        self.root.configure(bg="lightgreen")

        # Define quiz categories and their questions
        self.categories = {
            "Alphabet": [
                {"question": "What letter comes after 'A'?", "options": ["B", "C", "D"], "answer": "B", "difficulty": "Easy"},
                {"question": "What letter comes before 'C'?", "options": ["B", "D", "E"], "answer": "B", "difficulty": "Easy"},
                {"question": "What letter is between 'D' and 'F'?", "options": ["E", "G", "H"], "answer": "E", "difficulty": "Easy"},
                {"question": "Which letter is the 5th in the alphabet?", "options": ["E", "F", "G"], "answer": "E", "difficulty": "Easy"},
                {"question": "Which letter is last in the alphabet?", "options": ["X", "Y", "Z"], "answer": "Z", "difficulty": "Easy"}
            ],
            "Numbers": [
                {"question": "What is 1 + 1?", "options": ["2", "3", "4"], "answer": "2", "difficulty": "Easy"},
                {"question": "What is 2 * 2?", "options": ["4", "5", "6"], "answer": "4", "difficulty": "Easy"},
                {"question": "What is 10 - 5?", "options": ["4", "5", "6"], "answer": "5", "difficulty": "Easy"},
                {"question": "What is 3 + 7?", "options": ["9", "10", "11"], "answer": "10", "difficulty": "Easy"},
                {"question": "What is 9 / 3?", "options": ["2", "3", "4"], "answer": "3", "difficulty": "Easy"}
            ],
            "Colors": [
                {"question": "What color is the sky?", "options": ["Blue", "Red", "Green"], "answer": "Blue", "difficulty": "Easy"},
                {"question": "What color is grass?", "options": ["Green", "Yellow", "Brown"], "answer": "Green", "difficulty": "Easy"},
                {"question": "What color is an apple?", "options": ["Red", "Blue", "White"], "answer": "Red", "difficulty": "Easy"},
                {"question": "What color are bananas?", "options": ["Yellow", "Orange", "Purple"], "answer": "Yellow", "difficulty": "Easy"},
                {"question": "What color is the ocean?", "options": ["Blue", "Black", "Gray"], "answer": "Blue", "difficulty": "Easy"}
            ],
            "Shapes": [
                {"question": "How many sides does a triangle have?", "options": ["3", "4", "5"], "answer": "3", "difficulty": "Easy"},
                {"question": "How many sides does a square have?", "options": ["3", "4", "6"], "answer": "4", "difficulty": "Easy"},
                {"question": "How many sides does a pentagon have?", "options": ["4", "5", "6"], "answer": "5", "difficulty": "Easy"},
                {"question": "How many sides does a hexagon have?", "options": ["5", "6", "7"], "answer": "6", "difficulty": "Easy"},
                {"question": "How many sides does an octagon have?", "options": ["6", "7", "8"], "answer": "8", "difficulty": "Easy"}
            ]
        }

        # Initialize quiz state
        self.current_category = None
        self.current_question_index = 0
        self.user_answers = []

        # Create widgets (buttons with images for each category)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Category", font=("Helvetica", 24, "bold"), bg="lightgreen").pack(pady=20)

        # Load images for buttons and resize them
        images = {
            "Alphabet": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\fs.jpg", (80, 80)),
            "Numbers": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\dds.jpg", (80, 80)),
            "Colors": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\aw.jpg", (80, 80)),
            "Shapes": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\k.jpg", (80, 80))
        }

        # Create a button for each category with its corresponding image
        for category in self.categories.keys():
            tk.Button(self.root, text=category, image=images[category], compound="top",
                      command=lambda c=category: self.start_quiz(c),
                      font=("Helvetica", 10, "bold"), bg="white", fg="black", relief=tk.RAISED, bd=11).pack(pady=10, fill=tk.X, padx=200)

        # Store the images to avoid garbage collection
        self.images = images

    def resize_image(self, path, size=(150, 150)):
        with Image.open(path) as img:
            img = img.resize(size, Image.LANCZOS)  # Correct attribute for high-quality resizing
            return ImageTk.PhotoImage(img)

    def start_quiz(self, category):
        self.current_category = category
        self.current_question_index = 0
        self.user_answers = []
        self.show_question()

    def show_question(self):
        # Clear the window
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_question_index < len(self.categories[self.current_category]):
            question = self.categories[self.current_category][self.current_question_index]

            tk.Label(self.root, text=f"Question {self.current_question_index + 1}", font=("Helvetica", 24, "bold"), bg="lightgreen").pack(pady=10)
            tk.Label(self.root, text=question["question"], font=("Helvetica", 18), bg="lightgreen", wraplength=500, justify="center").pack(pady=20)

            # Create buttons for options
            for option in question["options"]:
                tk.Button(self.root, text=option, font=("Helvetica", 16), bg="lightblue", fg="black", relief=tk.RAISED, bd=3,
                          command=lambda opt=option: self.check_answer(opt)).pack(pady=10, fill=tk.X, padx=50)

            tk.Button(self.root, text="Submit", command=self.next_question, font=("Helvetica", 16), bg="lightcoral", fg="white", relief=tk.RAISED, bd=5).pack(pady=20)

        else:
            tk.Label(self.root, text="Quiz Completed!", font=("Helvetica", 24, "bold"), bg="lightgreen").pack(pady=20)
            tk.Button(self.root, text="Back to Categories", command=self.go_back, font=("Helvetica", 16), bg="lightcoral", fg="white", relief=tk.RAISED, bd=5).pack(pady=20)

    def check_answer(self, selected_option):
        correct_answer = self.categories[self.current_category][self.current_question_index]["answer"]
        if selected_option == correct_answer:
            self.user_answers.append(True)
        else:
            self.user_answers.append(False)

    def next_question(self):
        self.current_question_index += 1
        self.show_question()

    def go_back(self):
        # Destroy previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Recreate category buttons
        self.create_widgets()

# Main application code
if __name__ == "_main_":
    root = tk.Toplevel()
    app = QuizGame(root)
    root.mainloop()