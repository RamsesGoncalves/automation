from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time

from ..config import Locators, settings
from ..utils import highlight_element, sleep_if_display_mode


class ScreenFour:
	def __init__(self, driver: WebDriver) -> None:
		self.driver = driver
		self.wait = WebDriverWait(driver, settings.explicit_wait)

	def run(self, value: str, validate_value: str) -> None:
		# Preenche campo principal e clica sugestão
		input_el = self.wait.until(
			EC.visibility_of_element_located((By.XPATH, Locators.SCREEN_FOUR_INPUT_XPATH))
		)
		highlight_element(self.driver, input_el)
		sleep_if_display_mode()
		input_el.clear()
		input_el.send_keys(value)
		sleep_if_display_mode()

		suggestion_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_FOUR_BUTTON_INPUT_XPATH))
		)
		highlight_element(self.driver, suggestion_btn)
		sleep_if_display_mode()
		suggestion_btn.click()
		sleep_if_display_mode()

		# Preenche campo de validação e clica validar
		validate_input = self.wait.until(
			EC.visibility_of_element_located((By.XPATH, Locators.SCREEN_FOUR_INPUT_VALIDATE_XPATH))
		)
		highlight_element(self.driver, validate_input)
		sleep_if_display_mode()
		validate_input.clear()
		validate_input.send_keys(validate_value)
		sleep_if_display_mode()

		validate_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_FOUR_BUTTON_VALIDATE_XPATH))
		)
		highlight_element(self.driver, validate_btn)
		sleep_if_display_mode()
		validate_btn.click()

		# Aguarda 2s para o strong_assert aparecer
		time.sleep(2)
		self.wait.until(
			EC.visibility_of_element_located((By.XPATH, Locators.SCREEN_FOUR_STRONG_ASSERT_XPATH))
		)
		sleep_if_display_mode()

		# Prosseguir
		proceed_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_FOUR_BUTTON_PROCEED_XPATH))
		)
		highlight_element(self.driver, proceed_btn)
		sleep_if_display_mode()
		proceed_btn.click()
		sleep_if_display_mode()
