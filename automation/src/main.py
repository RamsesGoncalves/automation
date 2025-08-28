import time
from selenium.common.exceptions import TimeoutException

from .config import settings, validate_config
from .driver import build_driver
from .pages import (
	ScreenOne,
	ScreenTwo,
	ScreenThree,
	ScreenFour,
	ScreenFive,
	ScreenSix,
	ScreenSeven,
	ScreenEight,
)
from .csv_loader import load_csv_rows


# Mapeamento de colunas (0-based) conforme comentários de informação no config:
# informação 1 -> coluna 0, informação 4 -> coluna 3, informação 5 -> coluna 4, informação 6 -> coluna 5,
# informação 7 -> coluna 6, informação 8 -> coluna 7, informação 9 -> coluna 8, informação 10 -> coluna 9,
# informação 11 -> coluna 10, informação 12 -> coluna 11
COLUMN_MAP = {
	1: 0,
	4: 3,
	5: 4,
	6: 5,
	7: 6,
	8: 7,
	9: 8,
	10: 9,
	11: 10,
	12: 11,
}


def run_for_row(driver, row_values):
	# Extrai valores conforme mapeamento
	val_info4 = row_values[COLUMN_MAP[4]] if len(row_values) > COLUMN_MAP[4] else ""
	val_info5 = row_values[COLUMN_MAP[5]] if len(row_values) > COLUMN_MAP[5] else ""
	val_info6 = row_values[COLUMN_MAP[6]] if len(row_values) > COLUMN_MAP[6] else ""
	val_info7 = row_values[COLUMN_MAP[7]] if len(row_values) > COLUMN_MAP[7] else ""
	val_info1 = row_values[COLUMN_MAP[1]] if len(row_values) > COLUMN_MAP[1] else ""
	val_info8 = row_values[COLUMN_MAP[8]] if len(row_values) > COLUMN_MAP[8] else ""
	val_info9 = row_values[COLUMN_MAP[9]] if len(row_values) > COLUMN_MAP[9] else ""
	val_info10 = row_values[COLUMN_MAP[10]] if len(row_values) > COLUMN_MAP[10] else ""
	val_info11 = row_values[COLUMN_MAP[11]] if len(row_values) > COLUMN_MAP[11] else ""
	val_info12 = row_values[COLUMN_MAP[12]] if len(row_values) > COLUMN_MAP[12] else ""

	# Abre URL no início de cada execução
	driver.get(settings.url)
	time.sleep(30)  # aguarda 1 minuto antes de iniciar as interações

	print("Tela 1...")
	ScreenOne(driver).fill_and_proceed(val_info4 or settings.input_one_value)

	print("Tela 2...")
	ScreenTwo(driver).fill_and_proceed(val_info5 or settings.input_two_value)

	print("Tela 3...")
	flow_value = val_info6 or settings.input_three_value
	ScreenThree(driver).run(flow_value)

	print("Tela 4...")
	ScreenFour(driver).run(
		val_info7 or settings.input_four_value,
		val_info1 or settings.input_four_validate_value,
	)

	# Decisão de fluxo com base na Tela 3 (informação 6)
	normalized_flow = (flow_value or "").strip().lower()
	is_negative_flow = normalized_flow in ("não", "nao", "n")

	if not is_negative_flow:
		print("Tela 5...")
		ScreenFive(driver).run(val_info8 or settings.input_five_value)

		print("Tela 6...")
		ScreenSix(driver).run(
			val_info9 or settings.input_six_value,
			val_info10 or settings.input_six_value,
			val_info11 or settings.input_six_value,
		)
	else:
		print("Fluxo 'não' na Tela 3: pulando telas 5 e 6...")

	print("Tela 7...")
	ScreenSeven(driver).run(val_info12 or settings.input_six_value)

	print("Tela 8...")
	ScreenEight(driver).run()


def run() -> None:
	validate_config()
	rows = load_csv_rows(settings.csv_path)
	if not rows:
		print("CSV sem linhas (após cabeçalho). Nada a executar.")
		return

	print(f"Foram encontradas {len(rows)} linha(s) no CSV (excluindo cabeçalho).")
	choice = input("Executar todas as linhas? (s/N) ").strip().lower()
	indices = list(range(len(rows)))
	if choice not in ("s", "sim", "y", "yes"):
		while True:
			idx_str = input(f"Informe o número da linha (1..{len(rows)}): ").strip()
			if not idx_str.isdigit():
				print("Digite um número válido.")
				continue
			idx = int(idx_str)
			if 1 <= idx <= len(rows):
				indices = [idx - 1]
				break
			print("Fora do intervalo. Tente novamente.")

	driver = build_driver(settings)
	try:
		# Se anexando a um navegador já aberto, pode ser útil abrir nova aba só uma vez
		if settings.attach_to_browser and settings.open_new_tab:
			driver.switch_to.new_window("tab")

		for i in indices:
			print(f"\n=== Executando linha {i+1}/{len(rows)} ===")
			try:
				run_for_row(driver, rows[i])
			except TimeoutException as ex:
				print(f"Timeout na linha {i+1}: {ex}")
				if settings.display_mode and settings.stop_on_error:
					input("[DISPLAY_MODE] Pressione Enter para continuar...")
			except Exception as ex:
				print(f"Erro na linha {i+1}: {ex}")
				if settings.display_mode and settings.stop_on_error:
					input("[DISPLAY_MODE] Pressione Enter para continuar...")

		print("\nExecução finalizada.")
	finally:
		if not (settings.display_mode and settings.keep_open) and not settings.attach_to_browser:
			driver.quit()


if __name__ == "__main__":
	run()
