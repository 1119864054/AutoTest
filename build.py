import os

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def kill():
    os.system("taskkill /F /IM iedriverserver.exe /T")
    os.system("taskkill /F /IM iexplore.exe /T")
    os.system("taskkill /F /IM chrome.exe /T")


def get_element(driver, loc_type, loc_expression):

    try:
        element = WebDriverWait(driver, 30).until(
            lambda x: x.find_element(by=loc_type, value=loc_expression))

    except Exception as e:
        raise e

    finally:
        driver.quit()


if __name__ == '__main__':
    kill()
    url = "https://www.dogedoge.com/"
    driver = webdriver.Chrome()
    driver.get("https://www.dogedoge.com/")
    search_box = get_element(driver, "id", "wedonttrack")
    print(search_box)
