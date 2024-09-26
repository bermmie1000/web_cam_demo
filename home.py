import streamlit as st

st.title("카메라 이미지 캡처 예제")

html_code = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      video, canvas {
        width: 100%;
        max-width: 100%;
      }
      #button-container {
        text-align: center;
        margin-top: 10px;
      }
      #downloadBtnContainer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        background-color: white;
        padding: 10px;
        display: none; /* 초기에는 숨김 */
        z-index: 999; /* 다른 요소 위에 표시되도록 */
      }
      #downloadBtn {
        padding: 8px 16px;
        background-color: #4CAF50; /* 원하는 색상 */
        color: white;
        text-decoration: none;
        border-radius: 4px;
      }
      #downloadBtn:hover {
        background-color: #45a049;
      }
    </style>
  </head>
  <body>
    <video id="cameraview" autoplay playsinline></video>
    <canvas id="canvas" style="display: none;"></canvas>
    <div id="button-container">
      <button id="captureBtn">사진 찍기</button>
    </div>
    <!-- 다운로드 버튼 컨테이너를 추가 -->
    <div id="downloadBtnContainer">
      <a id="downloadBtn">다운로드</a>
    </div>
  </body>
  <script>
    var streamVideo;
    var cameraView = document.getElementById("cameraview");
    var canvas = document.getElementById("canvas");
    var captureBtn = document.getElementById("captureBtn");
    var downloadBtn = document.getElementById("downloadBtn");
    var downloadBtnContainer = document.getElementById("downloadBtnContainer");

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
      canvas.style.display = "block";
      var context = canvas.getContext('2d');
      canvas.width = cameraView.videoWidth;
      canvas.height = cameraView.videoHeight;
      context.drawImage(cameraView, 0, 0, canvas.width, canvas.height);

      // 캡처된 이미지를 다운로드 버튼에 연결
      var dataURL = canvas.toDataURL('image/png');
      downloadBtn.href = dataURL;
      downloadBtn.download = 'captured_image.png';
      downloadBtnContainer.style.display = "block"; // 다운로드 버튼 컨테이너를 표시
    });
  </script>
</html>
"""

st.components.v1.html(html_code, height=800)
