import csv
from typing import List
from pathlib import Path


def load_csv_rows(csv_path: str) -> List[List[str]]:
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV não encontrado: {csv_path}")
    rows: List[List[str]] = []
    with path.open(mode="r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        # Ignora cabeçalho
        header_skipped = False
        for row in reader:
            if not header_skipped:
                header_skipped = True
                continue
            # Remove espaços extras nas células
            rows.append([col.strip() for col in row])
    return rows
