from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from ..config import Locators, settings
from ..utils import highlight_element, sleep_if_display_mode


class ScreenNine:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, settings.explicit_wait)

    def run(self) -> None:
        btn_el = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_NINE_BUTTON_XPATH))
        )
        highlight_element(self.driver, btn_el)
        sleep_if_display_mode()
        btn_el.click()
        sleep_if_display_mode()


