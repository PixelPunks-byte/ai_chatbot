import streamlit as st
from integration import integrate

st.title("Image and Message Integration")

image = st.file_uploader("Upload an image")
message = st.text_input("Enter a message")

if st.button("Submit"):
    if image is not None and message:
        response, objects = integrate(image, message)
        st.write(f"Response: {response}")
        st.write(f"Detected Objects: {objects}")
    else:
        st.write("Please upload an image and enter a message.")