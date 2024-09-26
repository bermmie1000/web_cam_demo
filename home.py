import streamlit as st

st.title("카메라 제어 예제")

html_code = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <!-- 뷰포트 메타 태그 추가로 모바일 환경에서도 반응형으로 동작 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
      body, html {
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden;
      }
      #cameraview {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 1;
      }
      #button-container {
        position: fixed;
        bottom: 20px;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 2;
      }
      #button-container button {
        margin: 0 10px;
        padding: 15px 25px;
        font-size: 16px;
        border: none;
        border-radius: 5px;
        background-color: #007bff;
        color: white;
        cursor: pointer;
      }
      #button-container button:active {
        background-color: #0056b3;
      }
      #capturedImage {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: none;
        z-index: 1;
      }
    </style>
  </head>
  <body>
    <video id="cameraview" autoplay playsinline></video>
    <img id="capturedImage" />
    <div id="button-container">
      <button id="captureBtn">사진 찍기</button>
      <button id="downloadBtn" style="display: none;">다운로드</button>
      <button id="retakeBtn" style="display: none;">다시 찍기</button>
    </div>
    <canvas id="canvas" style="display: none;"></canvas>
  </body>
  <script>
    var streamVideo;
    var cameraView = document.getElementById("cameraview");
    var capturedImage = document.getElementById("capturedImage");
    var captureBtn = document.getElementById("captureBtn");
    var downloadBtn = document.getElementById("downloadBtn");
    var retakeBtn = document.getElementById("retakeBtn");
    var canvas = document.getElementById("canvas");
    var capturedImageDataURL = '';

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
          facingMode: "environment"  // 후면 카메라 사용 (모바일 디바이스에서)
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

    function closeCamera() {
      if (streamVideo) {
        var tracks = streamVideo.getTracks();
        tracks.forEach(track => track.stop());
        streamVideo = null;
        cameraView.srcObject = null;
      }
    }

    captureBtn.addEventListener('click', () => {
      canvas.width = cameraView.videoWidth;
      canvas.height = cameraView.videoHeight;
      var context = canvas.getContext('2d');
      context.drawImage(cameraView, 0, 0, canvas.width, canvas.height);

      // 이미지 데이터 저장
      capturedImageDataURL = canvas.toDataURL('image/png');

      // 캡처된 이미지 표시
      capturedImage.src = capturedImageDataURL;
      capturedImage.style.display = 'block';

      // 버튼 상태 변경
      captureBtn.style.display = 'none';
      downloadBtn.style.display = 'inline-block';
      retakeBtn.style.display = 'inline-block';
    });

    downloadBtn.addEventListener('click', () => {
      if (capturedImageDataURL) {
        var link = document.createElement('a');
        link.href = capturedImageDataURL;
        link.download = 'captured_image.png';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
      }
    });

    retakeBtn.addEventListener('click', () => {
      capturedImage.style.display = 'none';
      captureBtn.style.display = 'inline-block';
      downloadBtn.style.display = 'none';
      retakeBtn.style.display = 'none';
    });
  </script>
</html>
"""

# height 파라미터를 적절히 설정하여 컴포넌트 높이 조절
st.components.v1.html(html_code, height=600)
