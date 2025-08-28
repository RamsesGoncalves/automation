from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

from ..config import Locators, settings
from ..utils import highlight_element, sleep_if_display_mode


class ScreenSix:
	def __init__(self, driver: WebDriver) -> None:
		self.driver = driver
		self.wait = WebDriverWait(driver, settings.explicit_wait)

	def run(self, ambiente_value: str, tipo_value: str, gateway_value: str) -> None:
		# Ambiente
		amb_input = self.wait.until(
			EC.visibility_of_element_located((By.XPATH, Locators.SCREEN_SIX_INPUT_XPATH))
		)
		highlight_element(self.driver, amb_input)
		sleep_if_display_mode()
		amb_input.clear()
		amb_input.send_keys(ambiente_value)
		sleep_if_display_mode()

		suggestion_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_SIX_BUTTON_INPUT_XPATH))
		)
		highlight_element(self.driver, suggestion_btn)
		sleep_if_display_mode()
		suggestion_btn.click()
		sleep_if_display_mode()

		# Tipo Exposição
		tipo_input = self.wait.until(
			EC.visibility_of_element_located((By.XPATH, Locators.SCREEN_SIX_INPUT_TYPE_XPATH))
		)
		highlight_element(self.driver, tipo_input)
		sleep_if_display_mode()
		tipo_input.clear()
		tipo_input.send_keys(tipo_value)
		sleep_if_display_mode()

		suggestion_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_SIX_BUTTON_INPUT_XPATH))
		)
		highlight_element(self.driver, suggestion_btn)
		sleep_if_display_mode()
		suggestion_btn.click()
		sleep_if_display_mode()

		# Gateway
		gate_input = self.wait.until(
			EC.visibility_of_element_located((By.XPATH, Locators.SCREEN_SIX_INPUT_GATEWAY_XPATH))
		)
		highlight_element(self.driver, gate_input)
		sleep_if_display_mode()
		gate_input.clear()
		gate_input.send_keys(gateway_value)
		sleep_if_display_mode()

		suggestion_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_SIX_BUTTON_INPUT_XPATH))
		)
		highlight_element(self.driver, suggestion_btn)
		sleep_if_display_mode()
		suggestion_btn.click()
		sleep_if_display_mode()

		# Prosseguir
		proceed_btn = self.wait.until(
			EC.element_to_be_clickable((By.XPATH, Locators.SCREEN_SIX_PROCEED_XPATH))
		)
		highlight_element(self.driver, proceed_btn)
		sleep_if_display_mode()
		proceed_btn.click()
		sleep_if_display_mode()
