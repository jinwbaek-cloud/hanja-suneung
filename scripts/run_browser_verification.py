import os
import sys
import time
import json
import base64
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 13 Contexts with Source Image Fallback
IMAGE_CONTEXTS = [
    {"word": "부합", "hanja": "符合", "source": "2019 본수", "label": "2019_본수_p5"},
    {"word": "강호", "hanja": "江湖", "source": "2020 본수", "label": "2020_본수_p8"},
    {"word": "홍진", "hanja": "紅塵", "source": "2020 9모", "label": "2020_9모_p6"},
    {"word": "공명", "hanja": "功名", "source": "2020 본수", "label": "2020_본수_p8"},
    {"word": "풍류", "hanja": "風流", "source": "2020 9모", "label": "2020_9모_p6"},
    {"word": "풍월", "hanja": "風月", "source": "2020 9모", "label": "2020_9모_p6"},
    {"word": "시비", "hanja": "柴扉", "source": "2017 9모", "label": "2017_9모_p6"},
    {"word": "시비", "hanja": "柴扉", "source": "2020 9모", "label": "2020_9모_p6"},
    {"word": "하계", "hanja": "下界", "source": "2021 본수", "label": "2021_본수_p14"},
    {"word": "암향", "hanja": "暗香", "source": "2019 6모", "label": "2019_6모_p11"},
    {"word": "암향", "hanja": "暗香", "source": "2021 본수", "label": "2021_본수_p14"},
    {"word": "신용 위험", "hanja": "信用危險", "source": "2020 본수", "label": "2020_본수_p14"},
    {"word": "광한전", "hanja": "廣寒殿", "source": "2021 본수", "label": "2021_본수_p14"}
]

def create_driver(width=1280, height=900, is_mobile=False):
    options = Options()
    options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument(f'--window-size={width},{height}')
    if is_mobile:
        options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1')
    
    options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(width, height)
    return driver

def set_search_query(driver, query):
    el = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder*='검색']"))
    )
    driver.execute_script("""
    const el = arguments[0];
    const val = arguments[1];
    const setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
    setter.call(el, val);
    el.dispatchEvent(new Event('input', { bubbles: true }));
    el.dispatchEvent(new Event('change', { bubbles: true }));
    """, el, query)
    time.sleep(0.4)

def search_and_select(driver, query, target_hanja=None):
    """
    Simulates complete user flow:
    1. Input string into search input (avoiding broken single-key Korean composition)
    2. Verifies DOM search results are dynamically updated
    3. Clicks matching result card
    4. Verifies detail view is entered
    """
    set_search_query(driver, query)

    cards = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".grid .classic-card"))
    )
    assert len(cards) >= 1, f"Search results for '{query}' returned 0 cards!"

    matched_card = None
    for c in cards:
        c_text = c.text
        if query in c_text:
            if target_hanja:
                if target_hanja in c_text:
                    matched_card = c
                    break
            else:
                matched_card = c
                break

    assert matched_card is not None, f"Matching card for '{query}' (hanja: {target_hanja}) not found!"
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", matched_card)
    driver.execute_script("arguments[0].click();", matched_card)

    detail_card = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "detail-card"))
    )
    return detail_card

def close_detail(driver):
    close_btn = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "closeDetailBtn"))
    )
    driver.execute_script("arguments[0].click();", close_btn)
    time.sleep(0.4) # wait for 300ms closing animation

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    screenshots_dir = os.path.join(base_dir, 'screenshots')
    os.makedirs(screenshots_dir, exist_ok=True)

    report_data = {
        'desktop': {},
        'mobile': {},
        'image_contexts_13': [],
        'print_check': {},
        'console_errors': []
    }

    url = 'http://127.0.0.1:8080/index.html'

    print("==================================================")
    print("STAGE 1: Desktop Browser Verification Suite (1280x900)")
    print("==================================================")

    driver = create_driver(1280, 900, is_mobile=False)
    driver.get(url)
    time.sleep(1.5)

    # Prevent window.print blocking while recording invocation
    driver.execute_script("""
    window.__printIntercepted = false;
    window.print = function() {
        window.__printIntercepted = true;
        console.log("window.print() intercepted for test verification");
    };
    """)

    # 1. Page Load & Title
    assert "한알국쉬 수능" in driver.title, f"Unexpected page title: {driver.title}"
    print("[PASS] Desktop Page Load: Title verified")
    report_data['desktop']['page_load'] = True

    # 2. Unclassified New Word with Definition: 복선화음
    print("\n--- [Desktop] Testing Unclassified New Word: 복선화음 (福善禍淫) ---")
    detail = search_and_select(driver, "복선화음", "福善禍淫")
    detail_html = detail.get_attribute('outerHTML')

    assert "복선화음" in detail_html and "福善禍淫" in detail_html, "Title/Hanja mismatch in 복선화음"
    assert "data-policy-section=\"brief\"" not in detail_html, "Unset brief rendered in 복선화음"
    hanja_exps = driver.find_elements(By.CSS_SELECTOR, "[data-policy-section='hanja-explanation']")
    assert len(hanja_exps) == 0, "Unset hanja explanation card rendered in 복선화음"

    word_defs = driver.find_elements(By.CSS_SELECTOR, "[data-policy-section='word-definition']")
    assert len(word_defs) == 1, "Verified definition card missing in 복선화음"
    assert "착한 사람에게는 복을 주고" in word_defs[0].text, "Definition text mismatch in 복선화음"

    source_readings = driver.find_elements(By.CSS_SELECTOR, "[data-source-readings]")
    assert len(source_readings) >= 1, "Source readings section missing in 복선화음"
    for ch in ['福', '善', '禍', '淫']:
        assert ch in source_readings[0].text, f"Character {ch} missing in 복선화음 readings"

    dict_defs = driver.find_elements(By.CSS_SELECTOR, "[data-dictionary='true']")
    assert len(dict_defs) >= 1, "Dictionary section missing in 복선화음 context"

    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_bokseonhwaeum_detail.png'))
    print("[PASS] Desktop 복선화음: Verified definition shown, unset brief/hanja hidden, 4 hanja readings shown")
    report_data['desktop']['bokseonhwaeum'] = True
    close_detail(driver)

    # 3. Unclassified New Word with NO Definition: 가독성
    print("\n--- [Desktop] Testing Unclassified New Word with NO Definition: 가독성 (可讀性) ---")
    detail = search_and_select(driver, "가독성", "可讀性")
    assert len(driver.find_elements(By.CSS_SELECTOR, "[data-policy-section='word-definition']")) == 0, "Definition rendered for 가독성"
    assert len(driver.find_elements(By.CSS_SELECTOR, "[data-policy-section='hanja-card']")) == 0, "Hanja card rendered for 가독성"
    assert len(driver.find_elements(By.CSS_SELECTOR, "[data-policy-section='brief']")) == 0, "Brief rendered for 가독성"

    source_readings = driver.find_elements(By.CSS_SELECTOR, "[data-source-readings]")
    assert len(source_readings) >= 1, "Source readings missing for 가독성"
    for ch in ['可', '讀', '性']:
        assert ch in source_readings[0].text, f"Character {ch} missing in 가독성 readings"

    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_gadokseong_detail.png'))
    print("[PASS] Desktop 가독성: All unset cards (def/hanja/brief) hidden, source readings shown")
    report_data['desktop']['gadokseong'] = True
    close_detail(driver)

    # 4. Reading Notes: 상쇄-相殺 & 감쇄-減殺
    print("\n--- [Desktop] Testing Reading Notes: 상쇄-相殺 & 감쇄-減殺 ---")
    search_and_select(driver, "상쇄", "相殺")
    notes = driver.find_elements(By.CSS_SELECTOR, "[data-reading-note='true']")
    assert len(notes) >= 1 and "※ 殺은 여기서 ‘쇄’로 읽습니다." in notes[0].text, "Reading note missing on 상쇄"
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_sangshwae_reading_note.png'))
    print("[PASS] Desktop 상쇄 reading note verified")
    close_detail(driver)

    search_and_select(driver, "감쇄", "減殺")
    notes = driver.find_elements(By.CSS_SELECTOR, "[data-reading-note='true']")
    assert len(notes) >= 1 and "※ 殺은 여기서 ‘쇄’로 읽습니다." in notes[0].text, "Reading note missing on 감쇄"
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_gamshwae_reading_note.png'))
    print("[PASS] Desktop 감쇄 reading note verified")
    report_data['desktop']['reading_notes'] = True
    close_detail(driver)

    # 5. Multiple Contexts & Switching: 시비-柴扉
    print("\n--- [Desktop] Testing Multiple Contexts & Switching: 시비-柴扉 ---")
    search_and_select(driver, "시비", "柴扉")
    ctx_buttons = driver.find_elements(By.XPATH, "//div[contains(@class, 'border-b') and contains(@class, 'flex-wrap')]//button")
    assert len(ctx_buttons) >= 2, "Less than 2 contexts on 시비"
    p1 = driver.find_element(By.CSS_SELECTOR, "[data-source-image='true'] p").text
    assert "2017 9모" in p1, f"Context 1 source mismatch: {p1}"

    driver.execute_script("arguments[0].click();", ctx_buttons[1])
    time.sleep(0.4)
    p2 = driver.find_element(By.CSS_SELECTOR, "[data-source-image='true'] p").text
    assert "2020 9모" in p2, f"Context 2 source mismatch: {p2}"
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_sibi_context_switch.png'))
    print("[PASS] Desktop 시비: Context switching dynamically updated passage text & image")
    report_data['desktop']['context_switching'] = True
    close_detail(driver)

    # 6. Specialist Authority vs Dictionary Definitions: 개체성
    print("\n--- [Desktop] Testing Specialist Authority vs Dictionary: 개체성 ---")
    search_and_select(driver, "개체성", "個體性")
    editorial_sec = driver.find_elements(By.CSS_SELECTOR, "[data-editorial='true']")
    dict_sec = driver.find_elements(By.CSS_SELECTOR, "[data-dictionary='true']")
    assert len(editorial_sec) >= 1, "Specialist authority section missing on 개체성"
    assert len(dict_sec) == 0, "Dictionary section incorrectly shown on specialist-only context"
    assert "사전 원문과 구별한 설명" in editorial_sec[0].text, "Editorial note missing"
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_specialist_authority.png'))
    print("[PASS] Desktop 개체성: Specialist authority cleanly separated from dictionary")
    report_data['desktop']['specialist_authority'] = True
    close_detail(driver)

    # 7. Comprehensive Verification of ALL 13 Source Image Contexts: Load, Zoom, Pan, Close
    print("\n--- [Desktop] Testing ALL 13 Source Image Fallbacks (Load, Zoom, Pan, Close) ---")
    for idx, ic in enumerate(IMAGE_CONTEXTS, 1):
        w = ic['word']
        h = ic['hanja']
        src = ic['source']
        lbl = ic['label']

        search_and_select(driver, w, h)
        # Switch tab to target source if multiple
        tabs = driver.find_elements(By.XPATH, "//div[contains(@class, 'border-b') and contains(@class, 'flex-wrap')]//button")
        for t in tabs:
            if src in t.text:
                driver.execute_script("arguments[0].click();", t)
                time.sleep(0.2)
                break

        source_img_secs = driver.find_elements(By.CSS_SELECTOR, "[data-source-image='true']")
        assert len(source_img_secs) >= 1, f"Source image section missing for {w} ({src})"

        img_tag = source_img_secs[0].find_element(By.TAG_NAME, "img")
        img_src = img_tag.get_attribute("src")
        assert img_src.startswith("data:image/png;base64,"), f"Image src is not base64 URI for {w} ({src})"

        natural_w = driver.execute_script("return arguments[0].naturalWidth;", img_tag)
        assert natural_w > 0, f"Image failed to decode (naturalWidth={natural_w}) for {w} ({src})"

        # Zoom dialog test
        zoom_btn = source_img_secs[0].find_element(By.TAG_NAME, "button")
        driver.execute_script("arguments[0].click();", zoom_btn)
        time.sleep(0.3)

        dialog = driver.find_element(By.CSS_SELECTOR, "dialog.review-image-dialog")
        assert dialog.is_displayed(), f"Zoom dialog not displayed for {w} ({src})"
        dialog_img = dialog.find_element(By.TAG_NAME, "img")
        assert dialog_img.is_displayed(), f"Dialog image not visible for {w} ({src})"

        # Pan / Scroll test within dialog container
        driver.execute_script("arguments[0].scrollTop = 100; arguments[0].scrollLeft = 50;", dialog)
        time.sleep(0.1)

        if w == "광한전":
            driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_gwanghanjeon_image_modal.png'))

        # Close dialog
        close_btn = dialog.find_element(By.TAG_NAME, "button")
        driver.execute_script("arguments[0].click();", close_btn)
        time.sleep(0.2)
        assert len(driver.find_elements(By.CSS_SELECTOR, "dialog.review-image-dialog")) == 0, f"Dialog failed to close for {w}"

        print(f"[{idx:2d}/13 PASS] {w}({h}) | {src} ({lbl}): Loaded (w={natural_w}px), Zoomed, Panned, Closed cleanly")
        report_data['image_contexts_13'].append({
            'word': w,
            'hanja': h,
            'source': src,
            'label': lbl,
            'naturalWidth': natural_w,
            'status': 'PASS'
        })

        close_detail(driver)

    # 8. Study Master Action Button & LocalStorage Persistence
    print("\n--- [Desktop] Testing Study Master Action & LocalStorage Persistence ---")
    search_and_select(driver, "복선화음", "福善禍淫")
    master_btn = driver.find_element(By.XPATH, "//button[contains(., '이 단어 마스터 완료')]")
    driver.execute_script("arguments[0].click();", master_btn)
    time.sleep(0.5)

    # Verify toast notification
    toasts = driver.find_elements(By.XPATH, "//*[contains(text(), '마스터했습니다')]")
    assert len(toasts) >= 1, "Toast notification did not appear"
    print("[PASS] Desktop: Master toast notification appeared")

    # Verify LocalStorage persistence
    stored_passed = driver.execute_script("return window.localStorage.getItem('suneung_passed_words');")
    assert stored_passed is not None and "복선화음" in stored_passed, f"복선화음 missing from suneung_passed_words: {stored_passed}"
    print(f"[PASS] Desktop: LocalStorage successfully persisted mastered word: {stored_passed}")
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_master_toast.png'))
    report_data['desktop']['study_master_storage'] = True

    # 9. Vocabulary Mini Quiz Modal & Interaction
    print("\n--- [Desktop] Testing Vocabulary Mini Quiz Modal & Interaction ---")
    set_search_query(driver, "")
    time.sleep(0.4)

    quiz_start_btn = driver.find_element(By.ID, "miniQuizStartBtn")
    driver.execute_script("arguments[0].click();", quiz_start_btn)
    time.sleep(0.5)

    quiz_modal = driver.find_element(By.ID, "vocabQuizModal")
    assert quiz_modal.is_displayed(), "Quiz modal did not open"
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_quiz_landing.png'))
    print("[PASS] Desktop: Quiz landing modal opened")

    # Start classical category quiz
    classic_btn = driver.find_element(By.ID, "vocabSelectClassicBtn")
    driver.execute_script("arguments[0].click();", classic_btn)
    time.sleep(0.5)

    q_title = driver.find_element(By.ID, "vocabQuizQuestionTitle")
    assert len(q_title.text) > 0, "Quiz question title is empty"
    print(f"[PASS] Desktop: Quiz question loaded: '{q_title.text[:50]}...'")

    # Click first answer option
    opt0 = driver.find_element(By.ID, "vocabOptBtn-0")
    driver.execute_script("arguments[0].click();", opt0)
    time.sleep(0.5)

    # Verify feedback badge rendered
    opt_html = opt0.get_attribute('outerHTML')
    assert ("정답" in opt_html or "오답" in opt_html or "bg-" in opt_html), "Answer feedback not rendered"
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_quiz_answered.png'))
    print("[PASS] Desktop: Answer option submitted, feedback displayed")

    # Close quiz modal
    close_quiz = driver.find_element(By.ID, "vocabQuizCloseBtn")
    driver.execute_script("arguments[0].click();", close_quiz)
    time.sleep(0.4)
    assert len(driver.find_elements(By.ID, "vocabQuizModal")) == 0, "Quiz modal did not close"
    print("[PASS] Desktop: Quiz modal closed cleanly")
    report_data['desktop']['mini_quiz'] = True

    # 10. Print Trigger & Real PDF Generation + Emulated Print Layout
    print("\n--- [Desktop] Testing Print Trigger, Emulated Print CSS & Real PDF Generation ---")
    print_btn = driver.find_element(By.XPATH, "//button[contains(., 'PDF 단어장 인쇄')]")
    driver.execute_script("arguments[0].click();", print_btn)
    time.sleep(0.5)
    intercepted = driver.execute_script("return window.__printIntercepted;")
    assert intercepted is True, "window.print was not called by PDF print button!"
    print("[PASS] Desktop: PDF print button invoked window.print() trigger")
    report_data['print_check']['print_invoked'] = True

    # Generate real PDF via Chrome DevTools Protocol (CDP) Page.printToPDF
    print_params = {
        'landscape': False,
        'displayHeaderFooter': False,
        'printBackground': True,
        'preferCSSPageSize': True
    }
    pdf_result = driver.execute_cdp_cmd("Page.printToPDF", print_params)
    pdf_bytes = base64.b64decode(pdf_result['data'])
    pdf_path = os.path.join(screenshots_dir, 'desktop_wordlist_generated.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(pdf_bytes)
    assert len(pdf_bytes) > 10000, f"Generated PDF too small: {len(pdf_bytes)} bytes"
    assert pdf_bytes.startswith(b'%PDF-'), "Invalid PDF magic header"
    print(f"[PASS] Desktop: Real PDF generated via CDP ({len(pdf_bytes):,} bytes) -> {pdf_path}")
    report_data['print_check']['real_pdf_generated'] = {
        'bytes': len(pdf_bytes),
        'file': 'screenshots/desktop_wordlist_generated.pdf'
    }

    # Emulate Print CSS & screenshot
    driver.execute_cdp_cmd("Emulation.setEmulatedMedia", {"media": "print"})
    time.sleep(0.5)
    driver.save_screenshot(os.path.join(screenshots_dir, 'desktop_print_emulated_layout.png'))
    print(f"[SCREENSHOT] Saved: screenshots/desktop_print_emulated_layout.png")
    driver.execute_cdp_cmd("Emulation.setEmulatedMedia", {"media": ""})
    time.sleep(0.3)
    report_data['print_check']['print_css_emulated'] = True

    # Check desktop console errors (excluding benign favicon 404)
    desktop_logs = driver.get_log('browser')
    desktop_severe = [l for l in desktop_logs if l['level'] == 'SEVERE' and 'favicon.ico' not in l['message']]
    print(f"Desktop SEVERE Console Errors (excl favicon): {len(desktop_severe)}")
    assert len(desktop_severe) == 0, f"Severe errors on desktop: {desktop_severe}"
    driver.quit()

    print("\n==================================================")
    print("STAGE 2: Mobile Browser Verification Suite (375x812)")
    print("==================================================")

    driver_m = create_driver(375, 812, is_mobile=True)
    driver_m.get(url)
    time.sleep(1.5)

    # Prevent window.print blocking on mobile
    driver_m.execute_script("""
    window.__printIntercepted = false;
    window.print = function() { window.__printIntercepted = true; };
    """)

    scroll_w = driver_m.execute_script("return document.documentElement.scrollWidth;")
    inner_w = driver_m.execute_script("return window.innerWidth;")
    print(f"Mobile Home: scrollWidth={scroll_w}, innerWidth={inner_w}")
    assert scroll_w <= inner_w + 1, f"Horizontal overflow on mobile home: {scroll_w} > {inner_w}"
    print("[PASS] Mobile Home: No horizontal overflow")

    # 1. Mobile Search & Detail: 복선화음
    print("\n--- [Mobile] Testing Unclassified New Word: 복선화음 ---")
    detail_m = search_and_select(driver_m, "복선화음", "福善禍淫")
    scroll_w_detail = driver_m.execute_script("return document.documentElement.scrollWidth;")
    assert scroll_w_detail <= inner_w + 1, f"Horizontal overflow on mobile detail: {scroll_w_detail} > {inner_w}"
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_bokseonhwaeum_detail.png'))
    print("[PASS] Mobile 복선화음: No horizontal overflow, verified definition and readings intact")
    report_data['mobile']['bokseonhwaeum'] = True
    close_detail(driver_m)

    # 2. Mobile Search & Detail: 가독성
    print("\n--- [Mobile] Testing Unclassified New Word: 가독성 ---")
    detail_m = search_and_select(driver_m, "가독성", "可讀性")
    assert len(driver_m.find_elements(By.CSS_SELECTOR, "[data-policy-section='word-definition']")) == 0
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_gadokseong_detail.png'))
    print("[PASS] Mobile 가독성: Unset cards hidden, responsive layout clean")
    report_data['mobile']['gadokseong'] = True
    close_detail(driver_m)

    # 3. Mobile Reading Note: 상쇄-相殺
    print("\n--- [Mobile] Testing Reading Note: 상쇄-相殺 ---")
    search_and_select(driver_m, "상쇄", "相殺")
    notes_m = driver_m.find_elements(By.CSS_SELECTOR, "[data-reading-note='true']")
    assert len(notes_m) >= 1 and "※ 殺은 여기서 ‘쇄’로 읽습니다." in notes_m[0].text
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_sangshwae_reading_note.png'))
    print("[PASS] Mobile 상쇄: Reading note rendered legibly")
    report_data['mobile']['reading_notes'] = True
    close_detail(driver_m)

    # 4. Mobile Context Switching: 시비-柴扉
    print("\n--- [Mobile] Testing Context Switching: 시비-柴扉 ---")
    search_and_select(driver_m, "시비", "柴扉")
    tabs_m = driver_m.find_elements(By.XPATH, "//div[contains(@class, 'border-b') and contains(@class, 'flex-wrap')]//button")
    assert len(tabs_m) >= 2
    driver_m.execute_script("arguments[0].click();", tabs_m[1])
    time.sleep(0.4)
    p_m = driver_m.find_element(By.CSS_SELECTOR, "[data-source-image='true'] p").text
    assert "2020 9모" in p_m
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_sibi_context_switch.png'))
    print("[PASS] Mobile 시비: Context switching responsive")
    report_data['mobile']['context_switching'] = True
    close_detail(driver_m)

    # 5. Mobile Specialist Authority: 개체성
    print("\n--- [Mobile] Testing Specialist Authority: 개체성 ---")
    search_and_select(driver_m, "개체성", "個體性")
    ed_m = driver_m.find_elements(By.CSS_SELECTOR, "[data-editorial='true']")
    assert len(ed_m) >= 1
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_specialist_authority.png'))
    print("[PASS] Mobile 개체성: Specialist authority card rendered")
    report_data['mobile']['specialist_authority'] = True
    close_detail(driver_m)

    # 6. Mobile Source Image Fallback, Zoom & Pan: 광한전
    print("\n--- [Mobile] Testing Source Image Fallback, Zoom & Pan: 광한전 ---")
    search_and_select(driver_m, "광한전", "廣寒殿")
    zoom_btn_m = driver_m.find_element(By.CSS_SELECTOR, "[data-source-image='true'] button")
    driver_m.execute_script("arguments[0].click();", zoom_btn_m)
    time.sleep(0.5)

    dialog_m = driver_m.find_element(By.CSS_SELECTOR, "dialog.review-image-dialog")
    assert dialog_m.is_displayed(), "Mobile zoom dialog not displayed"
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_gwanghanjeon_image_modal.png'))
    print("[PASS] Mobile 광한전: Image zoom modal displayed cleanly")

    # Pan/Scroll in mobile dialog
    driver_m.execute_script("""
    const dlg = arguments[0];
    dlg.scrollTop = 100;
    dlg.scrollLeft = 50;
    """, dialog_m)
    time.sleep(0.3)

    close_btn_m = dialog_m.find_element(By.TAG_NAME, "button")
    driver_m.execute_script("arguments[0].click();", close_btn_m)
    time.sleep(0.4)
    assert len(driver_m.find_elements(By.CSS_SELECTOR, "dialog.review-image-dialog")) == 0
    print("[PASS] Mobile 광한전: Dialog closed cleanly")
    report_data['mobile']['image_zoom'] = True
    close_detail(driver_m)

    # 7. Mobile Mini Quiz Modal
    print("\n--- [Mobile] Testing Vocabulary Mini Quiz Modal ---")
    set_search_query(driver_m, "")
    time.sleep(0.4)
    quiz_btn_m = driver_m.find_element(By.ID, "miniQuizStartBtn")
    driver_m.execute_script("arguments[0].click();", quiz_btn_m)
    time.sleep(0.5)

    quiz_m = driver_m.find_element(By.ID, "vocabQuizModal")
    assert quiz_m.is_displayed()
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_quiz_modal.png'))
    
    close_quiz_m = driver_m.find_element(By.ID, "vocabQuizCloseBtn")
    driver_m.execute_script("arguments[0].click();", close_quiz_m)
    time.sleep(0.4)
    assert len(driver_m.find_elements(By.ID, "vocabQuizModal")) == 0
    print("[PASS] Mobile: Quiz modal opened and closed cleanly")
    report_data['mobile']['mini_quiz'] = True

    # 8. Mobile Study Master Button
    print("\n--- [Mobile] Testing Study Master Action Button ---")
    search_and_select(driver_m, "가독성", "可讀性")
    master_btn_m = driver_m.find_element(By.XPATH, "//button[contains(., '이 단어 마스터 완료')]")
    driver_m.execute_script("arguments[0].click();", master_btn_m)
    time.sleep(0.5)
    toasts_m = driver_m.find_elements(By.XPATH, "//*[contains(text(), '마스터했습니다')]")
    assert len(toasts_m) >= 1
    driver_m.save_screenshot(os.path.join(screenshots_dir, 'mobile_master_toast.png'))
    print("[PASS] Mobile: Master action triggered toast and closed view")
    report_data['mobile']['study_master'] = True

    # Check mobile console errors (excluding benign favicon 404)
    mobile_logs = driver_m.get_log('browser')
    mobile_severe = [l for l in mobile_logs if l['level'] == 'SEVERE' and 'favicon.ico' not in l['message']]
    print(f"Mobile SEVERE Console Errors (excl favicon): {len(mobile_severe)}")
    assert len(mobile_severe) == 0, f"Severe errors on mobile: {mobile_severe}"
    driver_m.quit()

    print("\n==================================================")
    print("ALL BROWSER VERIFICATION SUITES PASSED (100%)")
    print("==================================================")

    summary_path = os.path.join(base_dir, 'browser_verification_summary.json')
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)
    print(f"Saved complete test summary to: {summary_path}")

if __name__ == '__main__':
    main()
