import streamlit as st
from PIL import Image

def image_info(image):
    # Get image size
    width, height = image.size

    # Get image format
    img_format = image.format

    # Get image mode
    img_mode = image.mode

    return width, height, img_format, img_mode

def main():
    st.title("Image Uploader and Information Viewer")

    # Upload image file
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.subheader("Uploaded Image:")
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Get image information
        width, height, img_format, img_mode = image_info(img)

        # Display image information
        st.subheader("Image Information:")
        st.write(f"Width: {width}px")
        st.write(f"Height: {height}px")
        st.write(f"Format: {img_format}")
        st.write(f"Mode: {img_mode}")

if __name__ == "__main__":
    main()
