from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from keras.models import load_model
from PIL import Image
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

cnn=0

def get_prediction(img):
    dimension = 224
    channels = 3
    
    arr = np.ndarray(shape=(1, dimension, dimension, channels), dtype=np.float32)
    image = img

    size = (dimension, dimension)
    image = image.resize(size)

    image_array = np.asarray(image)
    arr[0] = (image_array.astype(np.float32) / 127.0) - 1

    return cnn.predict(arr)

if __name__ == '__main__':
        st.title('Welcome To CAC APP WORK PLEASE!')

        file = st.file_uploader('Upload An Image')
        if file:  # if user uploaded file   
               cnn = load_model('v4_melanoma')
               img = Image.open(file)
               prediction = get_prediction(img)
               if prediction[0] < 0.5:
                    st.write("Melanoma")
               else:
                    st.write("Not Melanoma")
