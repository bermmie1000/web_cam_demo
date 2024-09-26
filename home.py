# import streamlit as st
# from my_component import camera_component

# st.title("고화질 카메라 캡처")

# image_data = camera_component()

# if image_data:
#     st.image(image_data, caption="캡처된 이미지")


import streamlit as st


image = st.camera_input(label="카메라", key="capture")

if image:
    st.image(image)
