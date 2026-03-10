from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re  # 정규표현식 사용을 위해 추가

def practice_lms_automation():
    # 1. 크롬 브라우저 실행
    options = webdriver.ChromeOptions()
    # 사용자가 직접 제어하는 느낌을 주기 위해 브라우저 자체 음소거는 사용하지 않습니다.
    # options.add_argument("--mute-audio")
    options.add_argument("--window-size=1280,720")  # 창 크기 고정 (버튼 가림 방지)
    driver = webdriver.Chrome(options=options)
    # 2. 강의 목록이 있는 URL (새로고침할 때도 이 URL을 사용합니다)
    target_url = "https://portal.huss.ac.kr/lms_st/lctr/lctrMngr/sbjAll"
    driver.get(target_url)

    # 3. 직접 로그인 대기
    print("브라우저에서 직접 로그인을 완료하고 강의 목록 페이지로 이동해주세요.")
    print("로그인을 완료한 후, LMS -> 강의 바로가기 -> 학습하기 페이지로 접속해주세요")
    print("페이지에 강의들 수강하기 버튼 ('강의보기(view on)')이 보여야 합니다.")
    input("엔터(Enter) 키를 누르면 강의 자동화 연습을 시작합니다...")
    print("강의 자동화 연습을 시작합니다...")

    try:
        # 최초 미수강 강의 개수 파악
        initial_buttons = driver.find_elements(By.CSS_SELECTOR, "a.view.on")
        total_lectures = len(initial_buttons)
        print(f"총 {total_lectures}개의 미수강 강의를 발견했습니다.")

        # 4. 강의 개수만큼 반복해서 실행
        for i in range(total_lectures):
            print(f"\n--- [ {i + 1} / {total_lectures} ] 번째 강의 처리 시작 ---")

            # 💡 새로고침 후 시스템(Vue.js)이 준비될 시간을 명시적으로 줍니다.
            time.sleep(5)

            # 매번 새로 '강의보기(view on)' 버튼 목록을 가져옵니다.
            current_buttons = WebDriverWait(driver, 15).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.view.on"))
            )

            # 리스트가 비어있지 않다면, 항상 '남아있는 것 중 첫 번째(0)'를 클릭합니다.
            if len(current_buttons) == 0:
                print("더 이상 들을 강의가 없습니다.")
                break

            # 스크롤 이동 후 클릭 (안정성 증가)
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", current_buttons[0])
            time.sleep(1)

            # 모달 창 열기
            driver.execute_script("arguments[0].click();", current_buttons[0])
            print("강의보기 버튼을 클릭하여 모달창을 엽니다.")
            time.sleep(3) # 모달 창 뜰 때까지 대기

            # 💡 모달 창 안의 <video> 태그 자체가 로딩될 때까지 확실히 대기
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "video.vjs-tech"))
                )
                time.sleep(3) # 비디오 태그가 생겼어도 플레이어가 초기화될 시간 3초 부여
            except Exception as e:
                print("⚠️ 비디오 플레이어 로딩이 지연되고 있습니다.")

            # 5. 재생 버튼 클릭
            try:
                # 큰 재생 버튼이 화면에 '보일 때까지' 대기
                play_button = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, "button.vjs-big-play-button"))
                )

                # JS 강제 클릭 대신 가급적 정상적인 사람의 클릭을 유도
                try:
                    play_button.click()
                except:
                    driver.execute_script("arguments[0].click();", play_button)

                print("▶️ 재생 버튼을 성공적으로 눌렀습니다!")

                # (보완) 더 자연스러운 음소거를 위해 플레이어의 음소거 버튼을 클릭합니다.
                try:
                    mute_button = WebDriverWait(driver, 5).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.vjs-mute-control"))
                    )
                    # 음소거가 이미 되어있는지 확인 (vjs-vol-0 클래스가 있으면 음소거 상태)
                    if "vjs-vol-0" not in mute_button.get_attribute("class"):
                        mute_button.click()
                        print("🤫 음소거 버튼을 클릭했습니다.")
                    else:
                        print("🤫 이미 음소거 상태입니다.")
                except Exception:
                    print("⚠️ 음소거 버튼을 찾지 못했습니다.")
            except Exception as e:
                print("⚠️ 재생 버튼을 찾지 못했거나 이미 자동 재생 중입니다.")

            # 6. 실시간 시간 체크
            print("강의 진행 시간을 모니터링합니다...")
            while True:
                try:
                    # 텍스트 가져오기 (예: "학습진행시간 : 5분 / 33분")
                    time_element = driver.find_element(By.CSS_SELECTOR, "div.d_ing")
                    time_text = time_element.text

                    # 정규표현식으로 숫자만 추출
                    numbers = re.findall(r'\d+', time_text)

                    if len(numbers) >= 2:
                        current_time = int(numbers[0])
                        total_time = int(numbers[1])

                        print(f"현재 학습 상태: {current_time}분 / {total_time}분")

                        # 목표 시간에 도달했는지 확인
                        if current_time >= total_time:
                            print("✅ 강의 시간을 모두 채웠습니다!")
                            break  # while 루프 탈출

                except Exception as e:
                    print("시간 정보를 찾는 중...")

                # 90초마다 현재 수강 시간을 체크합니다.
                time.sleep(90)

            # 7. '학습종료' 버튼 찾아 누르기
            try:
                close_btn = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '학습종료')]"))
                )
                driver.execute_script("arguments[0].click();", close_btn)
                print("⏹️ 학습종료 버튼을 누르고 모달 창을 닫았습니다.")

                # 혹시 종료 알림창(Alert)이 뜨면 확인을 눌러줍니다.
                try:
                    WebDriverWait(driver, 3).until(EC.alert_is_present())
                    alert = driver.switch_to.alert
                    print(f"팝업 메시지 확인: {alert.text}")
                    alert.accept()
                    print("알림창을 닫았습니다.")
                except Exception as e:
                    pass

            except Exception as e:
                print("⚠️ 학습종료 버튼을 찾지 못했습니다. 수동 확인이 필요합니다.")

            # 서버에 학습 완료 데이터가 안전하게 넘어갈 시간을 줍니다.
            time.sleep(3)

            # 8. 확실한 새로고침을 위해 해당 페이지 URL로 다시 접속합니다.
            print("🔄 학습 상태 갱신을 위해 페이지를 다시 불러옵니다.")
            driver.get(target_url)

            # 새로고침 후 페이지 렌더링을 위해 넉넉히 대기합니다.
            time.sleep(3)

        print("\n🎉 모든 강의 자동화 연습이 성공적으로 완료되었습니다!")

    except KeyboardInterrupt:
        print("\n🛑 사용자에 의해 스크립트가 중단되었습니다.")

    except Exception as e:
        print(f"\n❌ 에러가 발생했습니다: {e}")

    finally:
        print("브라우저를 종료합니다.")
        driver.quit()

if __name__ == "__main__":
    practice_lms_automation()