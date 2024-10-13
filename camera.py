import sys
import uuid
import time
import requests

import streamlit as st

sys.path.append("../productlens_pilot")


def _init_session_state():
    if "detect_result" not in st.session_state:
        st.session_state.detect_result = None


def camera_module():
    """
    카메라 모듈
    카메라 입력을 받은 이미지를 API 서버에 전송하고, 인식 결과를 반환합니다.
    """
    _init_session_state()

    # api_url = "http://127.0.0.1:5000"
    api_url = "https://lse-lens-api-cdezeba2c4f5g8f9.koreacentral-01.azurewebsites.net"

    uuid = _generate_uuid()

    get_camera_input_and_post_image(uuid, api_url)

    st.session_state.detect_result = get_object_detection_response(uuid, api_url)


def _generate_uuid():
    return str(uuid.uuid4())


def get_camera_input_and_post_image(uuid: str, api_url: str):
    """
    카메라 입력을 받습니다.
    - 카메라 입력을 받는 코드를 작성합니다.
    """
    html_code = _load_html("src/camera/camera.html")
    html_code = html_code.replace("{{uuid}}", uuid)
    html_code = html_code.replace("{{api_url}}", api_url)

    st.components.v1.html(html_code, height=800, scrolling=True)


def _load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# ------------------------------------------------------------------
def get_object_detection_response(
    uuid: str,
    api_url: str,
    retries: int = 100,
    delay: int = 3,
) -> str:
    """
    객체 검출 결과를 요청합니다.
    - uuid: 검색할 UUID
    - retries: 최대 시도 횟수 (default: 10)
    - delay: 각 시도 간 대기 시간(초) (default: 3)

    UUID가 존재하면 item_code를 반환하고, 최대 시도 횟수를 초과하면 None을 반환합니다.
    """
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(
                f"{api_url}/object_detection",
                params={"uuid": uuid},
                timeout=5,
            )
            if response.status_code == 200:
                data = response.json()
                item_code = data.get("item_code")

                if item_code:
                    print(f"아이템 코드 발견: {item_code} (시도 {attempt}회)")
                    return item_code

            elif response.status_code == 404:
                print(f"시도 {attempt}회: UUID를 찾지 못했습니다. 다시 시도합니다...")

            else:
                data = response.json()
                print(f"시도 {attempt}회: 예상치 못한 응답 - {data}")

        except requests.RequestException as e:
            print(f"시도 {attempt}회: 요청 중 오류 발생 - {e}")

        if attempt < retries:
            time.sleep(delay)  # 지정된 간격만큼 대기
    print("UUID를 찾는 데 실패했습니다.")

    return None
