# 🎓 HUSS LMS Lecture Auto Player

MacOS 환경에서 정상작동 확인했습니다.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![License](https://img.shields.io/badge/License-MIT-orange)

**HUSS LMS Lecture Auto Player**는 HUSS LMS에서 강의를 수강할 때 발생하는 반복적인 작업(강의 종료 후 새로고침 → 다음 강의 클릭)을 자동화하기 위해 제작된 브라우저 자동화 스크립트입니다.

Selenium을 사용하여 강의 수강, 시간 모니터링, 다음 강의 이동을 자동으로 수행하여 학습 편의성을 높입니다.

---

## ✨ Features

- 🔍 **자동 탐색**: 미수강 강의 목록을 자동으로 확인합니다.
- ▶️ **자동 재생**: video.js 플레이어를 자동으로 재생합니다.
- ⏱️ **시간 모니터링**: 강의 진행 시간을 실시간으로 체크합니다.
- ✅ **자동 완료**: 학습 완료 시 '학습 종료' 버튼을 자동으로 클릭합니다.
- 🔄 **연속 재생**: 페이지 새로고침 후 다음 강의를 자동으로 실행합니다.
- 🏁 **자동 종료**: 모든 강의가 완료되면 스크립트가 종료됩니다.

---

## 🛠 Requirements

- Python 3.8+
- Google Chrome
- ChromeDriver
- Selenium

---

##  Virtual Environment (venv)

이 프로젝트는 Python 가상환경(venv) 사용을 권장합니다.

가상환경을 사용하면:
- 시스템 Python과 분리된 환경에서 실행할 수 있고
- 다른 프로젝트의 패키지와 충돌하는 것을 방지할 수 있습니다.
- 또한 selenium과 같은 의존성 패키지를 프로젝트별로 독립적으로 관리할 수 있습니다.

### 1️⃣ 가상환경 생성

**MacOS / Linux**
```bash
python3 -m venv venv
```

**Windows**
```bash
python -m venv venv
```

위 명령어를 실행하면 프로젝트 폴더 안에 `venv` 폴더가 생성됩니다.
이 폴더에는 Python 실행 환경과 필요한 패키지들이 설치됩니다.

### 2️⃣ 가상환경 활성화

스크립트를 실행하기 전에 반드시 가상환경을 활성화해야 합니다.

**MacOS / Linux**
```bash
source venv/bin/activate
```

**Windows**
```bash
venv\Scripts\activate
```

활성화되면 터미널 프롬프트 앞에 `(venv)` 표시가 나타납니다.

### 3️⃣ 패키지 설치

가상환경이 활성화된 상태에서 다음 명령어를 실행합니다.

```bash
pip install -r requirements.txt
```

이 명령어는 프로젝트 실행에 필요한 Python 패키지를 자동으로 설치합니다.

### 4️⃣ 스크립트 실행

```bash
python huss_auto.py
```

---

## 🚀 Usage Flow

스크립트를 실행하면 다음 순서로 동작합니다:

1. 크롬 브라우저 실행
2. HUSS LMS 강의 목록 페이지 접속
3. **사용자가 직접 로그인**
4. 엔터 입력 후 자동화 시작

**중단 명령어:**

**Ctrl + C** 를 눌러 프로그램을 종료합니다

**로그인 대기:**
로그인 후 터미널에 다음 메시지가 나타나면 `Enter`를 누르세요.

> 브라우저에서 직접 로그인을 완료하고 강의 목록 페이지로 이동해주세요.
> 로그인을 완료한 후, LMS -> 학습하기 페이지까지 진입한 후 엔터(Enter) 키를 누르면 강의 자동화 연습을 시작합니다...
> ![Screenshot 2026-03-10 at 13 43 06](https://github.com/user-attachments/assets/c13c542a-950a-42e0-865a-7a779393094b)
> 반드시 위와 같은 화면 진입 후, Enter 키를 눌러야 정상작동하게 됩니다.

---

## ⚙️ How it Works

**자동화 흐름**

1. 📂 **로그인**

   **강의 목록 페이지 접속** 은 사용자가 직접 해주셔야 합니다!!!

2. 🔍 **미수강 강의 탐색**
3. ▶️ **강의 재생**
4. ⏳ **학습 진행 시간 체크**
5. ✅ **학습 완료**
6. 🖱️ **학습 종료 버튼 클릭**
7. 🔄 **페이지 새로고침** (강의 상태 갱신)
8. ⏭️ **다음 강의 실행**

> HUSS LMS는 강의 완료 후 페이지 새로고침이 되어야 강의 상태가 갱신되기 때문에 스크립트에서는 강의 종료 후 페이지를 다시 로드합니다.

---

## ⚠️ Notes & Disclaimer

> **[주의사항]**
>
> 이 스크립트는 반복적인 UI 작업을 줄이기 위한 **자동화 예제**입니다.
>
> 강의를 실제로 시청하면서 사용해야 하며, 자리를 비운 상태에서 자동으로 강의를 수강하는 방식은 **각 교육 플랫폼의 이용 규정에 위반될 수 있습니다.**
>
> **사용자는 반드시 본인이 수강 중인 교육기관의 규정을 준수해야 합니다.**


**Disclaimer**
This project is provided for **educational and personal automation purposes only**. The author is not responsible for misuse that violates the terms of service of any platform or educational institution.

---

## 📜 License

MIT License
