import streamlit as st
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import base64
import matplotlib as plt
from functions_file import *
import streamlit_webrtc
from streamlit_webrtc import webrtc_streamer
import requests

st.title("My TrAiner")
exercise = st.selectbox("Choose exercise" , ("none","squat","knee extention","foot ankel extention"))

if (exercise == "none"):
    st.header("Please Choose an exercise")

elif (exercise == "squat"):
   video = open('/Users/ahmedbawazeer/Downloads/squat.mp4' , 'rb')
   video_bytes = video.read()
   st.video(video_bytes)
   st.header("Your Trun :)")
   # webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
   train = myTrAiner(exercise)

elif (exercise == "knee extention"):
   video = open('/Users/ahmedbawazeer/Downloads/knee extention.mp4', 'rb')
   video_bytes = video.read()
   st.video(video_bytes)
   # st.camera_input(label='Your Turn :)',disabled=False)
   webrtc_streamer(key="example")


elif (exercise == "foot ankel extention"):
   st.header("Coming SOON :)")


