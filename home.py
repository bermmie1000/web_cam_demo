import sys
import streamlit as st

sys.path.append("../web_cam_demo")

from camera import camera_module

st.title("Home")

camera_module()
