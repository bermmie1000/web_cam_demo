import streamlit as st

# from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
# import av
# import cv2
# import numpy as np
# from PIL import Image

st.set_page_config(layout="wide")
st.title("고품질 이미지 캡처")


# img = st.camera_input(label="h", key="h")
# if img:
#     st.image(img)
#     image = Image.open(img)
#     w, h = image.size
#     st.write(w, h)


# class VideoTransformer(VideoTransformerBase):
#     def __init__(self):
#         self.image = None
#         self.capture = False

#     def transform(self, frame):
#         img = frame.to_ndarray(format="bgr24")
#         if self.capture:
#             self.image = img
#             self.capture = False
#         return img


# ctx = webrtc_streamer(
#     key="example",
#     video_transformer_factory=VideoTransformer,
#     media_stream_constraints={
#         "video": {"width": 1280},
#         "audio": False,
#     },
#     video_html_attrs={
#         "style": {"width": "100%", "margin": "0 auto"},
#         "autoPlay": True,
#         "controls": False,
#         "muted": True,
#     },
# )

# if ctx.video_transformer:
#     if st.button("사진 찍기"):
#         ctx.video_transformer.capture = True

#         # 이미지를 받을 때까지 대기
#         while ctx.video_transformer.capture:
#             pass

#         img = ctx.video_transformer.image

#         if img is not None:
#             st.image(img, channels="BGR", caption="캡처된 이미지")
#             st.write(f"이미지 해상도: {img.shape[1]}x{img.shape[0]}")
#             # 이미지 저장 또는 추가 처리 가능
#     else:
#         st.write("사진 찍기 버튼을 눌러 이미지를 캡처하세요.")


st.title("카메라 제어 예제")

html_code = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <!-- 뷰포트 메타 태그 추가로 모바일 환경에서도 반응형으로 동작 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <body>
    <p><video id="cameraview" width="100%" autoplay playsinline></video></p>
    <div style="text-align: center;">
      <button id="openBtn">카메라 켜기</button>
      <button id="closeBtn">카메라 끄기</button>
    </div>
  </body>
  <script>
    var streamVideo;
    if(!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia )
    {
        alert("Media Device not supported");
    } else {
      document.getElementById("openBtn").addEventListener('click', openCamera);
      document.getElementById("closeBtn").addEventListener('click', closeCamera);
      // 페이지 로드 시 자동으로 카메라 켜기
      window.addEventListener('load', openCamera);
    }

    function openCamera() {
      closeCamera();
      navigator.mediaDevices.getUserMedia({
        video: {
          width: { ideal: 4096 },
          height: { ideal: 2160 },
          facingMode: "environment"  // 후면 카메라 사용 (모바일 디바이스에서)
        },
        audio: false
      }).then(stream => {
        streamVideo = stream;
        var cameraView = document.getElementById("cameraview");
        cameraView.srcObject = stream;
        cameraView.play();
      }).catch(error => {
        console.error("카메라 접근 오류:", error);
        alert("카메라에 접근할 수 없습니다.");
      });
    }

    function closeCamera() {
      if (streamVideo) {
        var tracks = streamVideo.getTracks();
        tracks.forEach(track => track.stop());
        streamVideo = null;
        var cameraView = document.getElementById("cameraview");
        cameraView.srcObject = null;
      }
    }
  </script>
</html>
"""

# height 파라미터를 적절히 설정하여 컴포넌트 높이 조절
st.components.v1.html(html_code, height=3000)
