import streamlit as st 
import numpy as np 
import pandas as pd
import time
from PIL import Image 

st.title("Image Editor")

raw = st.file_uploader("Upload a jpg | png image",type=['png','jpg'],accept_multiple_files=False)
if (raw):
    with Image.open(raw) as img:
        img.load()

    time.sleep(2)
    gray_img = img.convert('L')
    np_img = np.array(gray_img)
    size = np_img.size 
    shape = np_img.shape

# def bright(np_img,value):
#     img_bri = np_img.copy()
#     for row in range(0,shape[0]):
#         for col in range(0,shape[1]):
#             img_bri[row][col] += value  
#             if img_bri[row][col] > 255:
#                 img_bri[row][col] = 255

#     img2 = Image.fromarray(img_bri)
#     return img2

# def dark(np_img,value):
#     img_dar = np_img.copy()
#     for row in range(0,shape[0]):
#         for col in range(0,shape[1]):
#             img_dar[row][col] -= value  
#             if img_dar[row][col] < 0:
#                 img_dar[row][col] = 0 
    
#     img1 = Image.fromarray(img_dar)
#     return img1

if (raw):
    button1 = st.button("let's go...")
    col1,col2 = st.columns(2)
    col1.metric("Size of image ",size)
    col2.metric("Shape of image ",'x'.join(map(str,shape)))

    col3,col4 = st.columns(2)
    with col3:
        if (st.button("See Gray image")):
            st.image(gray_img)

    with col4: 
        if (st.button("Image in Array")):
            st.write(np_img)


if (raw):
    if (st.button("Manipulate the Image")):
        # value = st.number_input("Pick a number",5,255)

        st.write("Manipulation with Brightness of Image")
        col1,col2 = st.columns(2)
        with col1:
            value = st.slider("pick a number",2,255)
            st.write("Brightned Image")
            img_bri = np_img.copy()
            for row in range(0,shape[0]):
                for col in range(0,shape[1]):
                    img_bri[row][col] += value  
                    if img_bri[row][col] > 255:
                        img_bri[row][col] = 255
            img2 = Image.fromarray(img_bri)
            st.image(img2)

        with col2:
            st.write("Darken Image")
            value = st.slider("pick a number",2,255)
            img_dar = np_img.copy()
            for row in range(0,shape[0]):
                for col in range(0,shape[1]):
                    img_dar[row][col] -= value  
                    if img_dar[row][col] < 0:
                        img_dar[row][col] = 0 
            img1 = Image.fromarray(img_dar)
            st.image(img1)
