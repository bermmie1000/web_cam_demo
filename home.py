import streamlit as st

st.title("카메라 이미지 캡처 예제")

html_code = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      video, canvas, img {
        width: 100%;
        max-width: 100%;
      }
      #button-container {
        text-align: center;
        margin-top: 10px;
      }
      #message {
        text-align: center;
        margin-top: 10px;
        font-size: 16px;
      }
    </style>
  </head>
  <body>
    <video id="cameraview" autoplay playsinline></video>
    <canvas id="canvas" style="display: none;"></canvas>
    <div id="button-container">
      <button id="captureBtn">사진 찍기</button>
    </div>
    <img id="capturedImage" style="display: none; margin-top: 10px;" />
    <div id="message" style="display: none;">
      이미지를 길게 눌러 저장하세요.
    </div>
  </body>
  <script>
    var streamVideo;
    var cameraView = document.getElementById("cameraview");
    var canvas = document.getElementById("canvas");
    var captureBtn = document.getElementById("captureBtn");
    var capturedImage = document.getElementById("capturedImage");
    var message = document.getElementById("message");

    if(!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia )
    {
        alert("Media Device not supported");
    } else {
      openCamera();
    }

    function openCamera() {
      navigator.mediaDevices.getUserMedia({
        video: {
          width: { ideal: 4096 },
          height: { ideal: 2160 },
          facingMode: "environment"
        },
        audio: false
      }).then(stream => {
        streamVideo = stream;
        cameraView.srcObject = stream;
      }).catch(error => {
        console.error("카메라 접근 오류:", error);
        alert("카메라에 접근할 수 없습니다.");
      });
    }

    captureBtn.addEventListener('click', () => {
      canvas.style.display = "none";
      var context = canvas.getContext('2d');
      canvas.width = cameraView.videoWidth;
      canvas.height = cameraView.videoHeight;
      context.drawImage(cameraView, 0, 0, canvas.width, canvas.height);

      // 캡처된 이미지를 이미지 태그에 표시
      var dataURL = canvas.toDataURL('image/png');
      capturedImage.src = dataURL;
      capturedImage.style.display = "block";
      message.style.display = "block";
    });
  </script>
</html>
"""

st.components.v1.html(html_code, height=200)
