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
    </style>
  </head>
  <body>
    <video id="cameraview" autoplay playsinline></video>
    <canvas id="canvas" style="display: none;"></canvas>
    <div id="button-container">
      <button id="captureBtn">사진 찍기</button>
      <button id="downloadBtn" style="display: none;">다운로드</button>
    </div>
  </body>
  <script>
    var streamVideo;
    var cameraView = document.getElementById("cameraview");
    var canvas = document.getElementById("canvas");
    var captureBtn = document.getElementById("captureBtn");
    var downloadBtn = document.getElementById("downloadBtn");

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
      canvas.toBlob(function(blob) {
        var url = URL.createObjectURL(blob);
        downloadBtn.href = url;
        downloadBtn.download = 'captured_image.png';
        downloadBtn.style.display = "inline";
      }, 'image/png');
    });
  </script>
</html>
"""

st.components.v1.html(html_code, height=700)
