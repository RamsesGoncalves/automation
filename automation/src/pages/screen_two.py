from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from ..config import Locators, settings
from ..utils import highlight_element, sleep_if_display_mode


class ScreenTwo:
	def __init__(self, driver: WebDriver) -> None:
		self.driver = driver
		self.wait = WebDriverWait(driver, settings.explicit_wait)

	def fill_and_proceed(self, value: str) -> None:
		input_el = self.wait.until(
			EC.visibility_of_element_located((By.XPATH, Locators.SCREEN_TWO_INPUT_XPATH))
		)
		highlight_element(self.driver, input_el)
		sleep_if_display_mode()
		input_el.clear()
		input_el.send_keys(value)
		sleep_if_display_mode()

		# Clicar no botão de sugestão
		suggestion_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_TWO_BUTTON_INPUT_XPATH))
		)
		highlight_element(self.driver, suggestion_btn)
		sleep_if_display_mode()
		suggestion_btn.click()
		sleep_if_display_mode()

		proceed_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_TWO_PROCEED_XPATH))
		)
		highlight_element(self.driver, proceed_btn)
		sleep_if_display_mode()
		proceed_btn.click()
		sleep_if_display_mode()
