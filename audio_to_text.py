from pytube import Youtube 
import os 
import pywhisper 
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st 
import time

def transcribe_video_to_text1(url):
    