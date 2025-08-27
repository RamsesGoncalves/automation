import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from .config import settings


def sleep_if_display_mode() -> None:
    if settings.display_mode:
        time.sleep(max(settings.step_delay_ms, 0) / 1000.0)


def highlight_element(driver: WebDriver, element: WebElement, color: str = "#ffcc00", thickness: str = "3px") -> None:
    try:
        driver.execute_script(
            "arguments[0].style.outline = arguments[1]; arguments[0].style.outlineOffset = '2px';",
            element,
            f"{thickness} solid {color}",
        )
    except Exception:
        # Ignora erros de highlight para não quebrar o fluxo
        pass
