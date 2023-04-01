import streamlit as st
import numpy as np 
from PIL import Image, ImageFilter


col1, col2 = st.columns([0.8,0.2])

with col1:
    st.markdown(""" <style> .font {
        font-size:35px,font-family:'Copper Black';color:#FF9633;
    }
    """,unsafe_allow_html=True)
    st.markdown('<p class="font"> Upload your photo here...</p>',unsafe_allow_html=True)
    file = st.file_uploader("",type=['png','jpg','jpeg'])


# with col2:
#     st.image()

st.sidebar.markdown('<p class="font"> Low Level Image Processing App</p>',unsafe_allow_html=True)

with st.sidebar.expander("About the App"):
    st.write("""
        This is a Simple Low level image processing app build with library Pillow, numpy, and streamlit in python. 
    """)
    

if file is not None:
    img = Image.open(file)

    col1,col2 = st.columns([0.5,0.5])
    with col1:
        st.markdown('<p style="text-align:centher;"> Before</p>',unsafe_allow_html=True)
        st.image(img,width=300)

    with col2:
        st.markdown('<p style="text-align:center;"> After</p>',unsafe_allow_html=True)
        filter = st.sidebar.radio('Play with you Image:',['Original','Gray Image','Edge','Bright','Dark','Contrast'])
        if filter == 'Gray Image':
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            st.image(gray_img,width=300)
        elif filter == "Bright":
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            shape = np_gray.shape
            img2 = np_gray.copy()
            slider = st.sidebar.slider("Adjust intensity",2,255,step=2)
            for row in range(len(np_gray)):
                for col in range(len(np_gray)):
                    img2[row][col] += slider
                    if img2[row][col] > 255:
                        img2[row][col]  = 255
            img1 = Image.fromarray(img2)
            st.image(img1,widht=300)
            
        elif filter == "Dark":
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            shape = np_gray.shape
            img2 = np_gray.copy()
            slider = st.sidebar.slider("Adjust intensity",2,255,step=2)
            for row in range(len(np_gray)):
                for col in range(len(np_gray)):
                    img2[row][col] -= slider
                    if img2[row][col] < 0:
                        img2[row][col]  = 0  
            img1 = Image.fromarray(img2)
            st.image(img1,width=300)

        elif filter == "Edge":
            gray_img = img.convert('L')
            edges = gray_img.filter(ImageFilter.FIND_EDGES)
            st.image(edges,width=300)

        elif filter == "Contrast":
            gray_img = img.convert('L')
            np_gray = np.array(gray_img)
            shape = np_gray.shape
            img2 = np_gray.copy()
            slider = st.sidebar.slider("Adjust intensity",2,255,step=2)
            for row in range(len(np_gray)):
                for col in range(len(np_gray)):
                    img2[row][col] *= slider
                    if img2[row][col] > 255 :
                        img2[row][col]  = 255
                    if img2[row][col] < 0 :
                        img2[row][col]  = 0 

            img1 = Image.fromarray(img2)
            st.image(img1,widht=300)

