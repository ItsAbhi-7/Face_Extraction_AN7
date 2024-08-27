from retinaface import RetinaFace
import streamlit as st
import numpy as np
import tempfile
import os
import io
from PIL import Image
import warnings
warnings.filterwarnings('ignore')

st.title("Face Extraction")
uploaded_file=st.file_uploader("Upload a photo",type=["jpg","png","jpeg"])


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    image = image.convert('RGB')
    with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
        image.save(tmp_file, format='JPEG')
        tmp_file_path = tmp_file.name
    image_np=np.array(image)
    faces = RetinaFace.extract_faces(img_path=image_np)
    os.remove(tmp_file_path)
    if faces:
        for i, face in enumerate(faces):
            st.image(face,caption=f'Face {i+1}')
    else:
        st.write("No face detected.")
else:
    st.write("Please upload an image file")