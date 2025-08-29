from nt import scandir
import os
from dataclasses import dataclass
from turtle import Screen
from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    url: str = os.getenv("URL", "")
    browser: str = os.getenv("BROWSER", "chrome").lower()
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"

    # Modo de exibição (headed) e delay entre passos
    display_mode: bool = os.getenv("DISPLAY_MODE", "false").lower() == "true"
    step_delay_ms: int = int(os.getenv("STEP_DELAY_MS", "600"))

    # Comportamento de janela e erros
    keep_open: bool = os.getenv("KEEP_OPEN", "false").lower() == "true"
    stop_on_error: bool = os.getenv("STOP_ON_ERROR", "true").lower() == "true"

    # Tamanho da janela
    window_width: int = int(os.getenv("WINDOW_WIDTH", "1366"))
    window_height: int = int(os.getenv("WINDOW_HEIGHT", "768"))

    # Anexar a navegador já aberto
    attach_to_browser: bool = os.getenv("ATTACH_TO_BROWSER", "false").lower() == "true"
    debugger_address: str = os.getenv("DEBUGGER_ADDRESS", "127.0.0.1:9222")
    open_new_tab: bool = os.getenv("OPEN_NEW_TAB", "false").lower() == "true"

    # CSV
    csv_path: str = os.getenv("CSV_PATH", "src/plan/teste.csv")

    # Valores por tela (fallbacks opcionais)
    input_one_value: str = os.getenv("INPUT_ONE_VALUE", "")
    input_two_value: str = os.getenv("INPUT_TWO_VALUE", "")
    input_three_value: str = os.getenv("INPUT_THREE_VALUE", "")
    input_four_value: str = os.getenv("INPUT_FOUR_VALUE", "")
    input_four_validate_value: str = os.getenv("INPUT_FOUR_VALIDATE_VALUE", "")
    input_five_value: str = os.getenv("INPUT_FIVE_VALUE", "")
    input_six_value: str = os.getenv("INPUT_SIX_VALUE", "")

    implicit_wait: int = int(os.getenv("IMPLICIT_WAIT", "2"))
    explicit_wait: int = int(os.getenv("EXPLICIT_WAIT", "15"))
    page_load_timeout: int = int(os.getenv("PAGE_LOAD_TIMEOUT", "30"))
    script_timeout: int = int(os.getenv("SCRIPT_TIMEOUT", "30"))


class Locators:
    # Preencha os XPaths abaixo. Ex.: "//input[@id='login']"

    SCREEN_ZERO_INPUT_XPATH = "//a[normalize-space(.)='Criar']" # informação 1

    SCREEN_ONE_INPUT_XPATH = "//input[@type='text']" # informação 4
    SCREEN_ONE_BUTTON_INPUT_XPATH = "//button[@class='list-group-item list-group-item-action']"
    SCREEN_ONE_PROCEED_XPATH = "//button[@class='btn btn-primary mr-2']"

    SCREEN_TWO_INPUT_XPATH = "//input[@type='text']" # informação 5
    SCREEN_TWO_BUTTON_INPUT_XPATH = "//button[@class='list-group-item list-group-item-action']"
    SCREEN_TWO_PROCEED_XPATH = "//button[@class='btn btn-primary mr-2']"

    SCREEN_THREE_INPUT_XPATH = "//input[@type='text']" # informação 6
    SCREEN_THREE_BUTTON_INPUT_XPATH = "//button[@class='list-group-item list-group-item-action']"
    SCREEN_THREE_PROCEED_XPATH = "//button[@class='btn btn-primary mr-2']"

    SCREEN_FOUR_INPUT_XPATH = "//input[@type='text']" # informação 7
    SCREEN_FOUR_BUTTON_INPUT_XPATH = "//button[@class='list-group-item list-group-item-action']"
    SCREEN_FOUR_INPUT_VALIDATE_XPATH = "//input[@id='nomeRepositorio']" # informação 1
    SCREEN_FOUR_BUTTON_VALIDATE_XPATH = "//button[@class='btn btn-primary']"
    SCREEN_FOUR_STRONG_ASSERT_XPATH = "//button[@class='btn btn-primary mr-2']"
    SCREEN_FOUR_BUTTON_PROCEED_XPATH = "//button[@class='btn btn-primary mr-2']"

    SCREEN_FIVE_INPUT_XPATH = "//input[@type='text']" # informação 8
    SCREEN_FIVE_BUTTON_INPUT_XPATH = "//button[@class='list-group-item list-group-item-action']"
    SCREEN_FIVE_PROCEED_XPATH = "//button[@class='btn btn-primary mr-2']"

    SCREEN_SIX_INPUT_XPATH = "//label[normalize-space(.)='Ambiente:']/following-sibling::div[1]//input" # informação 9
    SCREEN_SIX_INPUT_TYPE_XPATH = "//label[normalize-space(.)='Tipo Exposição:']/following-sibling::div[1]//input" # informação 10
    SCREEN_SIX_INPUT_GATEWAY_XPATH = "//label[normalize-space(.)='Gateway:']/following-sibling::div[1]//input" # informação 11
    SCREEN_SIX_BUTTON_INPUT_XPATH = "//button[@class='list-group-item list-group-item-action']"
    SCREEN_SIX_PROCEED_XPATH = "//button[@class='btn btn-primary mr-2']"
    
    SCREEN_SEVEN_INPUT_XPATH = "//input[@type='text']" # informação 12
    SCREEN_SEVEN_PROCEED_XPATH = "//button[@class='btn btn-success']"

    SCREEN_EIGHT_PROCEED_XPATH = "//button[@class='btn btn-danger me-2']" # "//button[@class='btn btn-primary']" 

    SCREEN_NINE_BUTTON_XPATH = "//a[normalize-space(.)='Consultar']" # informação 13


settings = Settings()


def validate_config() -> None:
    if not settings.url:
        raise ValueError("URL não configurada. Defina URL no arquivo .env")
    # Demais XPaths agora são fornecidos; deixamos a validação para exceções de espera
