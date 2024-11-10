import cv2
from fer import FER
import tkinter as tk
from tkinter import Label, Frame
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

emotion_detector = FER(mtcnn=True)
snapshot_path = "snapshot.png"
chart_path = "emotion_chart.png"

def detect_emotions(frame):
    emotions = emotion_detector.detect_emotions(frame)
    if emotions:
        return emotions[0]['emotions'], emotions[0]['box']
    return None, None


def get_dominant_emotion(emotions):
    if emotions:
        return max(emotions.items(), key=lambda item: item[1])
    return None


def save_snapshot(frame, filename):
    cv2.imwrite(filename, frame)


def plot_emotions(emotions, chart_type="bar"):
    fig, ax = plt.subplots(figsize=(4, 3))

    if chart_type == "bar":
        colors = plt.cm.Paired.colors  # Use paired colors
        ax.barh(list(emotions.keys()), list(emotions.values()), color=colors)  # Horizontal bar chart
        ax.set_xlabel('Score', fontsize=8)
        ax.set_title('Emotion Recognition Results', fontsize=10, fontweight='bold')
        ax.tick_params(axis='x', labelsize=8)
        ax.tick_params(axis='y', labelsize=8)
        ax.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout(pad=1.0)
    elif chart_type == "pie":
        ax.pie(emotions.values(), labels=emotions.keys(), autopct='%1.1f%%', colors=plt.cm.Paired.colors)
        ax.set_title('Emotion Recognition Results', fontsize=10, fontweight='bold')

    plt.savefig("emotion_chart.png", bbox_inches='tight')
    plt.savefig("snapshot.png", bbox_inches='tight')
    plt.close()


def show_report(emotions, dominant_emotion, snapshot_path):
    root = tk.Toplevel()
    root.geometry("1500x700")
    root.title("Emotion Recognition Report")
    root.configure(background='#f0f0f0')

    # Display a test label
    Label(root, text="Emotion Recognition Report", font=("Arial", 20, "bold")).pack(pady=10)

    # Create a frame for the image and text
    report_frame = Frame(root, bg='#ffffff', bd=2, relief="ridge")
    report_frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Load and display the snapshot image
    img_snapshot = ImageTk.PhotoImage(Image.open(snapshot_path))
    snapshot_label = Label(report_frame, image=img_snapshot)
    snapshot_label.image = img_snapshot  # Keep a reference to avoid garbage collection
    snapshot_label.pack(side="left", padx=10, pady=10)

    # Load and display the emotion chart image
    img_chart = ImageTk.PhotoImage(Image.open("emotion_chart.png"))
    chart_label = Label(report_frame, image=img_chart)
    chart_label.image = img_chart  # Keep a reference to avoid garbage collection
    chart_label.pack(side="right", padx=10, pady=10)

    # Add more report details as needed
    if dominant_emotion:
        dominant_emotion_text = f"Dominant Emotion: {dominant_emotion[0].capitalize()}"
        Label(report_frame, text=dominant_emotion_text, font=("Arial", 16, "bold")).pack(pady=10)

    # Update the GUI to reflect changes and then close the window
    root.update_idletasks()
    root.destroy()









cap = cv2.VideoCapture(0)


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
                cv2.rectangle(overlay, (text_x - 5, y_offset - 15), (text_x + text_size[0] + 5, y_offset + 5), (0, 0, 0),
                              -1)
                cv2.putText(frame, emotion_text, (text_x, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
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
            # show_report(emotions, dominant_emotion, snapshot_path)
            break
