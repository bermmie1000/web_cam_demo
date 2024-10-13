import sys

import streamlit as st

sys.path.append("../web_cam_demo")

from camera import camera_module


st.write("# hello")

camera_module()
