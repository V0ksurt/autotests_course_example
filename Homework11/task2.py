# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
fix_auth = 'https://fix-sso.sbis.ru/auth-online/?ret=fix-online.sbis.ru/'
message = 'Привет'
person_name = 'Коржов Коржик'

try:
    browser.get(fix_auth)
    sleep(1)

    login = browser.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('DZautotest')
    button_login = browser.find_element(By.CSS_SELECTOR, '[tabindex="2"].controls-BaseButton')
    button_login.click()
    password = browser.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('DZautotest123')
    buttons_password = browser.find_element(By.CSS_SELECTOR, '[tabindex="4"]')
    buttons_password.click()
    sleep(3)

    browser.get('https://fix-online.sbis.ru/page/dialogs')
    sleep(2)
    icon_plus = browser.find_element(By.CLASS_NAME, 'icon-RoundPlus')
    icon_plus.click()
    sleep(2)
    search = browser.find_element(By.CSS_SELECTOR, ".controls-StackTemplate__top-area-content "
                                                   ".controls-Search__nativeField_caretEmpty")
    search.send_keys(person_name)
    sleep(1)
    find_person = browser.find_element(By.CSS_SELECTOR, ".msg-addressee-item [title='Коржов Коржик']")
    find_person.click()
    sleep(1)
    msg_box = browser.find_element(By.CSS_SELECTOR, "[role='textbox']")
    msg_box.send_keys(message)
    sleep(1)
    send_btn = browser.find_element(By.CSS_SELECTOR, ".icon-BtArrow")
    send_btn.click()
    sleep(2)
    sent_messages = browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')
    assert sent_messages[0].text == message, 'Отправленное сообщение отсутствует в реестре!'
    action_chain = ActionChains(browser)
    action_chain.move_to_element(sent_messages[0])
    action_chain.perform()
    delete_btn = browser.find_element(By.CSS_SELECTOR, ".controls-icon_style-danger")
    delete_btn.click()
    sleep(1)
    assert browser.find_elements(By.CSS_SELECTOR, '.msg-dialogs-item p')[0] != message, 'Сообщение не удалено!'
    sleep(2)




finally:
    browser.quit()