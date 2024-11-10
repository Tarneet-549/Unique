import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import subprocess
import tkinter as tk

load_dotenv()

genai.configure(api_key="AIzaSyCp4dYZX3hb7OBshRZAW8xUE8rWCcAxS4Q")


prompt = """You are a specialized video summarizer for neurodiverse students. Your task is to take the transcript of the video and explain the content in simple, easy-to-understand language with clear points. Make sure the summary includes all the important concepts taught in the video and repeats key ideas for better understanding. For example, if the video is about teaching the alphabet (A, B, C, D), make sure to clearly list and explain each letter so that it’s easy for neurodiverse students to follow and learn. Use stickers and emojis for better understanding and explain everything in tabular form."""



def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
    except Exception as e:
        raise e

def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

def run_streamlit_app():
    st.title("YouTube Transcript to Detailed Notes Converter")
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if youtube_link:
        video_id = youtube_link.split("=")[1]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

    if st.button("Get Detailed Notes"):
        transcript_text = extract_transcript_details(youtube_link)
        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)

if __name__ == "__main__":
    if not os.getenv('STREAMLIT_FLAG'):
        os.environ['STREAMLIT_FLAG'] = '1'
        subprocess.Popen(["streamlit", "run", "main.py"])
    else:
        run_streamlit_app()