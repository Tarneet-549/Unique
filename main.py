import json
import subprocess
import tkinter

import AdaptiveLogic
import FeedBack

#from AdaptiveLogic import DrawingApp


from tkinter import ttk, messagebox
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
#from tkinter import ttk
import random

import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import subprocess

import adp

# Define your image paths
adaptive_image_path = r"C:\Users\Tarneet singh\OneDrive\Desktop\adaptation.png"
assessment_image_path = r"C:\Users\Tarneet singh\OneDrive\Desktop\analytics.png"
supportive_resources_image_path = r"C:\Users\Tarneet singh\OneDrive\Desktop\resources.png"
gamified_learning_image_path = r"C:\Users\Tarneet singh\OneDrive\Desktop\activity.png"
feedback_image_path = r"C:\Users\Tarneet singh\OneDrive\Pictures\Camera Roll\review.png"
hover_image_path = r"C:\Users\Tarneet singh\OneDrive\Desktop\more-info (1).png"  # The hover image remains the same
large_image_path = r"C:\Users\Tarneet singh\OneDrive\Pictures\rr.jpg"  # Large image on the right side
#snapshot_path = "snapshot.png"
#background_image_path = r"C:\Users\Tarneet singh\OneDrive\Desktop\btt.jpg"
#yt_image = r"C:\Users\Tarneet singh\OneDrive\Desktop\youtube.png"
# canva_image = r"C:\Users\Tarneet singh\OneDrive\Desktop\canvas.png"

import cv2
from fer import FER
import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
import matplotlib.pyplot as plt



import cv2
from supportive import detect_emotions, get_dominant_emotion, save_snapshot, plot_emotions, show_report  # Import functions from the utility file

# Initialize the camera
cap = cv2.VideoCapture(0)
snapshot_path = "snapshot.png"

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class QuizGame:
    def __init__(self, root):
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
            "Alphabet": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\dds.jpg", (80, 80)),
            "Numbers": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\fs.jpg", (80, 80)),
            "Colors": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\k.jpg", (80, 80)),
            "Shapes": self.resize_image(r"C:\Users\Tarneet singh\OneDrive\Desktop\aw.jpg", (80, 80))
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
            img = img.resize(size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)

    def start_quiz(self, category):
        self.current_category = category
        self.current_question_index = 0
        self.user_answers = []
        self.show_question()

    def show_question(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        if self.current_question_index < len(self.categories[self.current_category]):
            question = self.categories[self.current_category][self.current_question_index]

            tk.Label(self.root, text=f"Question {self.current_question_index + 1}", font=("Helvetica", 24, "bold"), bg="lightgreen").pack(pady=10)
            tk.Label(self.root, text=question["question"], font=("Helvetica", 18), bg="lightgreen", wraplength=500, justify="center").pack(pady=20)

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
        for widget in self.root.winfo_children():
            widget.destroy()
        self.create_widgets()

def open_personalized_assessments_window():
    detail_window = tk.Toplevel(root)
    detail_window.title("Personalized Assessments")
    detail_window.geometry("800x600")

    # Title and Description
    title_frame = ttk.Frame(detail_window)
    title_frame.pack(pady=20)
    ttk.Label(title_frame, text="Personalized Assessments", font=("Arial", 24, "bold")).pack()

    description_frame = ttk.Frame(detail_window)
    description_frame.pack(pady=10, padx=30)
    ttk.Label(description_frame,
              text="Personalized Assessments tailor evaluation methods to suit individual strengths and needs. Features include customized test formats, adaptive questioning, and detailed feedback. Understand how these assessments can improve learning outcomes.",
              font=("Arial", 14), wraplength=700, justify="center").pack()

    # Button to Start Quiz
    button_frame = ttk.Frame(detail_window)
    button_frame.pack(pady=30)
    ttk.Button(detail_window,
               text="Start Quiz",
               command=lambda: open_quiz_game(),
               style="TButton").pack(pady=10, padx=20)

    # Define the style for the button
    style = ttk.Style()
    style.configure("TButton", font=("Arial", 24), background="blue", foreground="red", padding=10)

def open_quiz_game():
    quiz_window = tk.Toplevel(root)
    QuizGame(quiz_window)

# Main application code
if __name__ == "__main__":
    root = tk.Toplevel()
    root.title("Main Application")
    root.geometry("800x600")

    #ttk.Button(root, text="Open Personalized Assessments", command=open_personalized_assessments_window).pack(pady=20)

    root.mainloop()


import gameka
def open_gamified_learning_window():
    # detail_window = tk.Toplevel(root)
    # detail_window.title("Gamified Learning")
    # detail_window.geometry("400x400")

    # Add heading
    #ttk.Label(detail_window, text="Gamified Learning", font=("Arial", 20, "bold")).pack(pady=10)


    gameka.hag_d()



# Main window (root)


# Button to open the Gamified Learning window
#button = ttk.Button(root, text="Open Gamified Learning", command=open_gamified_learning_window)
#button.pack(pady=20)


def open_youtube_learning():
    # Open Streamlit application for YouTube Learning
    subprocess.Popen(["streamlit", "run", "adp.py"])
    adp.run_streamlit_app()

def open_canvas_learning():
        # Open Tkinter application for Canvas Learning
    subprocess.Popen(["python", "AdaptiveLogic.py"])
    AdaptiveLogic.start(root)
def create_main_window():
    root = tk.Tk()
    root.title("Learning Platform")
    root.geometry("600x400")

    tk.Label(root, text="Choose Learning Option", font=("Arial", 28, "bold")).pack(pady=20)
    #yt_image = r"C:\Users\Tarneet singh\OneDrive\Desktop\youtube.png"


    tk.Button(root, text="YouTube Learning",font=("Comic Sans MS",24,"bold"), command=open_youtube_learning, width=40,height=5,bg= "red").pack(pady=6)
    tk.Button(root, text="Canvas Learning",font=("Comic Sans MS",24,"bold"), command=open_canvas_learning, width=40,height=5,bg="yellow").pack(pady=6)

    root.mainloop()





def open_supportive_resources_window():

    def checkEmotions():
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            emotions, box = detect_emotions(rgb_frame)

            if emotions:
                x, y, w, h = box
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                y_offset = 60
                overlay = frame.copy()
                for emotion, score in emotions.items():
                    emotion_text = f'{emotion.capitalize()}: {score:.2f}'
                    text_size = cv2.getTextSize(emotion_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
                    text_x = frame.shape[1] - text_size[0] - 20
                    cv2.rectangle(overlay, (text_x - 5, y_offset - 15), (text_x + text_size[0] + 5, y_offset + 5),
                                  (0, 0, 0), -1)
                    cv2.putText(frame, emotion_text, (text_x, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255),
                                2)
                    y_offset += 30
                cv2.addWeighted(overlay, 0.5, frame, 0.5, 0, frame)

                dominant_emotion = get_dominant_emotion(emotions)
                if dominant_emotion:
                    dominant_text = f'Dominant: {dominant_emotion[0].capitalize()}'
                    text_size = cv2.getTextSize(dominant_text, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
                    text_x = frame.shape[1] - text_size[0] - 20
                    cv2.rectangle(frame, (text_x - 5, 5), (text_x + text_size[0] + 5, 35), (0, 0, 0), -1)
                    cv2.putText(frame, dominant_text, (text_x, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

            exit_text = "PRESS Q TO SEE REPORT"
            text_size = cv2.getTextSize(exit_text, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)[0]
            text_x = (frame.shape[1] - text_size[0]) // 2
            text_y = frame.shape[0] - 20
            cv2.rectangle(frame, (text_x - 10, text_y - text_size[1] - 10), (text_x + text_size[0] + 10, text_y + 10),
                          (0, 0, 0), -1)
            cv2.putText(frame, exit_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

            cv2.imshow('Emotion Recognition', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                save_snapshot(frame, snapshot_path)
                cap.release()
                cv2.destroyAllWindows()

                if emotions:
                    plot_emotions(emotions, chart_type="bar")
                show_report(emotions, dominant_emotion, snapshot_path)
                break

    # Start the emotion detection process
    checkEmotions()

def open_feedback_window():
    FeedBack.create_feedback_form()


def create_section(parent, title, description, detail_command, static_image_path):
    section_frame = ttk.Frame(parent, padding=10, relief="solid", borderwidth=1)
    section_frame.pack(fill="x", pady=10)

    # Load and display the static image on the left
    static_image = Image.open(static_image_path)
    static_image = static_image.resize((100, 100))  # Resize image as needed
    static_image = ImageTk.PhotoImage(static_image)
    static_image_label = ttk.Label(section_frame, image=static_image)
    static_image_label.image = static_image  # Keep a reference to avoid garbage collection
    static_image_label.pack(side="left", padx=10, pady=10)

    section_text_frame = ttk.Frame(section_frame)
    section_text_frame.pack(side="left", fill="x", expand=True)

    section_label = ttk.Label(section_text_frame, text=title, font=("Arial", 18, "bold"))
    section_label.pack(anchor="w")

    section_desc = ttk.Label(section_text_frame, text=description, font=("Arial", 12))
    section_desc.pack(anchor="w")

    # Load the hover image
    hover_image = Image.open(hover_image_path)
    hover_image = hover_image.resize((100, 100))  # Resize image as needed
    hover_image = ImageTk.PhotoImage(hover_image)

    # Create a Label for the hover image (initially hidden)
    hover_image_label = ttk.Label(section_frame, image=hover_image)
    hover_image_label.image = hover_image  # Keep a reference to avoid garbage collection

    # Make the hover image clickable
    hover_image_label.bind("<Button-1>", lambda e: detail_command())

    def on_enter(event):
        hover_image_label.pack(side="right", padx=10, pady=10)

    def on_leave(event):
        hover_image_label.pack_forget()

    section_frame.bind("<Enter>", on_enter)
    section_frame.bind("<Leave>", on_leave)


# Main application window
root = tk.Tk()
root.title("Personalized Education Platform")
root.geometry("1000x700")  # Increased window size




# Centered Header (Static and Properly Centered)
header_frame = tk.Frame(root, bg="#006666")
header_frame.pack(fill="x", side="top")

header_label = ttk.Label(header_frame, text="UNIQUE MINDS CONNECT", font=("Comic Sans MS", 28, "bold"), background="#006666",
                         foreground="white", padding=20)
header_label.pack()

# Create a Frame for the scrollable area
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Add a Canvas and a Scrollbar
canvas = tk.Canvas(main_frame)
scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a Frame inside the Canvas
scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

# Add the Frame to the Canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

# Move the canvas into the main frame
canvas.master = main_frame

# Create a Frame below the header for the scrollable content
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=True)

# Move the canvas into the content frame
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Create a frame for the large image on the right side of the main frame
large_image_frame = tk.Frame(main_frame, padx=10, pady=10)
large_image_frame.pack(side="right", fill="y", padx=10)

# Load and display the large image on the right
large_image = Image.open(large_image_path)
large_image = large_image.resize((500, 500))  # Resize image as needed
large_image = ImageTk.PhotoImage(large_image)
large_image_label = ttk.Label(large_image_frame, image=large_image)
large_image_label.image = large_image  # Keep a reference to avoid garbage collection
large_image_label.pack()

# Sections with different static images
sections = [
    ("Adaptive Learning Paths", "Discover courses that adapt to your learning pace and style.",create_main_window, adaptive_image_path),
    ("Personalized Assessments", "Take assessments that are customized to your strengths.",
     open_personalized_assessments_window, assessment_image_path),
    ("Supportive Resources", "Access resources to support your learning journey.", open_supportive_resources_window,
     supportive_resources_image_path),
    ("Gamified Learning", "Engage with interactive, game-based learning experiences.", open_gamified_learning_window,
     gamified_learning_image_path),
    ("Feedback", "Provide and receive feedback to enhance the learning process.", open_feedback_window,
     feedback_image_path),
]


for title, description, detail_command, image_path in sections:
    create_section(scrollable_frame, title, description, detail_command, image_path)

# Footer
footer_label = ttk.Label(root, text="© 2024 Personalized Education Platform. All rights reserved.", font=("Arial", 12),
                         background="#004d4d", foreground="white", padding=10)
footer_label.pack(fill="x", side="bottom")

# Enable smooth scrolling with mouse wheel
def view_scroll(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

canvas.bind_all("<MouseWheel>", view_scroll)


# Run the application
root.mainloop()