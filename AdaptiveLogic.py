import tkinter as tk
from PIL import Image, ImageTk, ImageDraw


class DrawingApp:
    def __init__(self, root, image_paths):
        self.root = root

        # Define the image sizes
        self.image_size = (250, 250)  # Resize images to 500x500
        self.large_image_size = (500, 500)  # Size for the enlarged image

        # Create a frame for the heading
        self.heading_frame = tk.Frame(root)
        self.heading_frame.pack(fill=tk.X, padx=20, pady=(20, 10))

        # Create the heading label
        self.heading_label = tk.Label(self.heading_frame, text="Canvas Images", font=("Arial", 20, "bold"))
        self.heading_label.pack()

        # Create a frame to hold images and buttons
        self.image_frame = tk.Frame(root)
        self.image_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Create a frame to show enlarged images
        self.enlarged_frame = tk.Frame(root)
        self.enlarged_frame.pack_forget()  # Initially hidden

        # Dictionary to hold image references
        self.images = []
        self.current_image_index = None
        self.original_image = None  # Store the original image for clearing

        # Default pen color
        self.pen_color = "black"

        # Load images and create buttons
        self.load_images(image_paths)

    def load_images(self, image_paths):
        self.frames = []  # To hold frames for each image and button

        for index, path in enumerate(image_paths):
            try:
                # Load and resize image
                image = Image.open(path)
                image_resized = image.resize(self.image_size)  # Resize images to 500x500
                image_tk = ImageTk.PhotoImage(image_resized)

                # Save image reference
                self.images.append((image, image_tk))

                # Create a frame for each image and its button
                frame = tk.Frame(self.image_frame)
                frame.pack(side=tk.LEFT, padx=20, pady=20)

                # Image label
                label = tk.Label(frame, image=image_tk)
                label.image = image_tk  # Keep a reference to avoid garbage collection
                label.pack()

                # Button below the image
                button = tk.Button(frame, text=f"Show Image {index + 1}", font=("Arial", 12), command=lambda i=index: self.on_button_click(i))
                button.pack(pady=10)

                # Save the frame reference
                self.frames.append(frame)

            except Exception as e:
                print(f"Error loading image {path}: {e}")

    def create_color_palette(self):
        # Create a frame for color palette
        self.color_palette_frame = tk.Frame(self.enlarged_frame)
        self.color_palette_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

        # Define colors
        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "brown"]
        for color in colors:
            color_button = tk.Button(self.color_palette_frame, bg=color, width=4, height=2, command=lambda c=color: self.set_pen_color(c))
            color_button.pack(pady=5)

    def set_pen_color(self, color):
        self.pen_color = color

    def on_button_click(self, index):
        print(f"Button {index + 1} clicked")
        self.show_enlarged_image(index)

    def show_enlarged_image(self, index):
        # Hide the image frame
        self.image_frame.pack_forget()

        # Show the enlarged frame
        self.enlarged_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Clear the enlarged frame
        for widget in self.enlarged_frame.winfo_children():
            widget.destroy()

        # Load and resize image for enlarged view
        self.current_image_index = index
        self.original_image = self.images[index][0].copy()  # Save the original image
        image_enlarged = self.original_image.resize(self.large_image_size)  # Resize to larger size
        image_tk_enlarged = ImageTk.PhotoImage(image_enlarged)

        # Create a canvas for drawing
        self.canvas = tk.Canvas(self.enlarged_frame, width=self.large_image_size[0], height=self.large_image_size[1])
        self.canvas.pack(side=tk.LEFT)

        # Create a label for the enlarged image
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk_enlarged)
        self.canvas.image = image_tk_enlarged  # Keep a reference to avoid garbage collection

        # Create a drawing object for the enlarged image
        self.draw = ImageDraw.Draw(self.original_image)

        # Bind mouse events for drawing
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Create a color palette
        self.create_color_palette()

        # Back button to return to the main view
        back_button = tk.Button(self.enlarged_frame, text="Back", font=("Arial", 14), command=self.show_main_view)
        back_button.pack(side=tk.LEFT, padx=10, pady=20)  # Add padding for visibility

        # Clear drawing button
        clear_button = tk.Button(self.enlarged_frame, text="Clear Drawing", font=("Arial", 14), command=self.clear_drawing)
        clear_button.pack(side=tk.LEFT, padx=10, pady=20)  # Add padding for visibility

    def paint(self, event):
        if self.old_x and self.old_y:
            x, y = event.x, event.y
            self.canvas.create_line(self.old_x, self.old_y, x, y, width=3, fill=self.pen_color, capstyle=tk.ROUND, smooth=tk.TRUE)
            self.draw.line([self.old_x, self.old_y, x, y], fill=self.pen_color, width=3)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def clear_drawing(self):
        # Redraw the original image without any drawing
        self.original_image = self.images[self.current_image_index][0].copy()  # Reload original image
        image_enlarged = self.original_image.resize(self.large_image_size)  # Resize to larger size
        image_tk_enlarged = ImageTk.PhotoImage(image_enlarged)

        # Update the canvas with the cleared image
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=image_tk_enlarged)
        self.canvas.image = image_tk_enlarged  # Keep a reference to avoid garbage collection

        # Recreate drawing object
        self.draw = ImageDraw.Draw(self.original_image)

    def show_main_view(self):
        # Hide the enlarged frame
        self.enlarged_frame.pack_forget()

        # Show the image frame
        self.image_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
# Main application window
# Main application window

def start(baseRoot):
    print("Starting application...")
    # baseRoot.destroy()
    root = tk.Toplevel()

    root.geometry("1200x600")  # Adjusted window size to fit larger images and buttons
    # Image paths
    image_paths = [
        r"C:\Users\Tarneet singh\OneDrive\Pictures\Camera Roll\222.jpg",
        r"C:\Users\Tarneet singh\OneDrive\Pictures\Camera Roll\333.jpg",
        r"C:\Users\Tarneet singh\OneDrive\Pictures\Camera Roll\444.jpg",
        r"C:\Users\Tarneet singh\OneDrive\Pictures\Camera Roll\666.jpg"
    ]

    # Start the Drawing App
    app = DrawingApp(root, image_paths)

    # root.mainloop()


if __name__ == '__main__':
    start()