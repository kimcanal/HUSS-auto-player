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

## 📦 Installation

1. **Selenium 설치**
   ```bash
   pip install selenium
   ```
   > **Tip:** 최신 Selenium 버전은 드라이버를 자동으로 관리합니다. 먼저 `python huss_auto.py`를 실행해보고, 오류가 발생하거나 Chrome이 실행되지 않을 경우에만 2번 과정을 진행하세요.

2. **ChromeDriver 다운로드**
   - [ChromeDriver 다운로드 페이지](https://chromedriver.chromium.org/)
   - *주의: 사용 중인 Chrome 브라우저 버전에 맞는 드라이버를 설치해야 합니다.*

---

## 🚀 Usage

스크립트를 실행하면 다음 순서로 동작합니다:

1. 크롬 브라우저 실행
2. HUSS LMS 강의 목록 페이지 접속
3. **사용자가 직접 로그인**
4. 엔터 입력 후 자동화 시작

**실행 명령어:**
```bash
python huss_auto.py
```

**중단 명령어**
Ctrl + C 를 눌러 프로그램을 종료합니다


**로그인 대기:**
로그인 후 터미널에 다음 메시지가 나타나면 `Enter`를 누르세요.

> 브라우저에서 직접 로그인을 완료하고 강의 목록 페이지로 이동해주세요.
> 로그인을 완료한 후, LMS -> 학습하기 페이지까지 진입한 후 엔터(Enter) 키를 누르면 강의 자동화 연습을 시작합니다...
> ![Screenshot 2026-03-10 at 13 43 06](https://github.com/user-attachments/assets/c13c542a-950a-42e0-865a-7a779393094b)
> 반드시 위와 같은 화면 진입 후, Enter 키를 눌러야 정상작동하게 됩니다.


---

## ⚙️ How it Works

**자동화 흐름**

1. 📂 **강의 목록 페이지 접속**
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

> **주의사항**
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
