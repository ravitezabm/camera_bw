import streamlit as st
from PIL import Image


with st.expander("start camera"):
    camera_image = st.camera_input("camera")
    uploaded_image = st.file_uploader("Upload Image")
if uploaded_image:
    image = Image.open(uploaded_image)
    grey_uploaded = image.convert("L")
    st.image(grey_uploaded)
if camera_image:
    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.image(gray_img)

