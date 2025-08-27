from typing import Literal
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.remote.webdriver import WebDriver

from .config import Settings


BrowserName = Literal["chrome", "edge"]


def _build_chrome(headless: bool, detach: bool, width: int, height: int, attach: bool, debugger_address: str) -> WebDriver:
	options = ChromeOptions()
	if attach:
		# Conecta ao Chrome já aberto em modo remoto: chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\\ChromeDebug"
		options.add_experimental_option("debuggerAddress", debugger_address)
	else:
		if headless:
			options.add_argument("--headless=new")
		options.add_argument("--disable-gpu")
		options.add_argument(f"--window-size={width},{height}")
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-dev-shm-usage")
		if detach:
			# Mantém a janela aberta após o término do script (apenas Chrome)
			options.add_experimental_option("detach", True)
	return webdriver.Chrome(options=options)


def _build_edge(headless: bool, width: int, height: int, attach: bool, debugger_address: str) -> WebDriver:
	options = EdgeOptions()
	if attach:
		# Conecta ao Edge já aberto em modo remoto: msedge.exe --remote-debugging-port=9222 --user-data-dir="C:\\EdgeDebug"
		options.add_experimental_option("debuggerAddress", debugger_address)
	else:
		if headless:
			options.add_argument("--headless=new")
		options.add_argument("--disable-gpu")
		options.add_argument(f"--window-size={width},{height}")
		options.add_argument("--no-sandbox")
		options.add_argument("--disable-dev-shm-usage")
	return webdriver.Edge(options=options)


def build_driver(settings: Settings) -> WebDriver:
	browser: BrowserName = "chrome" if settings.browser not in ("chrome", "edge") else settings.browser  # type: ignore[assignment]
	# DISPLAY_MODE força modo com janela (headed) quando não anexando
	effective_headless = settings.headless and (not settings.display_mode) and (not settings.attach_to_browser)
	if browser == "chrome":
		driver = _build_chrome(
			effective_headless,
			detach=(settings.display_mode or settings.keep_open) and (not settings.attach_to_browser),
			width=settings.window_width,
			height=settings.window_height,
			attach=settings.attach_to_browser,
			debugger_address=settings.debugger_address,
		)
	else:
		driver = _build_edge(
			effective_headless,
			width=settings.window_width,
			height=settings.window_height,
			attach=settings.attach_to_browser,
			debugger_address=settings.debugger_address,
		)

	driver.set_page_load_timeout(settings.page_load_timeout)
	driver.set_script_timeout(settings.script_timeout)
	driver.implicitly_wait(settings.implicit_wait)
	return driver
