import tkinter as tk
from tkinter import ttk

class FeedbackForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Feedback Form")
        self.root.geometry("400x300")

        # Create and place the widgets
        tk.Label(root, text="Feedback Form", font=("Arial", 18, "bold")).pack(pady=10)

        tk.Label(root, text="Name:").pack(anchor="w", padx=10)
        self.name_entry = tk.Entry(root, width=50)
        self.name_entry.pack(padx=10, pady=5)

        tk.Label(root, text="Email:").pack(anchor="w", padx=10)
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.pack(padx=10, pady=5)

        tk.Label(root, text="Comments:").pack(anchor="w", padx=10)
        self.comments_text = tk.Text(root, width=50, height=5)
        self.comments_text.pack(padx=10, pady=5)

        # Submit button positioned directly under the form
        submit_button = tk.Button(root, text="Submit", command=self.submit_feedback)
        submit_button.pack(padx=10, pady=10)  # Added padx and pady for spacing

    def submit_feedback(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        comments = self.comments_text.get("1.0", tk.END).strip()

        # For demonstration, we're just printing the feedback to the console
        print("Feedback Submitted:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Comments: {comments}")

        # Clear the form after submission
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.comments_text.delete("1.0", tk.END)

def create_feedback_form():
    root = tk.Tk()
    app = FeedbackForm(root)
    root.mainloop()

# Run this file directly to start the form
if __name__ == "__main__":
    create_feedback_form()
