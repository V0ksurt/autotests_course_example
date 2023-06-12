# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
browser.maximize_window()
sbis_site = 'https://sbis.ru/'

try:
    browser.get(sbis_site)
    sleep(1)

    tab_contacts = browser.find_element(By.CSS_SELECTOR, '[href="/contacts"].sbisru-Header__menu-link--hover')
    tab_contacts.click()
    sleep(1)

    banner_tensor = browser.find_element(By.CSS_SELECTOR, '[id="contacts_clients"] .sbisru-Contacts__logo-tensor')
    banner_tensor.click()
    browser.switch_to.window(browser.window_handles[1])
    sleep(1)

    check_blok_news_power_of_humans = browser.find_element(By.CLASS_NAME, 'tensor_ru-Index__block4-content')
    check_blok_news_power_of_humans.is_displayed()
    sleep(1)

    button_podrobnee_blok_news_power_of_humans = browser.find_element(By.CSS_SELECTOR,
                                                                      '[href="/about"].tensor_ru-Header__menu-link')
    button_podrobnee_blok_news_power_of_humans.click()
    assert browser.current_url == 'https://tensor.ru/about', \
        f'Неверно открыт сайт. Ожидали: https://tensor.ru/about. Получили: {browser.current_url}'
finally:
    browser.quit()